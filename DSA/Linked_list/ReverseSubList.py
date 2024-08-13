class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a new node at the
    # beginning of the list
    def push(head_ref, new_data):

        new_node = Node(new_data)
        new_node.data = new_data
        new_node.next = (head_ref)
        (head_ref) = new_node
        return head_ref

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
    
    # The standard reverse function used
    # to reverse a linked list
    def reverseLL(self, head):

        prev = None   
        curr = head
    
        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    
    # Function used to reverse a linked list
    # from position m to n which uses reverse
    # function
    def reverseBetween(head, m, n):

        if (m == n):
            return head
            
        # revs and revend is start and end respectively
        # of the portion of the linked list which
        # need to be reversed. revs_prev is previous
        # of starting position and revend_next is next
        # of end of list to be reversed.
        revs = None
        revs_prev = None
        revend = None
        revend_next = None
    
        # Find values of above pointers.
        i = 1
        curr = self.head
        
        while (curr and i <= n):
            if (i < m):
                revs_prev = curr
    
            if (i == m):
                revs = curr
    
            if (i == n):
                revend = curr
                revend_next = curr.next
    
            curr = curr.next
            i += 1

        revend.next = None
    
        # Reverse linked list starting with
        # revs.
        revend = self.reverseLL(head)
    
        # If starting position was not head
        if (revs_prev):
            revs_prev.next = revend
    
        # If starting position was head
        else:
            head = revend
    
        revs.next = revend_next
        return
    



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

head_list = llist.traverse()

# print(head)
B, C = 2, 4
reverseBetween(self.head, B, C)

# Traverse and print the linked list
print("traversing LL:")
llist.traverse()
