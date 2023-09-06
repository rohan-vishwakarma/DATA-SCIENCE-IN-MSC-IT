def selectionSort(array):
	size = len(array)
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, len(array)):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
				
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [12,4,56,7,88,888]
selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
