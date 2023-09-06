import array as arr

myarr = arr.array('i', [12,34,567,8,909])

def BubbleSort(array):

    if len(array) == 0:
        return f"array cannot be empty"
    else:
        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp            
        return array
execute = BubbleSort(myarr)
print(execute)   

