package main

import (

)

func divisor(n int) []int {
	divisorSlice := []int{}
	for i := 1; i < n + 1; i ++ {
		if i * i > n {
			break
		}
		if n % i == 0 {
			divisorSlice = append(divisorSlice, i)
			if i * i != n {
				divisorSlice = append(divisorSlice, n / i)
			}
		}
	}
	return divisorSlice
}