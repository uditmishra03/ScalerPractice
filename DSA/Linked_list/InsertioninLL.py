# Definition for singly-linked list.
class ListNode:
   def __init__(self, val):
       self.val = val
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def __init__(self):
        self.A = None
    def append(self, data):
        new_node = ListNode(val)
        if self.A is None:
            self.A = new_node
            return
        last = self.A
        while last.next:
            last = last.next
        last.next = new_node
    

    def traverse(self):
        temp = self.A
        while temp:
            print(temp.data, end=" ")
        temp = temp.next

    def solve(self, A, B, C):
        newNode = ListNode(B)
        if A == None:
            A = newNode
            return A
        if C <= 0:
            newNode.next = A
            return newNode
        i = 0
        cur_node = A
        while i < C-1 and cur_node.next != None:     # Traversing to C-1 position from 0.
            i+=1
            print(i)
            cur_node = cur_node.next
        newNode.next = cur_node.next
        cur_node.next = newNode
        return A
    

llist = Solution()
llist.append(1)
llist.append(2)
llist.append(3)

llist.traverse()

A = [6,3,3,6,7,8,7,3,7]
B = 3
C = 5

# obj = Solution()
# print(obj.solve(A, B, C))