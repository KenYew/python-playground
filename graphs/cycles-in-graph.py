# O(v + e) Time | O(v) Space
# where v is the number of vertices and e is the nunmber of edges in the graph
def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]
    
    for node in range(numberOfNodes):
        if visited[node]:
            continue
        
        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            return True
        
    return False

def isNodeInCycle(node, edges, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True
    
    neighbours = edges[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            containsCycle = isNodeInCycle(neighbour, edges, visited, currentlyInStack)
            if containsCycle:
                return True
        elif currentlyInStack[neighbour]:
            return True
        
    currentlyInStack[node] = False
    return False