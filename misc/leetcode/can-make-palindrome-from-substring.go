// coding:utf-8
// Copyright (C) dirlt

package main

import "fmt"

func canMakePaliQueries(s string, queries [][]int) []bool {
	qn := len(queries)
	ans := make([]bool, qn)
	n := len(s)

	bks := make([]int, n+1)
	bk := 0
	bks[0] = bk
	for i := 0; i < n; i++ {
		bk = bk ^ (1 << int(s[i]-'a'))
		bks[i+1] = bk
	}

	for qi, q := range queries {
		left, right, k := q[0], q[1], q[2]
		lbk := bks[left]
		rbk := bks[right+1]
		v := lbk ^ rbk
		res := 0
		for i := 0; i < 26; i++ {
			if (v & (1 << i)) != 0 {
				res += 1
			}
		}
		ans[qi] = (res/2 <= k)
	}
	return ans
}

func main() {
	res := canMakePaliQueries("abcda", [][]int{{3, 3, 0}, {1, 2, 0}, {0, 3, 1}, {0, 3, 2}, {0, 4, 1}})
	fmt.Printf("res = %v\n", res)
}
