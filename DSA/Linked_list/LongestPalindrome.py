# Python program to find longest palindrome 
# sublist in a list in O(1) time. 

# Linked List node 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# function for counting the common elements 
def countCommon(a, b) :

	count = 0

	# loop to count common in the list starting 
	# from node a and b 
	while ( a != None and b != None ) :

		# increment the count for same values 
		if (a.data == b.data) :
			count = count + 1
		else:
			break
		
		a = a.next
		b = b.next

	return count 

# Returns length of the longest palindrome 
# sublist in given list 
def maxPalindrome(head) :

	result = 0
	prev = None
	curr = head 

	# loop till the end of the linked list 
	while (curr != None) :
	
		# The sublist from head to current 
		# reversed. 
		next = curr.next
		curr.next = prev 

		# check for odd length 
		# palindrome by finding 
		# longest common list elements 
		# beginning from prev and 
		# from next (We exclude curr) 
		result = max(result, 
					2 * countCommon(prev, next) + 1) 

		# check for even length palindrome 
		# by finding longest common list elements 
		# beginning from curr and from next 
		result = max(result, 
					2 * countCommon(curr, next)) 

		# update prev and curr for next iteration 
		prev = curr 
		curr = next
	
	return result 

# Utility function to create a new list node 
def newNode(key) :

	temp = Node(0) 
	temp.data = key 
	temp.next = None
	return temp 

# Driver code

# Let us create a linked lists to test 
# the functions 
# Created list is a: 2->4->3->4->2->15 
# head = newNode(2) 
# head.next = newNode(4) 
# head.next.next = newNode(3) 
# head.next.next.next = newNode(4) 
# head.next.next.next.next = newNode(2) 
# head.next.next.next.next.next = newNode(15) 

head = newNode(2) 
head.next = newNode(3) 
head.next.next = newNode(3) 
head.next.next.next = newNode(3) 
# head.next.next.next.next = newNode(2) 
# head.next.next.next.next.next = newNode(15) 

print(maxPalindrome(head)) 

# This code is contributed by Arnab Kundu
