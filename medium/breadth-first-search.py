# O(v + e) Time | O(v) Space
# where v is the number of vertices and e is the number of edges
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # initialise the queue with the root node in the beginning
        queue = [self] # QUEUE should store NODES
        # while the queue is not empty (we haven't traversed the graph yet)
        while len(queue) > 0: 
            # pop the very first element of the queue and set that to be current value
            current = queue.pop(0)
            # append the name of the popped element into our answer array
            array.append(current.name)
            # then, for every child in the Node object's children array, we append the child to the back of the queue in FIFO order (FIFO enables BFS to work)
            for child in current.children:
                queue.append(child)
        # if we break out of the while loop because all elements of the queue have been popped (traversed all nodes in the graph), we return the answer array
        return array