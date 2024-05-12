package main

import (
    "fmt"
    "sort"
)

func main() {
    T := 1
    for {
        var N, Q int
        fmt.Scan(&N, &Q)
        if N == 0 && Q == 0 {
            break
        }

        marmores := make([]int, N)
        for i := 0; i < N; i++ {
            fmt.Scan(&marmores[i])
        }

        sort.Ints(marmores)

        fmt.Printf("CASE# %d:\n", T)
        T++

        for i := 0; i < Q; i++ {
            var consulta int
            fmt.Scan(&consulta)

            index := sort.SearchInts(marmores, consulta)

            if index < N && marmores[index] == consulta {
                fmt.Printf("%d found at %d\n", consulta, index+1)
            } else {
                fmt.Printf("%d not found\n", consulta)
            }
        }
    }
}