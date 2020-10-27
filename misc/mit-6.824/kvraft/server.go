package kvraft

import (
	"bytes"
	"fmt"
	"sync"
	"sync/atomic"
	"time"

	"../labgob"
	"../labrpc"
	"../raft"
)

type Op struct {
	// Your definitions here.
	// Field names must start with capital letters,
	// otherwise RPC will break.
	Cmd       string
	Key       string
	Value     string
	ServerId  int
	RpcId     int32
	ClientId  int32
	RequestId int32
}

type OpResult struct {
	RequestId int32
	Value     string
}

func (op *Op) String() string {
	return fmt.Sprintf("op(cmd=%s, key=%s, value='%s', serverId=%d, rpcId=%d, clientId=%d, requestId=%d)",
		op.Cmd, op.Key, op.Value, op.ServerId, op.RpcId, op.ClientId, op.RequestId)
}

type KVServer struct {
	mu      sync.Mutex
	me      int
	rf      *raft.Raft
	applyCh chan raft.ApplyMsg
	dead    int32 // set by Kill()

	maxraftstate int // snapshot if log grows this big
	persister    *raft.Persister

	// Your definitions here.
	data           map[string]string
	dedup          map[int32]*OpResult
	lastApplyIndex int
	lastApplyTerm  int
	lastApplyTime  time.Time
	rpcTrace       map[int32]time.Time
	ansBuffer      map[int32]chan *ApplyAnswer
	moreLogsCond   *sync.Cond
}

func (kv *KVServer) Lock() {
	kv.mu.Lock()
}

func (kv *KVServer) Unlock() {
	kv.mu.Unlock()
}

type ApplyAnswer struct {
	Term  int
	Index int
	Err   Err
	Value string
}

func (kv *KVServer) enterRpc(rpcId int32) {
	kv.Lock()
	defer kv.Unlock()
	kv.rpcTrace[rpcId] = time.Now()
}

func (kv *KVServer) exitRpc(rpcId int32) {
	kv.Lock()
	defer kv.Unlock()
	delete(kv.rpcTrace, rpcId)
}

func (kv *KVServer) createRpcChan(rpcId int32) chan *ApplyAnswer {
	ch := make(chan *ApplyAnswer, 1)
	kv.Lock()
	defer kv.Unlock()
	kv.ansBuffer[rpcId] = ch
	return ch
}

func (kv *KVServer) deleteRpcChan(rpcId int32) {
	kv.Lock()
	defer kv.Unlock()
	delete(kv.ansBuffer, rpcId)
}

func (kv *KVServer) submitAnswer(msg *raft.ApplyMsg, ans *ApplyAnswer) {
	op := msg.Command.(Op)
	if op.ServerId == kv.me {
		rpcId := op.RpcId
		ch := kv.ansBuffer[rpcId]
		if ch != nil {
			ch <- ans
		}
	}
}

func (kv *KVServer) WaitAnswer(index int, term int, ch chan *ApplyAnswer) *ApplyAnswer {
	for {
		if kv.killed() {
			return nil
		}

		currentTerm, _ := kv.rf.GetState()
		if currentTerm != term {
			return nil
		}

		select {
		case ans := <-ch:
			{
				return ans
			}
		case <-time.After(500 * time.Millisecond):
			{
			}
		}
	}
}

func (kv *KVServer) StartAndWaitAnswer(op *Op) (err Err, ans string) {
	err, ans = ErrWrongLeader, ""

	rpcId := op.RpcId
	kv.enterRpc(rpcId)
	defer kv.exitRpc(rpcId)
	defer func() {
		DPrintf("kv%d: return rpc#%d -> reply(%s,'%s')", kv.me, rpcId, err, TrimString(ans))
	}()

	ch := kv.createRpcChan(rpcId)
	defer kv.deleteRpcChan(rpcId)

	index, term, isLeader := kv.rf.Start(*op)
	DPrintf("kv%d: start rpc#%d -> reply(term=%d, index=%d, isLeader=%v)", kv.me, rpcId, term, index, isLeader)
	if !isLeader {
		return
	}

	res := kv.WaitAnswer(index, term, ch)
	if res == nil {
		return
	}
	if res.Index != index {
		panic(fmt.Sprintf("command index disagree. res = %d, exp = %d", res.Index, index))
	}
	if res.Term != term {
		msg := fmt.Sprintf("kv%d: %s -> term disagree. res = %d, exp = %d", kv.me, op, res.Term, term)
		DPrintf(msg)
	} else {
		err = res.Err
		ans = res.Value
	}
	return
}

func (kv *KVServer) Get(args *GetArgs, reply *GetReply) {
	// Your code here.
	rpcId := args.RpcId
	op := Op{
		Cmd:       OpGet,
		Key:       args.Key,
		ServerId:  kv.me,
		RpcId:     rpcId,
		ClientId:  args.ClientId,
		RequestId: args.RequestId,
	}
	err, value := kv.StartAndWaitAnswer(&op)
	reply.Err = err
	reply.Value = value
}

