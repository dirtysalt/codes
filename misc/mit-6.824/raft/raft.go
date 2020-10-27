package raft

//
// this is an outline of the API that raft must expose to
// the service (or tester). see comments below for
// each of these functions for more details.
//
// rf = Make(...)
//   create a new Raft server.
// rf.Start(command interface{}) (index, term, isleader)
//   start agreement on a new log entry
// rf.GetState() (term, isLeader)
//   ask a Raft for its current term, and whether it thinks it is leader
// ApplyMsg
//   each time a new entry is committed to the log, each Raft peer
//   should send an ApplyMsg to the service (or tester)
//   in the same server.
//

import (
	"bytes"
	"fmt"
	"math/rand"
	"sort"
	"strings"
	"sync"
	"sync/atomic"
	"time"

	"../labgob"
	"../labrpc"
)

// import "bytes"
// import "../labgob"

//
// as each Raft peer becomes aware that successive log entries are
// committed, the peer should send an ApplyMsg to the service (or
// tester) on the same server, via the applyCh passed to Make(). set
// CommandValid to true to indicate that the ApplyMsg contains a newly
// committed log entry.
//
// in Lab 3 you'll want to send other kinds of messages (e.g.,
// snapshots) on the applyCh; at that point you can add fields to
// ApplyMsg, but set CommandValid to false for these other uses.
//
type ApplyMsg struct {
	CommandValid bool
	Command      interface{}
	CommandIndex int
	CommandTerm  int

	// used when commandvalid = false
	WaitChan chan string
	OpName   string
	RpcId    int32
}

func (msg *ApplyMsg) String() string {
	if msg.CommandValid {
		return fmt.Sprintf("ApplyMsg(command=%v, term=%d, index=%d)",
			msg.Command, msg.CommandTerm, msg.CommandIndex)
	} else {
		return fmt.Sprintf("ApplyMsg(opname=%s, rpcId=%d)", msg.OpName, msg.RpcId)
	}
}

type LogEntry struct {
	Command interface{}
	Term    int
}

var GlobalRpcId int32 = 0

const (
	sendHeartbeatInterval       = 200
	loseConnectionTimeout       = sendHeartbeatInterval * 8
	checkHeartbeatInterval      = 50
	electionTimeoutBase         = 300
	electionTimeoutRandom       = 100
	maxNumberLogEntries         = 100
	installSnapshotFailedWait   = 50
	sendAppendEntriesFailedWait = 50
)

func newRpcId() int32 {
	return atomic.AddInt32(&GlobalRpcId, 1)
}

//
// A Go object implementing a single Raft peer.
//
type Raft struct {
	mu         sync.Mutex          // Lock to protect shared access to this peer's state
	peers      []*labrpc.ClientEnd // RPC end points of all peers
	persister  *Persister          // Object to hold this peer's persisted state
	me         int                 // this peer's index into peers[]
	dead       int32               // set by Kill()
	applyCond  *sync.Cond
	commitCond *sync.Cond
	replCond   []*sync.Cond
	leaderCond *sync.Cond
	markhb     []bool      // 标记是否有hearbeat需要发送
	followerhb []time.Time // 每个follower最新同步的时间
	applyCh    chan ApplyMsg

	// Your data here (2A, 2B, 2C).
	// Look at the paper's Figure 2 for a description of what
	// state a Raft server must maintain.
	isLeader     bool
	leaderId     int
	lasthb       time.Time // election timer
	lasthbLeader time.Time // 用于快速否定request vote
	logs         []*LogEntry
	currentTerm  int // last term server has ever seen
	votedFor     int // candidate voted in current term
	commitIndex  int
	lastApplied  int
	baseLogIndex int
	lastLogIndex int
	nextIndex    []int
	matchIndex   []int
	lockAt       int32
}

func (rf *Raft) Lock(at int32) {
	rf.SetLockAt(at)
	rf.mu.Lock()
}
func (rf *Raft) GetLockAt() int32 {
	return atomic.LoadInt32(&rf.lockAt)
}
func (rf *Raft) SetLockAt(at int32) {
	atomic.StoreInt32(&rf.lockAt, at)
}
func (rf *Raft) Unlock() {
	rf.mu.Unlock()
	rf.SetLockAt(-1)
}

// return currentTerm and whether this server
// believes it is the leader.
func (rf *Raft) GetState() (int, bool) {

	var term int
	var isLeader bool
	// Your code here (2A).

	rf.Lock(136)
	defer rf.Unlock()

	term = rf.currentTerm
	isLeader = rf.isLeader

	return term, isLeader
}

//
// save Raft's persistent state to stable storage,
// where it can later be retrieved after a crash and restart.
// see paper's Figure 2 for a description of what should be persistent.
//

func (rf *Raft) encodeState() []byte {
	w := new(bytes.Buffer)
	e := labgob.NewEncoder(w)
	e.Encode(rf.votedFor)
	e.Encode(rf.currentTerm)
	e.Encode(rf.logs)
	e.Encode(rf.lastLogIndex)
	e.Encode(rf.baseLogIndex)
	data := w.Bytes()
	return data
}

