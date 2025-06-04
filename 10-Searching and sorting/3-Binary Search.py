def binary_search(lst, t):
    start = 0
    size = len(lst)
    end = size - 1 

    while(start <= end):
        mid = (start + end)//2
        if lst[mid] == t:
            return mid
        elif lst[mid] > t:
            end = mid - 1
        elif lst[mid] < t:
            start = mid + 1
        
    return -1
    
my_lst = [10,23,35,45,50,70,85]
target = 85
print(binary_search(my_lst, target))