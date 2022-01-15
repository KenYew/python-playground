class BinaryTree:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
        
def heightBalancedBinaryTree(tree):
    isBalanced, _ = checkBalanced(tree)
    return isBalanced

def checkBalanced(tree): 
    if tree is None:
        return (True, -1)
    
    isLeftTreeBalanced, leftTreeHeight = checkBalanced(tree.left)
    isRightTreeBalanced, rightTreeHeight = checkBalanced(tree.right) 

    isBalanced = isLeftTreeBalanced and isRightTreeBalanced and (abs(leftTreeHeight - rightTreeHeight) <= 1)
    height = max(leftTreeHeight, rightTreeHeight) + 1
    
    return (isBalanced, height)