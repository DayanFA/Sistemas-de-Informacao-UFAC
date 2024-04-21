package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	times := strings.Fields(input)
	sh, _ := strconv.Atoi(times[0])
	sm, _ := strconv.Atoi(times[1])
	eh, _ := strconv.Atoi(times[2])
	em, _ := strconv.Atoi(times[3])

	st := sh * 60 + sm
	et := eh * 60 + em
	d := et - st
	if d <= 0 {
		d += 24 * 60
	}
	h := d / 60
	m := d % 60
	fmt.Printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m)
}