"""
Input:
                 1
              /    \
            2        3      Depth = 1
           /  \     /  \   
         4     5   6    7   Depth = 2
        / \    
       8   9                Depth = 3
Output: 16
Explanation: 
- The depth of the node with value 2 is 1.
- The depth of the node with value 3 is 1.
- The depth of the node with value 4 is 2.
- The depth of the node with value 5 is 2.
- etc...
- Summing all of these depths yields 16.
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Average case: When the tree is balanced
# O(n) Time | O(h) Space - where n is the number of nodes in BT and h is the height of BT
def nodeDepths(root):
    sumofDepths = 0
    # Stack of dicts where each dict contains node and depth as key-value pairs
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0: 
        nodeInfo = stack.pop()
        node = nodeInfo["node"]
        depth = nodeInfo["depth"] 
        if node is None: 
            continue
        sumofDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumofDepths

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
    print(nodeDepths(root))
    
if __name__ == "__main__":
    main()