func (rf *Raft) persist() {
	// Your code here (2C).
	// Example:
	// w := new(bytes.Buffer)
	// e := labgob.NewEncoder(w)
	// e.Encode(rf.xxx)
	// e.Encode(rf.yyy)
	// data := w.Bytes()
	// rf.persister.SaveRaftState(data)

	// disable persist first.
	if true {
		data := rf.encodeState()
		rf.persister.SaveRaftState(data)
	}
}

//
// restore previously persisted state.
//
func (rf *Raft) readPersist(data []byte) {
	if data == nil || len(data) < 1 { // bootstrap without any state?
		return
	}
	// Your code here (2C).
	// Example:
	// r := bytes.NewBuffer(data)
	// d := labgob.NewDecoder(r)
	// var xxx
	// var yyy
	// if d.Decode(&xxx) != nil ||
	//    d.Decode(&yyy) != nil {
	//   error...
	// } else {
	//   rf.xxx = xxx
	//   rf.yyy = yyy
	// }

	r := bytes.NewBuffer(data)
	d := labgob.NewDecoder(r)
	d.Decode(&rf.votedFor)
	d.Decode(&rf.currentTerm)
	d.Decode(&rf.logs)
	d.Decode(&rf.lastLogIndex)
	d.Decode(&rf.baseLogIndex)
	rf.commitIndex = rf.baseLogIndex
	rf.lastApplied = rf.baseLogIndex
}

func (rf *Raft) LogCompaction(snapshot []byte, applyIndex int) {
	rf.Lock(211)
	defer rf.Unlock()
	rf.dumpLogs("LogCompaction.Before")
	discard := max(applyIndex-rf.baseLogIndex, 0)
	rf.logs = rf.logs[discard:]
	rf.baseLogIndex += discard
	DPrintf("X%d: log compaction. applyIndex=%d, rf.lastApplied=%d, rf.commitIndex=%d, baseIndex=%d",
		applyIndex, rf.me, rf.lastApplied, rf.commitIndex, rf.baseLogIndex)
	state := rf.encodeState()
	rf.persister.SaveStateAndSnapshot(state, snapshot)
	rf.dumpLogs("LogCompaction.After")
}

//
// example RequestVote RPC arguments structure.
// field names must start with capital letters!
//
type RequestVoteArgs struct {
	// Your data here (2A, 2B).
	Term         int
	CandidateId  int
	LastLogIndex int
	LastLogTerm  int
	RpcId        int32
}

func (args *RequestVoteArgs) String() string {
	return fmt.Sprintf("req(term=%d, candId=%d, logIndex=%d, logTerm=%d, rpcId=%d)",
		args.Term, args.CandidateId, args.LastLogIndex, args.LastLogTerm, args.RpcId)
}

//
// example RequestVote RPC reply structure.
// field names must start with capital letters!
//
type RequestVoteReply struct {
	// Your data here (2A).
	Term        int
	VoteGranted bool
}

func (reply *RequestVoteReply) String() string {
	return fmt.Sprintf("reply(term=%d, vote=%v)", reply.Term, reply.VoteGranted)
}

func (rf *Raft) lastLogEntry() *LogEntry {
	// sz := len(rf.logs)
	// return &rf.logs[sz-1]
	return rf.getLogEntry(rf.lastLogIndex)
}

func (rf *Raft) lastLogTerm() (term int) {
	log := rf.lastLogEntry()
	return log.Term
}

func (rf *Raft) getLogEntry(index int) *LogEntry {
	log := rf.logs[index-rf.baseLogIndex]
	return log
}

func (rf *Raft) DiscardLogs(index int, term int) {
	rf.Lock(269)
	defer rf.Unlock()
	DPrintf("X%d: discard logs. set logs index = %d, lastIndex = %d, baseIndex = %d", rf.me, index, rf.lastLogIndex, rf.baseLogIndex)
	if index <= rf.lastLogIndex {
		idx := index - rf.baseLogIndex
		rf.logs = rf.logs[idx:]
	} else {
		rf.logs = []*LogEntry{
			{Command: nil, Term: term},
		}
	}
	rf.lastLogIndex = index + len(rf.logs) - 1
	rf.baseLogIndex = index
	rf.lastApplied = index
	rf.commitIndex = index
}

var DEBUG_DUMP_LOGS = 0

func (rf *Raft) dumpLogs(where string) {
	if DEBUG_DUMP_LOGS == 0 {
		return
	}

	output := strings.Builder{}
	index := rf.baseLogIndex
	output.WriteString("[")
	for i := 0; i < len(rf.logs); i++ {
		output.WriteString(fmt.Sprintf("%d:%d ", index, rf.logs[i].Term))
		index += 1
	}
	output.WriteString("]")
	msg := output.String()
	DPrintf("X%d: [LOGS] where=%s, baseIndex=%d, lastIndex=%d. %s", rf.me, where, rf.baseLogIndex, rf.lastLogIndex, msg)
}

