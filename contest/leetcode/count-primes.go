package main
import "fmt"
func countPrimes(n int) int {
	mark := make([]bool, n + 1)
	
	for i:=2; i * i <= n; i += 1 {
		if mark[i] == true {
			continue
		}

		for j:=2 ; i * j <= n; j += 1 {
			mark[i * j]	= true
		}
	}

	res := 0
	for i:=2; i < n; i+=1 {
		if mark[i] == false {
			res += 1
		}
	}
	return res
}

func main() {
	fmt.Println(countPrimes(11))
	fmt.Println(countPrimes(12))
}