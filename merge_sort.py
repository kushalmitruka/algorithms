"""
Given Array A - Sorting the array in Increasing Order using Merge Sort
"""

def mergeSortedArrays(array_1, array_2):
	i = 0
	j = 0
	len_array_1 = len(array_1)
	len_array_2 = len(array_2)
	result_array = []

	while(i < len_array_1 or j < len_array_2):
		if (i < len_array_1 and j < len_array_2):
			if array_1[i] < array_2[j]:
				result_array.append(array_1[i])
				i += 1
			elif array_1[i] >= array_2[j]:
				result_array.append(array_2[j])
				j += 1
		elif i == len_array_1 and j < len_array_2:
			result_array.extend(array_2[j:])
			break
		elif j == len_array_2 and i < len_array_1:
			result_array.extend(array_1[i:])
			break
	
	return result_array


def mergeSort(A, low, high):

	if low == high - 1:
		return A[low:high]


	mid = (low + high)//2

	left_sorted = mergeSort(A, low, mid)
	right_sorted = mergeSort(A, mid, high)

	return mergeSortedArrays(left_sorted, right_sorted)


if __name__=='__main__':

	n = int(raw_input('Enter the Length of Array: '))
	A = raw_input().split(' ')
	A = [int(x) for x in A]

	sorted_array = mergeSort(A, 0, n)

	print (', '.join((str(i) for i in sorted_array)))