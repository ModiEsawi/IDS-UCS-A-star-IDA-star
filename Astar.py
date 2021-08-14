from AstarSearch import Astar_Search

""" The A* Algorithm implemented as seen in class, which is a kind of a Searcher.
calls the best first graph search algorithm with the correct F function """
def Astar_search(matrix):
    # cost of path function
    def g(node, fatherNode):
        return fatherNode.getPathCost() + node.getCost()

    # heuristic function
    def h(node, goalX, goalY):
        neighborX = node.getState()[0]
        neighborY = node.getState()[1]
        hFunction = matrix.getSmallestValue() * max(abs(neighborX - goalX), abs(neighborY - goalY))
        return hFunction
    # return F function which is actually g + h
    return Astar_Search().search(matrix, f=lambda n, d, x, y: g(n, d) + h(n, x, y))