func (rf *Raft) changeToFollower(term int, reason string) {
	DPrintf("X%d: change to follower. new term = %d, reason = %s", rf.me, term, reason)
	rf.isLeader = false
	rf.votedFor = -1
	rf.currentTerm = term
	rf.leaderId = -1
}

//
// example RequestVote RPC handler.
//
func (rf *Raft) RequestVote(args *RequestVoteArgs, reply *RequestVoteReply) {
	// Your code here (2A, 2B).
	rf.Lock(310)
	defer rf.Unlock()
	trace := strings.Builder{}
	defer func() {
		DPrintf("X%d: RequestVote: %v --> %v %s ", rf.me, args, reply, trace.String())
	}()

	reply.Term = rf.currentTerm
	reply.VoteGranted = false

	now := time.Now()
	off := now.Sub(rf.lasthbLeader)
	// disregard vote if you think a leader exists.
	if off.Milliseconds() < sendHeartbeatInterval {
		trace.WriteString("[ignore for heartheat]")
		return
	}

	if args.Term < rf.currentTerm {
		trace.WriteString("[ignore lower term]")
		return
	}
	if args.Term > rf.currentTerm {
		trace.WriteString("[update higher term]")
		rf.changeToFollower(args.Term, "RequestVote")
	}
	if rf.votedFor == -1 {
		lastTerm := rf.lastLogTerm()
		if (args.LastLogTerm > lastTerm) || (args.LastLogTerm == lastTerm && args.LastLogIndex >= rf.lastLogIndex) {
			rf.votedFor = args.CandidateId
		}
		trace.WriteString(fmt.Sprintf("[req(t=%d,i=%d), me(t=%d,i=%d)]", args.LastLogTerm, args.LastLogIndex, lastTerm, rf.lastLogIndex))
	}
	if rf.votedFor == args.CandidateId {
		reply.VoteGranted = true
	}
	if reply.VoteGranted {
		trace.WriteString(fmt.Sprintf("[voted for %d]", args.CandidateId))
	}
	rf.persist()
}

type AppendEntriesRequest struct {
	Term              int
	LeaderId          int
	PrevLogIndex      int
	PrevLogTerm       int
	Entries           []*LogEntry
	LeaderCommitIndex int
	RpcId             int32
}

func (req *AppendEntriesRequest) String() string {
	return fmt.Sprintf("req(term=%d, leaderId=%d, prevIndex=%d, prevTerm=%d, leaderCommitIndex=%d, rpcId=%d)",
		req.Term, req.LeaderId, req.PrevLogIndex, req.PrevLogTerm, req.LeaderCommitIndex, req.RpcId)
}

type AppendEntriesReply struct {
	Term      int
	Success   bool
	Conflict  bool
	SyncIndex int
}

func (x *AppendEntriesReply) String() string {
	return fmt.Sprintf("reply(term=%d, ok=%v, conflict=%v, si=%d)",
		x.Term, x.Success, x.Conflict, x.SyncIndex)
}

