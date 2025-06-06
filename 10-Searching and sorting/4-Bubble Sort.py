def bubble_sort(arr):
    n = len(arr)
    # for i in range(n): Not optimal solution...
    #     for j in range(0,n-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr




print(bubble_sort([12,25,11,34,90,22]))