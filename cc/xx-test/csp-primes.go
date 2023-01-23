// coding:utf-8
// Copyright (C) dirlt

package main

import "fmt"

func P(left chan int, output chan int, done chan bool) {
	p := <-left
	output <- p

	var right chan int
	var rdone chan bool

	for x := range left {
		if (x % p) == 0 {
			continue
		}
		if right == nil {
			right = make(chan int)
			rdone = make(chan bool)
			go P(right, output, rdone)
		}
		right <- x
	}
	if right != nil {
		close(right)
		<-rdone
	}
	done <- true
}

func collect(output chan int) {
	fmt.Printf("prime numbers: ");
	for p := range output {
		fmt.Printf("%d ", p)
	}
	fmt.Printf("\n");
}

func main() {
	output := make(chan int)
	input := make(chan int)
	done := make(chan bool)
	const N = 10000
	go P(input, output, done)
	go collect(output)
	for i := 2; i < N; i++ {
		input <- i
	}
	close(input)
	<-done
	close(output)
}
