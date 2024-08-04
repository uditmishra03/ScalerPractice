def helper(nums, k, index):
	# Initialize variables low, high, and res to store the
	# lower index, higher index, and the result index
	low = 0
	high = index
	res = index

	# Perform binary search to find the maximum frequency
	# of the current element by varying the element to its
	# left
	while low <= high:
		mid = low + (high - low) // 2

		# Calculate the sum of the elements from mid to index
		s = sum(nums[mid:index+1])

		# Check if the sum can be increased by at most k by
		# replacing the elements from mid to index with the
		# current element nums[index]
		if s + k >= (index - mid + 1) * nums[index]:
			# If yes, update the result to mid and search
			# for a better solution to the left of mid
			res = mid
			high = mid - 1
		else:
			# If no, search for a better solution to the
			# right of mid
			low = mid + 1
    
	# Return the frequency of the current element
	return index - res + 1

def maxFrequency(nums, k):
	# Sort the input list in non-decreasing order
	nums.sort()
	print(nums)

	# Get the size of the input list
	n = len(nums)

	# Initialize a variable ans to store the maximum frequency
	ans = 0
	current_number, majority_number = None, None
	freq_count = 0

	# Iterate over each element of the input list
	for i in range(n):
		# Update the maximum frequency by taking the
		# maximum of the current maximum frequency and the
		# frequency of the current element
		freq_count = helper(nums, k, i)
		current_number= nums[i]
		if freq_count >= ans:
			ans = freq_count
			majority_number = current_number
		    # ans = max(ans, helper(nums, k, i))
    
	# Return the maximum frequency
	# print(majority_number)
	return [ans, majority_number]


# A = [3, 1, 2, 2, 1]
# B = 3

# A = [5, 5, 5]
# B = 3

A = [-5,6,1,-5,1,-3,1,3,1,5]
B = 9 
print(maxFrequency(A, B))