class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        # First, we append the Node object's name into the answer array
        array.append(self.name)
        # Then, for every child in the Node object's children array, we recursively perform DFS again to append the next Node object's name into the answer array down the branch
        for child in self.children:
            child.depthFirstSearch(array)
        return array