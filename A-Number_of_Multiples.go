package main
import "fmt"

func main() {
	var l, r, d int
	fmt.Scan(&l, &r, &d)
	ans := 0
	for i := l; i < r + 1; i ++ {
		if i % d == 0 {
			ans += 1
		}
	}
	fmt.Println(ans) 
}