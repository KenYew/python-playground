"""
tree =
                 1
              /    \
            2        3
           /  \     /  \
         4     5   6    7 
        / \    /
       8   9  10
Output: [15, 16, 18, 10, 11]
15 == 1 + 2 + 4 + 8
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7
"""
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
    root.left.right.left = BinaryTree(10)
    print(branchSums(root))
    
if __name__ == "__main__":
    main()
    
# O(n) Time | O(n) Space
# Time: traversing n nodes with constant time operations
# Space: returning a list of branch sums with the length of the number of leaf nodes in the input BT
def branchSums(root):
    sums = []
    # Initialising parameters for the root node where initially there are no runningSums 
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None: 
        return
    # Recursively compute sum all the way to leaf node
    newRunningSum = runningSum + node.value
    # If node is a leaf node (reached the end of the branch), add the complete running sum to the answer
    if node.left is None and node.right is None: 
        sums.append(newRunningSum)
        return
    # Recursively calls the helper function to continue traversing and summing up nodes on both branches
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)