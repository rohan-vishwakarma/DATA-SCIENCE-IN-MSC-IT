arr = [12,3,4,5,6,7,1,2]


def find_arr(arr, num):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] + arr[j] == num:
                print( (arr[i], arr[j]))


p = find_arr(arr, 5)