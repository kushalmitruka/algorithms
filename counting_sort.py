"""
Given an array A - Use Counting Sort to Sort the array

Can Counting Sort only be implemented on positive numbers??
"""


def countSort(array, max_value, size_of_a):

	result_array = [0]*size_of_a
	temp = [0]*max_value

	for item in array:
		temp[item] += 1

	for i in range(1, max_value):
		temp[i] += temp[i-1]

	for j in range(size_of_a-1, -1, -1):
		item = array[j]
		index_of_item = temp[item]
		result_array[index_of_item - 1] = item
		temp[item] -= 1

	return result_array


if __name__=='__main__':

	n = int(raw_input('Enter the length of Array >> '))

	k = int(raw_input('Enter the max value of Numbers >> '))

	A = raw_input('Array >> ').strip().split()
	
	A = [int(i) for i in A]

	print (countSort(A, k, n))