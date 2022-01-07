def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)

def helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value): 
        closest = tree.value
        
    if target < tree.value: 
        return helper(tree.left, target, closest)
    elif target > tree.value: 
        return helper(tree.right, target, closest)
    else:
        return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def main():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.left.left.left = BST(1)
    root.right.left.right = BST(14)
    print(findClosestValueInBst(root, 12))
    
if __name__ == "__main__":
    main()