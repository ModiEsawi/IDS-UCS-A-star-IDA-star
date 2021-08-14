from queue import PriorityQueue
from Searcher import Searcher, checkIfInQueue, resetPriority, findNodeInDic, getPriority

""" The actual search algorithm that is used in the A* algorithm , takes a matrix and an F function , 
 implemented as we seen in class"""


class Astar_Search(Searcher):
    # The actual searching method
    def search(self, matrix, f):
        nodesDict = {}
        numbersDict = {}
        nodeNumber = 1
        smallestValue = matrix.getSmallestValue()
        goalIsFound = None
        initialState = matrix.getInitialState()
        initialState.setCost(0)
        initialState.setPathCost(0)
        finalGoal = matrix.getGoalState()
        goalX = int(finalGoal.getState()[0])
        goalY = int(finalGoal.getState()[1])
        # a queue which is sorted by the F value
        frontier = PriorityQueue()
        initialState.setfValue(
            smallestValue * max(abs(initialState.getState()[0] - goalX), abs(initialState.getState()[1] - goalY)))
        frontier.put(
            (smallestValue * max(abs(initialState.getState()[0] - goalX), abs(initialState.getState()[1] - goalY)),
             nodeNumber))
        nodesDict[nodeNumber] = initialState
        numbersDict[initialState] = nodeNumber
        nodeNumber += 1
        closedList = set()
        while frontier:
            nodeToDelete = frontier.get()
            currentNode = nodesDict[nodeToDelete[1]]
            if currentNode.getState() == finalGoal.getState():
                goalIsFound = currentNode
                break
            self.evaluatedNodes += 1
            closedList.add(currentNode.getState())
            neighbors = matrix.getNeighbors(currentNode)
            neighbors = list(reversed(neighbors))
            for neighbor in neighbors:
                if neighbor.getState() not in closedList and not checkIfInQueue(neighbor, frontier, nodesDict):
                    pathCost = currentNode.getPathCost() + neighbor.getCost()
                    neighbor.setFather(currentNode)
                    neighbor.setPathCost(pathCost)
                    neighbor.setfValue(f(neighbor, currentNode, goalX, goalY))
                    frontier.put((f(neighbor, currentNode, goalX, goalY), nodeNumber))
                    nodesDict[nodeNumber] = neighbor
                    numbersDict[neighbor] = nodeNumber
                    nodeNumber += 1
                elif checkIfInQueue(neighbor, frontier, nodesDict) and f(neighbor, currentNode, goalX,
                                                                         goalY) < getPriority(neighbor,
                                                                                              frontier,
                                                                                              nodesDict):
                    fVal = f(neighbor, currentNode, goalX, goalY)
                    needed = (numbersDict, nodesDict, fVal, nodeNumber, currentNode, finalGoal)
                    frontier = resetPriority(findNodeInDic(neighbor, nodesDict), frontier, needed, matrix.getSmallestValue())
                    nodeNumber += 1

        if goalIsFound is not None:
            fathers = self.traceBack(goalIsFound)
            if len(fathers) == 1:
                solutionString = "no path"
                self.totalPathCost = -1
                return solutionString
            else:
                self.totalPathCost += goalIsFound.getCost()
                goalIsFound = goalIsFound.getWhereWeCameFrom()
                while goalIsFound.getWhereWeCameFrom() is not None:
                    self.totalPathCost += goalIsFound.getCost()
                    goalIsFound = goalIsFound.getWhereWeCameFrom()
                finalAnswer = (fathers, self.totalPathCost, self.evaluatedNodes)
                return finalAnswer
        else:
            solutionString = "no path"
            return solutionString
