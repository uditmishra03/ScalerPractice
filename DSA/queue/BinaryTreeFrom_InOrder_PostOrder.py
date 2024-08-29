'''Given the inorder and postorder traversal of a tree, construct the binary tree.

'''


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        inOrder, postOrder = A, B
        in_start, in_end = 0, len(A)-1
        post_start, post_end = 0, len(B)-1

        if in_start == in_end:
            return TreeNode(inOrder[in_start])
        root_val = postOrder[post_end]
        root = TreeNode(root_val)
        # inOrder_idx = 