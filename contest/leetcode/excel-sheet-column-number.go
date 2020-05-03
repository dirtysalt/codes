package main

import "fmt"

func titleToNumber(s string) int {
	var res int = 0
	for _, c := range s {
		res = res * 26  + int(c - 'A') + 1
	}
	return res
}

type Case struct {
	s string
	exp int
}

func main() {
	cases := [] Case{
		{"A" , 1},
		{"AB", 28},
		{"ZY", 701},
	}

	for _, c := range cases {
		out := titleToNumber(c.s)
		if out != c.exp {
			fmt.Printf("FAILED!. s = %v, out = %v, exp = %v\n", c.s, out, c.exp)
		} else {
			fmt.Println("PASSED!")
		}
	}
}