func (kv *KVServer) PutAppend(args *PutAppendArgs, reply *PutAppendReply) {
	// Your code here.
	rpcId := args.RpcId
	op := Op{
		Cmd:       args.Op,
		Key:       args.Key,
		Value:     args.Value,
		ServerId:  kv.me,
		RpcId:     rpcId,
		ClientId:  args.ClientId,
		RequestId: args.RequestId,
	}
	err, _ := kv.StartAndWaitAnswer(&op)
	reply.Err = err
}

func (kv *KVServer) applyOp(op *Op) (err Err, ans string) {
	ans = ""
	err = OK

	key := op.Key
	value := op.Value
	cmd := op.Cmd

	// dedup first
	clientId := op.ClientId
	requestId := op.RequestId
	serverId := op.ServerId
	rpcId := op.RpcId
	p, ok := kv.dedup[clientId]
	if ok && p.RequestId == requestId {
		ans = p.Value
		DPrintf("kv%d: duplicated message(cmd=%s, key=%s, clientId=%d, requestId=%d, rpcId=%d, serverId=%d)",
			kv.me, cmd, key, clientId, requestId, rpcId, serverId)
		return
	}

	switch cmd {
	case OpGet:
		{
			p, ok := kv.data[key]
			if !ok {
				p = ""
			}
			ans = p
		}
	case OpAppend:
		{
			p, ok := kv.data[key]
			if !ok {
				p = ""
			}
			p = p + value
			kv.data[key] = p
		}
	case OpPut:
		{
			kv.data[key] = value
		}
	default:
		panic(fmt.Sprintf("unknown cmd: %s", cmd))
	}

	res := OpResult{
		RequestId: requestId,
		Value:     ans,
	}
	kv.dedup[clientId] = &res
	return
}

func (kv *KVServer) applyMessage(msg *raft.ApplyMsg) {
	if msg.CommandValid {
		op := msg.Command.(Op)
		byMe := (op.ServerId == kv.me)
		if byMe {
			DPrintf("kv%d: Leader apply message %v, term = %d, index = %d", kv.me, &op, msg.CommandTerm, msg.CommandIndex)
		}
		DPrintf("kv%d: apply message %v, term = %d, index = %d", kv.me, &op, msg.CommandTerm, msg.CommandIndex)

		kv.Lock()
		if msg.CommandIndex > kv.lastApplyIndex && msg.CommandIndex != (kv.lastApplyIndex+1) {
			panic(fmt.Sprintf("kv%d: apply message index not consecutive. msgIndex = %d, applyIndex = %d", kv.me, msg.CommandIndex, kv.lastApplyIndex))
		}
		// 如果这个日志已经执行过的话，那么就不要继续执行了
		if msg.CommandIndex <= kv.lastApplyIndex {
			kv.Unlock()
			return
		}
		err, value := kv.applyOp(&op)
		kv.lastApplyIndex = msg.CommandIndex
		kv.lastApplyTerm = msg.CommandTerm
		kv.lastApplyTime = time.Now()

		// // if byMe {
		// DPrintf("kv%d: data = %v", kv.me, kv.data)
		// // }

		ans := ApplyAnswer{
			Term:  msg.CommandTerm,
			Index: msg.CommandIndex,
			Err:   err,
			Value: value,
		}

		kv.submitAnswer(msg, &ans)
		kv.moreLogsCond.Signal()
		kv.Unlock()

	} else {
		op := msg.OpName
		if op == "install" {
			DPrintf("kv%d: install snapshot. rpcId=%d", kv.me, msg.RpcId)
			data := msg.Command.([]byte)
			wait := msg.WaitChan
			kv.doInstallSnapshot(data)
			wait <- "ok"
			// 这里安装完成了snapshot之后
			// 最好在做一个snapshot. 不然如果这个时候重启的话
			// applyIndex会回滚到之前的状态，而这个状态没有办法接着继续
			kv.doLogCompaction()
		}
	}
}

func (kv *KVServer) applyWorker() {
	for msg := range kv.applyCh {
		kv.applyMessage(&msg)
	}
}

func (kv *KVServer) doInstallSnapshot(data []byte) {
	kv.Lock()
	defer kv.Unlock()
	lastApplyIndex := kv.lastApplyIndex
	kv.decodeSnapshot(data)
	kv.rf.DiscardLogs(kv.lastApplyIndex, kv.lastApplyTerm)
	if kv.lastApplyIndex < lastApplyIndex {
		panic(fmt.Sprintf("kv%d: apply index goes backward %d->%d", kv.me, kv.lastApplyIndex, lastApplyIndex))
	}
	DPrintf("kv%d: apply message. install snapshot. apply index %d -> %d", kv.me, lastApplyIndex, kv.lastApplyIndex)
}

