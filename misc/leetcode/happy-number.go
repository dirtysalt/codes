package main

import "fmt"

func nextNumber(n int) int {
	res := 0
	for ; n != 0;  {
		v := n % 10
		n = n / 10
		res += v * v
	}
	return res
}

func isHappy(n int) bool {
	seen := make(map[int]bool)
	for times := 10000; times >= 0; times-- {
		if n == 1 {
			return true
		} else if _, ok := seen[n]; ok {
			return false
		}
		seen[n] = true
		n = nextNumber(n)
	}
	return false
}

type Case struct {
	n   int
	exp bool
}

func main() {
	cases := []Case{
		{19, true},
		{123, false},
	}
	for _, c := range cases {
		out := isHappy(c.n)
		if out != c.exp {
			fmt.Printf("FAILED!\n")
		} else {
			fmt.Println("PASSED!")
		}
	}
}
