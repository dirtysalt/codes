// coding:utf-8
// Copyright (C) dirlt
package main

import "fmt"

func makeCross(a, b []int) map[int]int {
	c := make(map[int]int)
	for _, v := range a {
		for _, v2 := range b {
			c[v+v2] += 1
		}
	}
	// fmt.Println(c)
	return c
}

func fourSumCount(A []int, B []int, C []int, D []int) int {
	c1 := makeCross(A, B)
	c2 := makeCross(C, D)
	ans := 0
	for k, v := range c1 {
		if v2, ok := c2[-k]; ok {
			ans += v2 * v
		}
	}
	return ans
}

func main() {
	fmt.Println(fourSumCount([]int{1, 2}, []int{-2, -1}, []int{-1, 2}, []int{0, 2}))
}
