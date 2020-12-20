package main

import "fmt"

func computeArea(A int, B int, C int, D int, E int, F int, G int, H int) int {
	dx := 0
	// A,C,G,E
	if (E >= A && E <= C) {
		if (G <= C) {
			dx = (G-E)
		} else {
			dx = (C-E)
		}
	} else if (G >= A && G <= C) {
		if (E >= A) {
			dx = (G-E)
		} else {
			dx = (G-A)
		}
	} else if (E <= A && G >= C) {
		dx = (C-A)
	}

	dy := 0
	// B,D,F,H
	if (F >= B && F <= D) {
		if (H <= D) {
			dy = (H-F)
		} else {
			dy = (D-F)
		}
	} else if (H >= B && H<=D) {
		// fmt.Printf("F = %v, H = %v, B = %d\n", F, H, B)
		if (F >= B) {
			dy = (H-F)
		} else {
			dy = (H-B)
		}
	} else if (F <= B && H >= D) {
		dy = (D-B)
	}

	// fmt.Printf("dx = %v, dy = %v\n", dx, dy)
	area1 := (C-A) * (D-B)
	area2 := (H-F) * (G-E)
	return area1 + area2 - dx * dy
}

func main() {
	fmt.Println(computeArea(-3, 0,  3, 4, 0,  -1, 9, 2))
	fmt.Println(computeArea(-2,-2,2,2,-3,-3,3,-1))
}