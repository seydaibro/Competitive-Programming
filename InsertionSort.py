def insertionSort1(n, arr):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while(j>= 0 and arr[j ] > temp):
            arr[j+1] = arr[j]
            print(*arr)
            j -= 1
            
        arr[j+1] = temp
    print(*arr)    
