def solve(self, root):
        if not root:
            return None
        queue = []
        ans=[]
 
    # Enqueue Root and initialize height
        queue.append(root)
        ans.append(root.val)
    
        while(len(queue) > 0):
    
            # Print front of queue and
            # remove it from queue
            
            node = queue.pop(0)
    
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
                ans.append(node.left.val)
            else:
                ans.append(-1)
    
            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
                ans.append(node.right.val)
            else:
                ans.append(-1)
        return ans
