// coding:utf-8
// Copyright (C) dirlt
package main

import "fmt"

import "container/heap"

type Item struct {
	value int
	way   int
}
type IntHeap []Item

func (self IntHeap) Len() int {
	return len(self)
}

func (self *IntHeap) Push(x interface{}) {
	*self = append(*self, x.(Item))
}

func (self IntHeap) Less(i, j int) bool {
	return self[i].value < self[j].value
}

func (self IntHeap) Swap(i, j int) {
	self[i], self[j] = self[j], self[i]
}

func (self *IntHeap) Pop() interface{} {
	old := *self
	n := len(old)
	x := old[n-1]
	*self = old[0 : n-1]
	return x
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func nthSuperUglyNumber(n int, primes []int) int {
	todo := &IntHeap{Item{value: 1, way: 0}}
	heap.Init(todo)
	var x Item
	max_value := 0
	for i := 0; i < n; i++ {
		x = heap.Pop(todo).(Item)
		// fmt.Printf("pop = %v\n", x)
		exp := (n - i)
		for idx, c := range primes[x.way:] {
			if todo.Len() > exp && x.value*c > max_value {
				break
			}
			heap.Push(todo, Item{value: x.value * c, way: idx + x.way})
			max_value = max(max_value, x.value*c)
			// fmt.Printf("push = %v\n", x*c)
		}
	}
	return x.value
}

func main() {
	fmt.Println(nthSuperUglyNumber(12, []int{2, 7, 13, 19}))
	fmt.Println(nthSuperUglyNumber(1000, []int{2, 7, 13, 19}))
}
