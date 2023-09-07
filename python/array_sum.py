
arr = [12,4,56,7,88,888]



def calculate(array):
    sum = 0
    for i in range(len(array)):
        sum+= array[i]
    
    return sum


p = calculate(arr)
print(p)