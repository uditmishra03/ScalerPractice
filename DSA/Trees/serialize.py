                            
from queue import Queue
from typing import Optional

# Definition for a
# binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Check if the tree is empty
        if not root:
            return ""

        # Initialize an empty string
        # to store the serialized data
        s = ""
        # Use a queue for
        # level-order traversal
        q = Queue()
        # Start with the root node
        q.put(root)

        # Perform level-order traversal
        while not q.empty():
            # Get the front node in the queue
            cur_node = q.get()

            # Check if the current node is
            # null and append "#" to the string
            if not cur_node:
                s += "#,"
            else:
                # Append the value of the
                # current node to the string
                s += str(cur_node.val) + ","
                # Push the left and right children
                # to the queue for further traversal
                q.put(cur_node.left)
                q.put(cur_node.right)

        # Return the
        # serialized string
        return s

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Check if the
        # serialized data is empty
        if not data:
            return None

        # Use a queue for
        # level-order traversal
        q = Queue()
        # Use a list to store tokens
        tokens = data.split(',')
        # Read the root value
        # from the serialized data
        root_val = int(tokens.pop(0))
        root = TreeNode(root_val)
        q.put(root)

        # Perform level-order traversal
        # to reconstruct the tree
        while not q.empty():
            # Get the front node in the queue
            node = q.get()

            # Read the value of the left
            # child from the serialized data
            left_val = tokens.pop(0)
            # If the value is not "#", create a new
            # left child and push it to the queue
            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.put(left_node)

            # Read the value of the right child
            # from the serialized data
            right_val = tokens.pop(0)
            # If the value is not "#", create a
            # new right child and push it to the queue
            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.put(right_node)

        # Return the reconstructed
        # root of the tree
        return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()
    print("Original Tree: ", end="")
    inorder(root)
    print()

    serialized = solution.serialize(root)
    print("Serialized: " + serialized)

    deserialized = solution.deserialize(serialized)
    print("Tree after deserialization: ", end="")
    inorder(deserialized)
    print()
                           
                        