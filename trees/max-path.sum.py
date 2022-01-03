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

def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))
    
    # ====================================================
    # STEP 1: RECURSIVE DFS CALLS TO REACH LEAF NODE FIRST
    # ====================================================
    # Recursively call child nodes all the way to the branch end (DFS) first before executing the below code
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    
    # ===================================================================
    # STEP 2: BACKTRACK USING MAX COMPUTATIONS FROM LEAF BACK TO THE ROOT
    # ===================================================================
    # Once recursive DFS until the branch end is complete, backtrack with the following computations:
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
    
    return (maxSumAsBranch, maxPathSum) # Return tuple with MaxSumAsBranch, maxPathSum values

def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(maxPathSum(root))
    
if __name__ == "__main__":
    main()