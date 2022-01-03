"""
Input:
         1
      /    \
     2      3      
    /  \   /  \   
  4     5 6    7  
 / \    
8   9               
Output: 
      1
    /    \
   3      2      
 /  \    /  \   
7    6  5    4  
            / \    
           9   8        
"""

# O(n) Time | O(n) Space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        node = queue.pop(0)
        if node is None:
            continue
        swapLeftAndRight(node)
        queue.append(node.left)
        queue.append(node.right)
    return tree
        
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    print(invertBinaryTree(root).left.value)
    
if __name__ == "__main__":
    main()