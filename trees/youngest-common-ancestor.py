# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(h) Time | O(1) Space - where h is the height of the ancestral tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo: 
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor: 
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0: 
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant

def main():
    root = AncestralTree("A")
    root.left = AncestralTree("B")
    root.right = AncestralTree("C")
    root.left.left = AncestralTree("D")
    root.left.right = AncestralTree("E")
    root.right.left = AncestralTree("F")
    root.right.right = AncestralTree("G")
    root.left.left.left = AncestralTree("H")
    root.right.left.right = AncestralTree("I")

    """
    topAncestor = node A
    descendantOne = node E
    descendantTwo = node I
    """
    
    print(getYoungestCommonAncestor(root, root.left.right, root.right.left.right))
    
if __name__ == "__main__":
    main()
