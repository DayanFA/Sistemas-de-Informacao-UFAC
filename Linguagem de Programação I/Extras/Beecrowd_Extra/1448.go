package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())
	for i := 1; i <= t; i++ {
		scanner.Scan()
		correct := scanner.Text()

		scanner.Scan()
		team1 := scanner.Text()

		scanner.Scan()
		team2 := scanner.Text()

		score1 := 0
		score2 := 0
		for j := 0; j < len(correct); j++ {
			if correct[j] == team1[j] {
				score1++
			}
			if correct[j] == team2[j] {
				score2++
			}
		}

		fmt.Printf("Instancia %d\n", i)
		if score1 > score2 {
			fmt.Println("time 1")
		} else if score1 < score2 {
			fmt.Println("time 2")
		} else {
			tieBreaker := false
			for j := 0; j < len(correct); j++ {
				if correct[j] == team1[j] && correct[j] != team2[j] {
					fmt.Println("time 1")
					tieBreaker = true
					break
				} else if correct[j] != team1[j] && correct[j] == team2[j] {
					fmt.Println("time 2")
					tieBreaker = true
					break
				}
			}
			if !tieBreaker {
				fmt.Println("empate")
			}
		}
		fmt.Println()
	}
}