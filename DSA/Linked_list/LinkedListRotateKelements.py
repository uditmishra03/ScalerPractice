class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        return self.head
    
    def getLLSize(self):
        # get the size of of linkedList
        n = 0
        curr_node = self.head
        while curr_node:
            n +=1
            curr_node = curr_node.next
        return n

    
    def reverseKNodes(self, head, k):
        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        # Reverse first K notes of the Linked list
        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count +=1
        
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverseKNodes(next, k) 
  
        # prev is new head of the input list 
        return prev 


    


# Create a linked list
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
# llist.append(8)
# llist.append(16)

# Traverse and print the linked list
print("traversing LL:")
llist.traverse()
# llist.deleteNode(head, 9)
llist.traverse()
print('Size of linked list: ', llist.getLLSize())

llist.head = llist.reverseKNodes(llist.head, 3)
print("Revesed Linked List:")
llist.traverse()
