

arr = [1,2,4,4,55,66,8]


def remove_duplicate(arr):
    list1 = []

    for i in arr:
        if i not in list1:
            list1.append(i)
    return list1s

p = remove_duplicate(arr)
print(p)