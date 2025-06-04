def linear_search(lst, t):
    for i in range(0,len(lst)):
        if lst[i] == t:
            return i

    return -1 

my_lst = [10,23,45,70,11]
target = 70

result = linear_search(my_lst, target)
print(result)

