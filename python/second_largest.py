
arr = [1,2,3,4,5,6,7,8,11,22,33,44,999]
def second_lar(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left+=1
        right-=1

    second_largest = arr[1]
    return second_largest

p = second_lar(arr)
print(p)