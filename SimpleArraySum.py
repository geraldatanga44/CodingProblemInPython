def simpleArraySum(arr):
	sol = 0 	#track sum of array 
	odd = len(arr) % 2 != 0 	#even or odd array
	low = 0 	#left value
	high = len(arr) - 1 	#right value
	
	if odd: 	#compute odd length array
		while low < high:
			sol += (arr[low] + arr[high])
			low += 1
			high -= 1
		sol += arr[len(arr) // 2]
	if not odd: 	#compute even length array
		while low < high:
			sol += (arr[low] + arr[high])
			low += 1
			high -= 1
	return sol 	#return accummulator 
print(simpleArraySum([1, 2, 3, 4])) 	# simple test case