func (rf *Raft) AppendEntries(req *AppendEntriesRequest, reply *AppendEntriesReply) {
	rf.Lock(379)
	defer rf.Unlock()
	reply.Success = false
	reply.Term = rf.currentTerm
	reply.Conflict = false
	trace := strings.Builder{}

	defer func() {
		DPrintf("X%d: AppendEntries:%v -> %v %s", rf.me, req, reply, trace.String())
	}()

	if req.Term < rf.currentTerm {
		trace.WriteString("[ignore lower term]")
		return
	}

	now := time.Now()
	rf.lasthb = now
	rf.lasthbLeader = now

	if req.Term > rf.currentTerm {
		trace.WriteString("[update higher term]")
		rf.changeToFollower(req.Term, "AppendEntries")
	}
	rf.leaderId = req.LeaderId

	idx := req.PrevLogIndex - rf.baseLogIndex
	conflict := true
	// 因为logcompaction会造成idx < 0
	if idx < 0 || idx >= len(rf.logs) {
		DPrintf("X%d: mismatch log entry size. prevIndex=%d, baseIndex=%d, lastIndex=%d",
			rf.me, req.PrevLogIndex, rf.baseLogIndex, rf.lastLogIndex)
		idx = len(rf.logs) - 1
	} else if idx >= 0 && rf.logs[idx].Term != req.PrevLogTerm {
		fastRollback := true

		DPrintf("X%d: mismatch log entry. index = %v, leader term = %v, my term = %v",
			rf.me, req.PrevLogIndex, req.PrevLogTerm, rf.logs[idx].Term)
		if fastRollback {

			// 下面这个逻辑是正常的
			// 实验中遇到了这样的情况
			// x0 351(16)
			// x1 351(16)
			// x2 351(16)
			// x3 351(16) 352(16) 353(16)
			// x4 351(16) 352(16) 353(16)
			// 在351这里commit. 之后x0,x1,x2组成一个group, 并且在x0后面增加了一个352(17)
			// x0 logs: 351(16) 352(17)
			// 之后x1,x2,x3,x4组成group, 并且同步了logs: 351(16) 352(16) 353(16)
			// 最后x0重新加入，这个时候需要覆盖351. 正确的term是16，而x0上是17

			// if rf.logs[idx].Term > req.PrevLogTerm {
			// 	panic(fmt.Sprintf("X%d: conflict term assert error: %d, %d", rf.me, rf.logs[idx].Term, req.PrevLogTerm))
			// }

			searchTerm := rf.logs[idx].Term
			rb := 0
			for idx >= 0 && rf.logs[idx].Term == searchTerm && (idx+rf.baseLogIndex) > rf.commitIndex {
				idx -= 1
				rb += 1
			}
			DPrintf("X%d: rollback %d entries", rf.me, rb)
		} else {
			idx -= 1
		}
		if idx < 0 {
			rf.dumpLogs("AppendEntries.Fatal")
			panic(fmt.Sprintf("X%d: can not find sync index", rf.me))
		}
	} else {
		conflict = false
	}

	if conflict {
		reply.SyncIndex = idx + rf.baseLogIndex
		reply.Conflict = true
		return
	}

	idx += 1
	if len(req.Entries) != 0 {
		DPrintf("X%d: append logs at [%d,%d]", rf.me, idx, idx+len(req.Entries)-1)
		// TODO: append logs
		for i := 0; i < len(req.Entries); i++ {
			if len(rf.logs) == idx {
				rf.logs = append(rf.logs, req.Entries[i])
			} else {
				rf.logs[idx] = req.Entries[i]
			}
			idx += 1
		}
	}
	rf.logs = rf.logs[:idx]
	rf.lastLogIndex = idx - 1 + rf.baseLogIndex
	rf.dumpLogs("AppendEntries")

	// 这里更新commitIndex前提是logs已经完全一致了
	if req.LeaderCommitIndex > rf.commitIndex {
		trace.WriteString("[update commit index]")
		prevCommitIndex := rf.commitIndex
		rf.commitIndex = min(req.LeaderCommitIndex, rf.lastLogIndex)
		DPrintf("X%d: update commit index %d->%d. lastLogIndex=%d", rf.me, prevCommitIndex, rf.commitIndex, rf.lastLogIndex)
		rf.applyCond.Signal()
	}

	rf.checkLogsSize()
	reply.Success = true
	rf.persist()
	return
}

type InstallSnapshotRequest struct {
	Term     int
	LeaderId int
	Snapshot []byte
	RpcId    int32
}
type InstallSnapshotReply struct {
	Term    int
	Success bool
}

func (req *InstallSnapshotRequest) String() string {
	return fmt.Sprintf("req(term=%d, leaderId=%d, rpcId=%d)", req.Term, req.LeaderId, req.RpcId)
}

func (reply *InstallSnapshotReply) String() string {
	return fmt.Sprintf("reply(term=%d, ok=%v)", reply.Term, reply.Success)
}

func (rf *Raft) InstallSnapshot(req *InstallSnapshotRequest, reply *InstallSnapshotReply) {
	rf.Lock(494)
	defer func() {
		DPrintf("X%d: InstallSnapshot:%v -> %s", rf.me, req, reply)
	}()

	reply.Success = false
	reply.Term = rf.currentTerm

	if req.Term < rf.currentTerm {
		rf.Unlock()
		return
	}
	rf.leaderId = req.LeaderId
	rf.Unlock()

	// TODO: 这里同步等待返回如何
	reply.Success = true
	wait := make(chan string)
	msg := ApplyMsg{
		CommandValid: false,
		OpName:       "install",
		Command:      req.Snapshot,
		WaitChan:     wait,
		RpcId:        req.RpcId,
	}
	rf.applyCh <- msg
	<-wait
}

type HeartbeatRequest struct {
	Term     int
	LeaderId int
	RpcId    int32
}

func (req *HeartbeatRequest) String() string {
	return fmt.Sprintf("req(term=%d, leaderId=%d, rpcId=%d)",
		req.Term, req.LeaderId, req.RpcId)
}

type HeartbeatReply struct {
	Term    int
	Success bool
}

func (x *HeartbeatReply) String() string {
	return fmt.Sprintf("reply(term=%d, ok=%v)", x.Term, x.Success)
}

func (rf *Raft) Heartbeat(req *HeartbeatRequest, reply *HeartbeatReply) {
	rf.Lock(419)
	defer rf.Unlock()
	reply.Success = false
	reply.Term = rf.currentTerm
	trace := strings.Builder{}

	// defer func() {
	// 	DPrintf("X%d: Heartbeat:%v -> %v %s", rf.me, req, reply, trace.String())
	// }()

	if req.Term < rf.currentTerm {
		trace.WriteString("[ignore lower term]")
		return
	}

	now := time.Now()
	rf.lasthb = now
	rf.lasthbLeader = now

	if req.Term > rf.currentTerm {
		trace.WriteString("[update higher term]")
		rf.changeToFollower(req.Term, "Heartbeat")
	}
	rf.leaderId = req.LeaderId
	reply.Success = true
}

