"""
Input:
            1
         /    \
        3      2      
       /  \     
      7    4   
     /      \
    8        5  
   /          \
  9            6
Output: 6 
Explanation: 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
- There are 6 edges between the first node and the last node of this tree's longest path.
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)
    
    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
    
    return TreeInfo(currentDiameter, currentHeight)
    
class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

def main():
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.right.right = BinaryTree(5)
    root.left.left.left.left = BinaryTree(9)
    root.left.right.right.right = BinaryTree(6)
    print(binaryTreeDiameter(root))
    
if __name__ == "__main__":
    main()