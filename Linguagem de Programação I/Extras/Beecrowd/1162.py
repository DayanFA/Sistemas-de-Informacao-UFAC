def insertion_sort(arr):
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                swaps += 1
                j -= 1
        arr[j+1] = key
    return swaps

N = int(input())

for _ in range(N):
    L = int(input())
    vagao = list(map(int, input().strip().split()))
    swaps = insertion_sort(vagao)
    print(f'Optimal train swapping takes {swaps} swaps.')