//
// example code to send a RequestVote RPC to a server.
// server is the index of the target server in rf.peers[].
// expects RPC arguments in args.
// fills in *reply with RPC reply, so caller should
// pass &reply.
// the types of the args and reply passed to Call() must be
// the same as the types of the arguments declared in the
// handler function (including whether they are pointers).
//
// The labrpc package simulates a lossy network, in which servers
// may be unreachable, and in which requests and replies may be lost.
// Call() sends a request and waits for a reply. If a reply arrives
// within a timeout interval, Call() returns true; otherwise
// Call() returns false. Thus Call() may not return for a while.
// A false return can be caused by a dead server, a live server that
// can't be reached, a lost request, or a lost reply.
//
// Call() is guaranteed to return (perhaps after a delay) *except* if the
// handler function on the server side does not return.  Thus there
// is no need to implement your own timeouts around Call().
//
// look at the comments in ../labrpc/labrpc.go for more details.
//
// if you're having trouble getting RPC to work, check that you've
// capitalized all field names in structs passed over RPC, and
// that the caller passes the address of the reply struct with &, not
// the struct itself.
//
func (rf *Raft) sendRequestVote(server int, args *RequestVoteArgs, reply *RequestVoteReply) bool {
	ok := rf.peers[server].Call("Raft.RequestVote", args, reply)
	return ok
}

func (rf *Raft) sendAppendEntries(server int, args *AppendEntriesRequest, reply *AppendEntriesReply) bool {
	ok := rf.peers[server].Call("Raft.AppendEntries", args, reply)
	return ok
}

func (rf *Raft) sendInstallSnapshot(server int, args *InstallSnapshotRequest, reply *InstallSnapshotReply) bool {
	ok := rf.peers[server].Call("Raft.InstallSnapshot", args, reply)
	return ok
}

func (rf *Raft) sendHeartbeat(server int, args *HeartbeatRequest, reply *HeartbeatReply) bool {
	ok := rf.peers[server].Call("Raft.Heartbeat", args, reply)
	return ok
}

func (rf *Raft) signalRepl() {
	for i := 0; i < len(rf.peers); i++ {
		rf.replCond[i].Signal()
	}
}

func (rf *Raft) checkLogsSize() {
	sz := rf.baseLogIndex + len(rf.logs)
	if sz != (rf.lastLogIndex + 1) {
		msg := fmt.Sprintf("X%d: logs size(%d) mismatch with last log index(%d)", rf.me, sz, rf.lastLogIndex)
		panic(msg)
	}
	if rf.commitIndex > rf.lastLogIndex {
		msg := fmt.Sprintf("X%d: erase commited logs. commit-index = %d, lastLogIndex = %d", rf.me, rf.commitIndex, rf.lastLogIndex)
		panic(msg)
	}
	if rf.lastApplied > rf.commitIndex {
		msg := fmt.Sprintf("X%d: applied > commited logs. applied-index = %d, commit-index = %d", rf.me, rf.lastApplied, rf.commitIndex)
		panic(msg)
	}
}

//
// the service using Raft (e.g. a k/v server) wants to start
// agreement on the next command to be appended to Raft's log. if this
// server isn't the leader, returns false. otherwise start the
// agreement and return immediately. there is no guarantee that this
// command will ever be committed to the Raft log, since the leader
// may fail or lose an election. even if the Raft instance has been killed,
// this function should return gracefully.
//
// the first return value is the index that the command will appear at
// if it's ever committed. the second return value is the current
// term. the third return value is true if this server believes it is
// the leader.
//
func (rf *Raft) Start(command interface{}) (int, int, bool) {
	index := -1
	term := -1
	isLeader := true

	// Your code here (2B).
	rf.Lock(604)
	defer rf.Unlock()

	isLeader = rf.isLeader
	if isLeader {
		rf.lastLogIndex = rf.lastLogIndex + 1
		index = rf.lastLogIndex
		term = rf.currentTerm
		log := LogEntry{
			Command: command,
			Term:    term,
		}
		rf.logs = append(rf.logs, &log)
		rf.dumpLogs("Start")
		rf.checkLogsSize()
		rf.nextIndex[rf.me] = index + 1
		rf.matchIndex[rf.me] = index
		DPrintf("X%d: next[X%d]=%d, match[X%d]=%d", rf.me, rf.me, rf.nextIndex[rf.me], rf.me, rf.matchIndex[rf.me])
		rf.signalRepl()
		rf.persist()
		DPrintf("X%d: Start command. index = %d, term = %d", rf.me, index, term)
	}

	return index, term, isLeader
}

