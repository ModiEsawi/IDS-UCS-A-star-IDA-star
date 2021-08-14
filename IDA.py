from IDA_Search import IDA_Search
""" the iterative deepening A* algorithm , calls the IDA_Search algorithm with the right parameters which will
 perform DFS with the limits we saw in class"""

def IDA(matrix):
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
    def f(node, father, x, y):
        return g(node, father) + h(node, x, y)

    finalGoal = matrix.getGoalState()
    initialState = matrix.getInitialState()
    initialState.setCost(0)
    initialState.setPathCost(0)
    goalX = int(finalGoal.getState()[0])
    goalY = int(finalGoal.getState()[1])
    threshold = h(initialState, goalX, goalY)
    currentIDA = IDA_Search()
    while True:
        distance = currentIDA.search(matrix, f, initialState, threshold, 0)
        if distance == float("inf"):
            return "no path"
        elif isinstance(distance, list):
            fathers = distance
            if len(fathers) == 1:
                solutionString = "no path"
                currentIDA.totalPathCost = -1
                return solutionString
            else:
                goal = fathers[0]
                currentIDA.totalPathCost += goal.getCost()
                goalIsFound = goal.getWhereWeCameFrom()
                while goalIsFound.getWhereWeCameFrom() is not None:
                    currentIDA.totalPathCost += goalIsFound.getCost()
                    goalIsFound = goalIsFound.getWhereWeCameFrom()
                finalAnswer = (fathers, currentIDA.totalPathCost, currentIDA.evaluatedNodes)
                return finalAnswer
        else:
            threshold = distance
