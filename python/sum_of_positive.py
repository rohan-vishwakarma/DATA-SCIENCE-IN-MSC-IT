arr = [1,2, -3, -4,6,7,-9,-8]

ini = 0
sum = 0
for i in range(len(arr)):
    if arr[i] > ini:
        sum+=arr[i]


print(sum)


