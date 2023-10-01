array = [1,2,3,4,5,6,7,8,9,1,2,2]

# remove the duplicates from the array

def remove_dup(array):
    sorted = []
    for i in range(0, len(array)):
        for j in sorted:
            if j == array[i]:
                print("exists")
            else:
                sorted.append(array[i])
    return sorted

remove_dup(array)

p = remove_dup(array)
print(p)