func (kv *KVServer) doLogCompaction() {
	// log compaction 和 install snapshot 过程要对应上
	// 这个过程先对kv加锁，在对rf加锁
	kv.Lock()
	defer kv.Unlock()
	snapshot := kv.encodeSnapshot()
	applyIndex := kv.lastApplyIndex
	// 向前保留几个log可能可以减少同步次数
	kv.rf.LogCompaction(snapshot, applyIndex-10)
}

func (kv *KVServer) encodeSnapshot() []byte {
	w := new(bytes.Buffer)
	e := labgob.NewEncoder(w)
	e.Encode(kv.data)
	e.Encode(kv.dedup)
	e.Encode(kv.lastApplyIndex)
	e.Encode(kv.lastApplyTerm)
	data := w.Bytes()
	return data
}

func (kv *KVServer) decodeSnapshot(data []byte) {
	r := bytes.NewBuffer(data)
	d := labgob.NewDecoder(r)
	d.Decode(&kv.data)
	d.Decode(&kv.dedup)
	d.Decode(&kv.lastApplyIndex)
	d.Decode(&kv.lastApplyTerm)
}

func (kv *KVServer) logCompactionWorker() {
	if kv.maxraftstate == -1 {
		return
	}

	const COMPACTION_RATIO = 4
	const CHECK_INTERVAL = 20
	for {
		if kv.killed() {
			break
		}
		kv.Lock()
		size := kv.persister.RaftStateSize()
		if float64(size) < float64(kv.maxraftstate)*COMPACTION_RATIO {
			kv.moreLogsCond.Wait()
			kv.Unlock()
			continue
		}
		kv.Unlock()
		DPrintf("kv%d: make log compaction, current size = %d, threshold = %d", kv.me, size, kv.maxraftstate)
		kv.doLogCompaction()
		SleepMills(CHECK_INTERVAL)
	}
}

func (kv *KVServer) checkRpcTrace() {
	const MAX_WAIT_TIME = 5000
	for {
		if kv.killed() {
			break
		}
		kv.Lock()
		now := time.Now()
		for k, v := range kv.rpcTrace {
			dur := now.Sub(v)
			if dur.Milliseconds() > MAX_WAIT_TIME {
				DPrintf("kv%d: rpc#%d waits too long. rf.lockAt = %d", kv.me, k, kv.rf.GetLockAt())
			}
		}
		dur := now.Sub(kv.lastApplyTime)
		if dur.Milliseconds() > MAX_WAIT_TIME {
			DPrintf("kv%d: no message committed too long", kv.me)
		}
		kv.Unlock()
		SleepMills(MAX_WAIT_TIME)
	}
}

//
// the tester calls Kill() when a KVServer instance won't
// be needed again. for your convenience, we supply
// code to set rf.dead (without needing a lock),
// and a killed() method to test rf.dead in
// long-running loops. you can also add your own
// code to Kill(). you're not required to do anything
// about this, but it may be convenient (for example)
// to suppress debug output from a Kill()ed instance.
//
func (kv *KVServer) Kill() {
	DPrintf("kv%d: killed.", kv.me)
	atomic.StoreInt32(&kv.dead, 1)
	kv.rf.Kill()
	// Your code here, if desired.
	// 保险起见，在关闭的时候也在做一次snapshot.
	kv.doLogCompaction()
}

func (kv *KVServer) killed() bool {
	z := atomic.LoadInt32(&kv.dead)
	return z == 1
}

//
// servers[] contains the ports of the set of
// servers that will cooperate via Raft to
// form the fault-tolerant key/value service.
// me is the index of the current server in servers[].
// the k/v server should store snapshots through the underlying Raft
// implementation, which should call persister.SaveStateAndSnapshot() to
// atomically save the Raft state along with the snapshot.
// the k/v server should snapshot when Raft's saved state exceeds maxraftstate bytes,
// in order to allow Raft to garbage-collect its log. if maxraftstate is -1,
// you don't need to snapshot.
// StartKVServer() must return quickly, so it should start goroutines
// for any long-running work.oo
//
func StartKVServer(servers []*labrpc.ClientEnd, me int, persister *raft.Persister, maxraftstate int) *KVServer {
	// call labgob.Register on structures you want
	// Go's RPC library to marshall/unmarshall.
	labgob.Register(Op{})

	kv := new(KVServer)
	kv.me = me
	kv.maxraftstate = maxraftstate

	// You may need initialization code here.

	kv.applyCh = make(chan raft.ApplyMsg)
	kv.rf = raft.Make(servers, me, persister, kv.applyCh)
	kv.persister = persister

	// You may need initialization code here.
	kv.data = make(map[string]string)
	kv.dedup = make(map[int32]*OpResult)
	kv.rpcTrace = make(map[int32]time.Time)
	kv.ansBuffer = make(map[int32]chan *ApplyAnswer)
	kv.lastApplyTime = time.Now()
	kv.moreLogsCond = sync.NewCond(&kv.mu)

	kv.decodeSnapshot(persister.ReadSnapshot())
	go kv.applyWorker()
	go kv.checkRpcTrace()
	go kv.logCompactionWorker()
	DPrintf("kv%d: restart.", kv.me)
	return kv
}