//
// the tester doesn't halt goroutines created by Raft after each test,
// but it does call the Kill() method. your code can use killed() to
// check whether Kill() has been called. the use of atomic avoids the
// need for a lock.
//
// the issue is that long-running goroutines use memory and may chew
// up CPU time, perhaps causing later tests to fail and generating
// confusing debug output. any goroutine with a long-running loop
// should call killed() to check whether it should stop.
//

func (rf *Raft) Kill() {
	DPrintf("X%d: killed.", rf.me)
	atomic.StoreInt32(&rf.dead, 1)
	rf.applyCond.Broadcast()
	rf.commitCond.Broadcast()
	// Your code here, if desired.
}

func (rf *Raft) killed() bool {
	z := atomic.LoadInt32(&rf.dead)
	return z == 1
}

func sleepMills(v int) {
	time.Sleep(time.Duration(v) * time.Millisecond)
}

func (rf *Raft) keepHeartbeatWorker(peer int) {
	if rf.me == peer {
		return
	}

	for {
		if rf.killed() {
			break
		}
		rf.Lock(743)
		if !rf.isLeader {
			rf.leaderCond.Wait()
			rf.Unlock()
			continue
		}
		now := time.Now()
		off := now.Sub(rf.followerhb[peer])
		if off.Milliseconds() > sendHeartbeatInterval {
			rpcId := newRpcId()
			req := HeartbeatRequest{
				Term:     rf.currentTerm,
				LeaderId: rf.me,
				RpcId:    rpcId,
			}
			reply := HeartbeatReply{}
			rf.Unlock()

			if !rf.sendHeartbeat(peer, &req, &reply) {
				sleepMills(checkHeartbeatInterval)
				continue
			}

			rf.Lock(794)
			now := time.Now()
			rf.followerhb[peer] = now
			if reply.Term > rf.currentTerm {
				rf.changeToFollower(reply.Term, "runHeartbeatWorker")
			}
			rf.Unlock()
		} else {
			rf.Unlock()
			sleepMills(checkHeartbeatInterval)
		}
	}
}

func (rf *Raft) markHeartbeat() {
	now := time.Now()
	rf.lasthb = now
	rf.followerhb[rf.me] = now
	for i := 0; i < len(rf.peers); i++ {
		rf.markhb[i] = true
	}
	rf.signalRepl()
}

func (rf *Raft) keepHeartbeat() {
	for {
		if rf.killed() {
			break
		}

		rf.Lock(825)
		if rf.isLeader {
			rf.markHeartbeat()
		}
		rf.Unlock()
		sleepMills(sendHeartbeatInterval)
	}
}

