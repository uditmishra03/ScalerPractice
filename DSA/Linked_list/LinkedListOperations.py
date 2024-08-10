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

    def deleteNode(self, head, idx):
        print('Deleting node where head is :', head, 'at:', idx)
        if idx == 0:
            head= self.head.next
            return head
        else:
            i = 0
            curNode = self.head
            while i < idx-1 and curNode.next != None:
                i +=1
                curNode = curNode.next
            # B = curNode.next
            curNode.next = curNode.next.next
            return head

    def findDuplicates(self):
        print('Checking if duplicates are found in LL')
        cur_node = self.head
        if cur_node is None:
            return
        while cur_node.next:
            if cur_node.data == cur_node.next.data:
                new = cur_node.next.next
                cur_node.next = None
                cur_node.next = new
                # print('Deletion Done!')
            else:
                cur_node= cur_node.next
        return self.head

    def getLLSize(self):
        # get the size of of linkedList
        n = 0
        curr_node = self.head
        while curr_node:
            n +=1
            curr_node = curr_node.next
        return n
    
    def deleteNode(self, A, B):
        print("Deleting Node of position:", B)
        n = llist.getLLSize()
        print(n)
        if B >0 and B > n:
            print("next node:", A.next.data)
            A = A.next
            return A
        # elif B > n:
        else:
            i = 0
            curNode = A
            while i < B-1 and curNode.next != None:
                i +=1
                curNode = curNode.next
            # B = curNode.next
            curNode.next = curNode.next.next
            return A

    def RemoveNthFromEnd(self,head,  B):
        llist.traverse()
        n = llist.getLLSize()
        print('size of ll:', n)
        print('\nRunning Function Remove', n-B, "node from the end.")
        llist.deleteNode(head, n-B)



# Create a linked list
llist = LinkedList()
llist.append(99)
llist.append(98)
llist.append(2)
llist.append(4)
llist.append(4)
llist.append(8)
llist.append(8)
# llist.append(16)

# Traverse and print the linked list
print("traversing LL:")

head = llist.traverse()
# print(head)
print('Size of linked list: ', llist.getLLSize())
print()

# llist.deleteNode(head, 3)

# llist.findDuplicates()

# # Traverse and print the linked list
# print("\ntraversing LL post deletion:")
# llist.traverse()
# print()
llist.traverse()
# llist.deleteNode(head, 9)
llist.traverse()
print('Size of linked list: ', llist.getLLSize())

llist.RemoveNthFromEnd(head, 2)