def insertion_sort(arr):
    n = len(arr)
    for current in range(1,n):
        current_card = arr[current]
        correctPosition = current - 1 #it will go from i-1 to 0

        while correctPosition >= 0:
            if(arr[correctPosition]< current_card):
                break
            else:
                arr[correctPosition + 1] = arr[correctPosition]
                correctPosition -= 1
            arr[correctPosition + 1] = current_card

    return arr

print(insertion_sort([12,25,11,34,90,22]))