from Searcher import Searcher

""" the iterative deepening A* search algorithm, performs a DFS with the limits we saw in class , will stop a current
depth first search run if the depth of the path is larger then 20"""

class IDA_Search(Searcher):
    # The actual searching method
    def search(self, matrix, f, node, threshold, currentDepth):
        goal = matrix.getGoalState().getState()
        goalX = int(goal[0])
        goalY = int(goal[1])
        minVal = float("inf")
        neighbors = matrix.getNeighbors(node)
        currentDepth += 1
        if currentDepth > 20:
            return float("inf")
        neighbors = list(reversed(neighbors))
        if node.getState() == goal:
            fathers = self.traceBack(node)
            return fathers
        self.evaluatedNodes += 1
        for neighbor in neighbors:
            pathCost = node.getPathCost() + neighbor.getCost()
            neighbor.setFather(node)
            neighbor.setPathCost(pathCost)
            neighborsFval = f(neighbor, node, goalX, goalY)
            if neighborsFval <= threshold:
                if neighbor.getState() == goal:
                    fathers = self.traceBack(neighbor)
                    return fathers
                newVal = self.search(matrix, f, neighbor, threshold, currentDepth)
                if isinstance(newVal, list):
                    return newVal
                if newVal < minVal:
                    minVal = newVal
            elif neighborsFval > threshold:
                if neighborsFval < minVal:
                    minVal = neighborsFval
        return minVal
