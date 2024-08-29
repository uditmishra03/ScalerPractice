from collections import deque
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        current_level = deque()
        current_level.append(A)
        # print(current_level)
        next_level = deque()
        levels = [[A.val]]
        while current_level:
            node = current_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not current_level:
                if next_level:
                    levels.append([n.val for n in next_level])
                current_level = next_level
                next_level = deque()
        return levels
    

    
    
# A = [6, 9, 4, -1, -1, 8, -1, -1, 3, -1, -1]
# obj = Solution()
# obj.solve(A)