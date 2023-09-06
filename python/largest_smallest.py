arr = [12,4,5,67,77,777,7]


def largestEle(array):
    max = array[0] 

    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[j] > max:
                max = array[i]
    return max

lar = largestEle(arr)
print(lar)



def SmallestEle(array):
    max = array[0] 

    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[j] < max:
                max = array[i]
    return max

small = SmallestEle(arr)
print(small)