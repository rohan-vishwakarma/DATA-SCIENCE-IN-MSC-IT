fri = ['ritik', 'rohan', 'priya', 'swati']

def rev_list(array):
    left = 0
    right = len(array)-1

    while left< right:
        temp = array[left] 
        array[left] = array[right]
        array[right] = temp

        left+= 1
        right-=1
    
    return array

print(rev_list(fri))