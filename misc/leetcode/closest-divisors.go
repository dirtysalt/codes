// coding:utf-8
// Copyright (C) dirlt
package main
import "fmt"

func abs(x, y int) int {
	if x > y {
		return x - y
	} else {
		return y - x
	}
}
func closestDivisors(num int) []int {
	x := num
	a, b := 1, x+2
	for i:= 1;i*i <= (x + 2); i++ {
		if (x+1)%i == 0 {
			y := (x+1) / i
			if abs(i, y) < abs(a, b) {			
				a, b = i, y
			}
		}
		if (x + 2) % i == 0 {
			y := (x+2) / i
			if abs(i, y) < abs(a, b) {			
				a, b = i, y
			}
		}
	}
	ans := []int {a, b}
	return ans
}

func main() {
	fmt.Println(closestDivisors(8))
	fmt.Println(closestDivisors(123))
}
