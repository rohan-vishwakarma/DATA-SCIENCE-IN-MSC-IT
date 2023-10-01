array = [12,45,87,1,46,77]

def selection_sort(arr):
    new_arr =[]
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i] 
                arr[i] = arr[j]   
                arr[j] = temp

    return arr    
        
        


p = selection_sort(array)
print(p)
