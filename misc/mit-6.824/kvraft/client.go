package kvraft

import (
	"crypto/rand"
	"math/big"
	"sync/atomic"

	"../labrpc"
)

type Clerk struct {
	servers []*labrpc.ClientEnd
	// You will have to modify this struct.
	clientId  int32
	requestId int32
	leaderIdx int32
}

var GlobalClientId int32 = 0
var GlobalRpcId int32 = 0

const (
	RetryWaitTime = 200
)

func (ck *Clerk) GetLeaderIdx() int {
	return int(atomic.LoadInt32(&ck.leaderIdx))
}
func (ck *Clerk) SetLeaderIdx(v int) {
	atomic.StoreInt32(&ck.leaderIdx, int32(v))
}

func (ck *Clerk) newRequestId() int32 {
	return atomic.AddInt32(&ck.requestId, 1) - 1
}

func nrand() int64 {
	max := big.NewInt(int64(1) << 62)
	bigx, _ := rand.Int(rand.Reader, max)
	x := bigx.Int64()
	return x
}

func MakeClerk(servers []*labrpc.ClientEnd) *Clerk {
	ck := new(Clerk)
	ck.servers = servers
	// You'll have to add code here.
	ck.clientId = atomic.AddInt32(&GlobalClientId, 1) - 1
	ck.requestId = 0
	idx := int(nrand()) % len(ck.servers)
	ck.SetLeaderIdx(idx)
	return ck
}

//
// fetch the current value for a key.
// returns "" if the key does not exist.
// keeps trying forever in the face of all other errors.
//
// you can send an RPC with code like this:
// ok := ck.servers[i].Call("KVServer.Get", &args, &reply)
//
// the types of args and reply (including whether they are pointers)
// must match the declared types of the RPC handler function's
// arguments. and reply must be passed as a pointer.
//
func (ck *Clerk) Get(key string) string {
	// You will have to modify this function.
	reqId := ck.newRequestId()
	req := GetArgs{
		Key:       key,
		RequestId: reqId,
		ClientId:  ck.clientId,
	}
	idx := ck.GetLeaderIdx()
	name := "KVServer.Get"
	ans := ""
	for {
		reply := GetReply{}
		req.RpcId = atomic.AddInt32(&GlobalRpcId, 1) - 1
		ok := ck.servers[idx].Call(name, &req, &reply)
		DPrintf("ck%d: %s(%v) %s -> %s", ck.clientId, name, ok, &req, &reply)
		if !ok || reply.Err == ErrWrongLeader {
			idx = (idx + 1) % len(ck.servers)
			SleepMills(RetryWaitTime)
		}
		if reply.Err == OK {
			ans = reply.Value
			break
		}
	}
	ck.SetLeaderIdx(idx)
	return ans
}

//
// shared by Put and Append.
//
// you can send an RPC with code like this:
// ok := ck.servers[i].Call("KVServer.PutAppend", &args, &reply)
//
// the types of args and reply (including whether they are pointers)
// must match the declared types of the RPC handler function's
// arguments. and reply must be passed as a pointer.
//
func (ck *Clerk) PutAppend(key string, value string, op string) {
	// You will have to modify this function.
	reqId := ck.newRequestId()
	req := PutAppendArgs{
		Key:       key,
		Value:     value,
		Op:        op,
		RequestId: reqId,
		ClientId:  ck.clientId,
	}
	idx := ck.GetLeaderIdx()
	name := "KVServer.PutAppend"
	for {
		reply := PutAppendReply{}
		req.RpcId = atomic.AddInt32(&GlobalRpcId, 1) - 1
		ok := ck.servers[idx].Call(name, &req, &reply)
		DPrintf("ck%d: %s(%v) %s -> %s", ck.clientId, name, ok, &req, &reply)
		if !ok || reply.Err == ErrWrongLeader {
			idx = (idx + 1) % len(ck.servers)
			SleepMills(RetryWaitTime)
		}
		if reply.Err == OK {
			break
		}
	}
	ck.SetLeaderIdx(idx)
}

func (ck *Clerk) Put(key string, value string) {
	ck.PutAppend(key, value, OpPut)
}
func (ck *Clerk) Append(key string, value string) {
	ck.PutAppend(key, value, OpAppend)
}