func (rf *Raft) checkHeartbeat() {
	rf.electLeader()
	for {
		if rf.killed() {
			break
		}

		do := false
		now := time.Now()
		rf.Lock(713)
		off := now.Sub(rf.lasthb)
		if off.Milliseconds() > (int64(electionTimeoutBase) + (rand.Int63() % electionTimeoutRandom)) {
			do = true
		}
		if !do && rf.isLeader {
			// 如果是leader的话，需要判断多少个followe已经超时

			cnt := 0
			for i := 0; i < len(rf.peers); i++ {
				off = now.Sub(rf.followerhb[i])
				if off.Milliseconds() > loseConnectionTimeout {
					cnt += 1
				}
			}

			if cnt > len(rf.peers)/2 {
				sb := strings.Builder{}
				for i := 0; i < len(rf.peers); i++ {
					sb.WriteString(fmt.Sprintf("X%d:%d ms ", i, off.Milliseconds()))
				}
				DPrintf("X%d: leader lose connection to majority. hb: %s", rf.me, sb.String())
				do = true
			}
		}
		rf.Unlock()

		if !do {
			sleepMills(checkHeartbeatInterval)
			continue
		}
		if rf.killed() {
			break
		}
		rf.electLeader()
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func (rf *Raft) changeToLeader() {
	rf.Lock(768)
	defer rf.Unlock()

	rf.isLeader = true
	DPrintf("X%d: change to leader. new term = %d", rf.me, rf.currentTerm)
	now := time.Now()
	for i := 0; i < len(rf.peers); i++ {
		rf.nextIndex[i] = rf.lastLogIndex + 1
		rf.matchIndex[i] = 0
		rf.followerhb[i] = now
	}
	rf.markHeartbeat()
	rf.leaderCond.Broadcast()
}

func (rf *Raft) okToRepl(peer int) bool {
	if !rf.isLeader {
		return false
	}
	if rf.markhb[peer] {
		return true
	}
	if rf.nextIndex[peer] > rf.lastLogIndex {
		return false
	}
	return true
}

func (rf *Raft) checkReplProgress(peer int) {
	if rf.me == peer {
		return
	}

	ok := false // 记录上次是否成功
	for {
		if rf.killed() {
			break
		}
		rf.Lock(802)
		if !rf.okToRepl(peer) {
			rf.SetLockAt(-1)
			rf.replCond[peer].Wait()
			rf.Unlock()
			continue
		}

		rf.markhb[peer] = false
		prevIndex := rf.nextIndex[peer] - 1
		lastIndex := rf.lastLogIndex

		// 如果leader没有办法提供日志的话
		// 那么需要发送snapshot.
		if prevIndex < rf.baseLogIndex {
			rpcId := newRpcId()
			DPrintf("X%d: can not send logs to X%d. rpcId=%d, prevIndex=%d, baseIndex=%d. install snapshot", rf.me, peer, rpcId, prevIndex, rf.baseLogIndex)
			ok = false
			req := InstallSnapshotRequest{
				Term:     rf.currentTerm,
				LeaderId: rf.me,
				RpcId:    rpcId,
			}
			reply := InstallSnapshotReply{}
			rf.Unlock()
			req.Snapshot = rf.persister.ReadSnapshot()

			if !rf.sendInstallSnapshot(peer, &req, &reply) {
				DPrintf("X%d: install snapshot rpcId=%d failed", rf.me, rpcId)
				sleepMills(installSnapshotFailedWait)
				continue
			}

			rf.Lock(828)
			if !reply.Success {
				if reply.Term > rf.currentTerm {
					rf.changeToFollower(reply.Term, "installSnapshot")
				}
			} else {
				// 这可以随便设置一个点，等待下次同步
				rf.nextIndex[peer] = lastIndex + 1
			}
			rf.Unlock()
			continue
		}

		prevLog := rf.getLogEntry(prevIndex)
		// 如果之前失败的话，那么首先发送一个空log去同步
		if !ok {
			lastIndex = prevIndex
		}

		// 控制单次最多发送的数量
		if lastIndex-prevIndex > maxNumberLogEntries {
			lastIndex = prevIndex + maxNumberLogEntries
		}

		rpcId := newRpcId()
		req := AppendEntriesRequest{
			Term:              rf.currentTerm,
			LeaderId:          rf.me,
			PrevLogIndex:      prevIndex,
			PrevLogTerm:       prevLog.Term,
			LeaderCommitIndex: rf.commitIndex,
			Entries:           rf.logs[prevIndex+1-rf.baseLogIndex : lastIndex+1-rf.baseLogIndex],
			RpcId:             rpcId,
		}

		reply := AppendEntriesReply{}
		rf.Unlock()

		sz := len(req.Entries)
		DPrintf("X%d: sendAppendEntries to X%d: %v. lastIndex=%d, sz=%d", rf.me, peer, &req, lastIndex, sz)

		// 本次发送失败，可能是follower不可达
		if !rf.sendAppendEntries(peer, &req, &reply) {
			DPrintf("X%d: send append entries rpcId=%d faied", rf.me, rpcId)
			sleepMills(sendAppendEntriesFailedWait)
			continue
		}

		rf.Lock(872)
		now := time.Now()
		rf.followerhb[peer] = now
		if !reply.Success {
			if reply.Term > rf.currentTerm {
				rf.changeToFollower(reply.Term, "checkReplProgress")
			}
			if reply.Conflict {
				// term confliction
				rf.nextIndex[peer] = reply.SyncIndex + 1
			}
			ok = false
		} else {
			// accept logs[prevIndex+1:lastIndex+1]
			changed := (rf.matchIndex[peer] != lastIndex)
			rf.nextIndex[peer] = lastIndex + 1
			rf.matchIndex[peer] = lastIndex
			if changed {
				DPrintf("X%d: next[X%d]=%d, match[X%d]=%d", rf.me, peer, rf.nextIndex[peer], peer, rf.matchIndex[peer])
			}
			rf.commitCond.Signal()
			ok = true
		}

		rf.Unlock()

	}
}

func (rf *Raft) checkApplyProgress() {
	for {
		if rf.killed() {
			break
		}
		rf.Lock(906)
		// DPrintf("X%d: commit-index = %d, last-applied = %d", rf.me, rf.commitIndex, rf.lastApplied)
		if rf.commitIndex <= rf.lastApplied {
			rf.SetLockAt(-1)
			rf.applyCond.Wait()
			rf.Unlock()

		} else {
			DPrintf("X%d: commit logs at [%d,%d]. baseIndex = %d", rf.me, rf.lastApplied+1, rf.commitIndex, rf.baseLogIndex)
			msgs := []*ApplyMsg{}

			for i := rf.lastApplied + 1; i <= rf.commitIndex; i++ {
				log := rf.getLogEntry(i)
				msg := ApplyMsg{
					CommandValid: true,
					Command:      log.Command,
					CommandIndex: i,
					CommandTerm:  log.Term,
				}
				msgs = append(msgs, &msg)
			}

			isLeader := rf.isLeader
			rf.lastApplied = rf.commitIndex
			rf.Unlock()

			for i := 0; i < len(msgs); i++ {
				msg := msgs[i]
				rf.applyCh <- *msg
				DPrintf("X%d: commit msg = %v", rf.me, msg)
				if isLeader {
					DPrintf("X%d: Leader Commit. index = %d, msg = %v", rf.me, i, msg)
				}
			}
		}
	}
}

func (rf *Raft) maxReplicateIndex() int {
	match := make([]int, len(rf.peers))
	for i := 0; i < len(rf.peers); i++ {
		match[i] = rf.matchIndex[i]
	}
	sort.Ints(match)
	// DPrintf("X%d: match index = %v(%v)", rf.me, match, rf.matchIndex)
	return match[len(rf.peers)/2]
}

func (rf *Raft) checkCommitProgress() {
	for {
		if rf.killed() {
			break
		}
		rf.Lock(948)
		maxReplIndex := rf.maxReplicateIndex()
		// DPrintf("X%d: max-repl-index = %d, commit-index = %d", rf.me, maxReplIndex, rf.commitIndex)
		if maxReplIndex <= rf.commitIndex {
			rf.SetLockAt(-1)
			rf.commitCond.Wait()
		} else {
			rf.commitIndex = maxReplIndex
			rf.applyCond.Signal()
		}
		rf.Unlock()
	}
}

func (rf *Raft) electLeader() {
	req := RequestVoteArgs{}

	rf.Lock(965)
	rf.changeToFollower(rf.currentTerm+1, "electLeader")
	// reset election timer
	rf.lasthb = time.Now()

	req.Term = rf.currentTerm
	req.CandidateId = rf.me
	req.LastLogIndex = rf.lastLogIndex
	req.LastLogTerm = rf.lastLogTerm()
	req.RpcId = newRpcId()
	rf.Unlock()

	DPrintf("X%d: electLeader ...", rf.me)
	votes := int32(0)
	for i := 0; i < len(rf.peers); i++ {
		go func(peer int) {
			reply := RequestVoteReply{}
			DPrintf("X%d: sendRequestVote to X%d: %v", rf.me, peer, &req)
			if rf.sendRequestVote(peer, &req, &reply) {
				valid := true
				rf.Lock(984)
				// 如果修改了currentTerm的话，那么认为这轮就失败了
				// 因为这里投票其实是投给req.Term
				// 如果这里直接更新了currentTerm的话，那么就会出现两个leader.
				if reply.Term > rf.currentTerm {
					rf.changeToFollower(reply.Term, "electLeaderResponse")
				}
				if req.Term != rf.currentTerm {
					valid = false
				}
				rf.Unlock()

				// get majority votes
				if valid && reply.VoteGranted {
					v := atomic.AddInt32(&votes, 1)
					if int(v) == (len(rf.peers)/2 + 1) {
						rf.changeToLeader()
					}
				}
			}
		}(i)
	}
}

//
// the service or tester wants to create a Raft server. the ports
// of all the Raft servers (including this one) are in peers[]. this
// server's port is peers[me]. all the servers' peers[] arrays
// have the same order. persister is a place for this server to
// save its persistent state, and also initially holds the most
// recent saved state, if any. applyCh is a channel on which the
// tester or service expects Raft to send ApplyMsg messages.
// Make() must return quickly, so it should start goroutines
// for any long-running work.
//
func Make(peers []*labrpc.ClientEnd, me int,
	persister *Persister, applyCh chan ApplyMsg) *Raft {
	rf := &Raft{}
	rf.peers = peers
	rf.persister = persister
	rf.me = me
	rf.applyCond = sync.NewCond(&rf.mu)
	rf.applyCh = applyCh
	rf.commitCond = sync.NewCond(&rf.mu)
	rf.leaderCond = sync.NewCond(&rf.mu)
	rf.replCond = make([]*sync.Cond, len(rf.peers))
	rf.markhb = make([]bool, len(rf.peers))
	rf.followerhb = make([]time.Time, len(rf.peers))
	now := time.Now()
	for i := 0; i < len(rf.peers); i++ {
		rf.replCond[i] = sync.NewCond(&rf.mu)
		rf.followerhb[i] = now
	}

	// Your initialization code here (2A, 2B, 2C).
	rf.logs = []*LogEntry{
		{
			Command: nil,
			Term:    0,
		},
	}
	rf.baseLogIndex = 0
	rf.lastLogIndex = 0
	rf.currentTerm = 0
	rf.votedFor = -1
	rf.isLeader = false
	rf.commitIndex = 0
	rf.lastApplied = 0
	rf.nextIndex = make([]int, len(peers))
	rf.matchIndex = make([]int, len(peers))

	// initialize from state persisted before a crash
	rf.readPersist(persister.ReadRaftState())

	go rf.checkHeartbeat()
	go rf.keepHeartbeat()
	go rf.checkApplyProgress()
	go rf.checkCommitProgress()
	for i := 0; i < len(rf.peers); i++ {
		go rf.checkReplProgress(i)
		go rf.keepHeartbeatWorker(i)
	}

	DPrintf("X%d: restart.", rf.me)
	return rf
}
