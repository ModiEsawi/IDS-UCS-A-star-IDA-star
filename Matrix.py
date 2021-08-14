from Node import Node
from Coordinates import Coordinates

"""
 * The Matrix class
 * define a matrix , which for all elements ,the cost is it's value. this is representable class , which mean we can
 * build a an object of this class by given list of strings (given in CTOR)
 """


class Matrix:
    # creating the instance via the constructor
    def __init__(self, matrix, initialState, finalGoal, rowsNumber, columnNumber, smallestValue):
        self.matrix = matrix
        self.smallestValue = smallestValue
        self.finalGoal = finalGoal
        self.rowsNumber = rowsNumber
        self.columnNumber = columnNumber
        startingState = Node()
        startingState.state = initialState
        xStart = initialState[0]
        yStart = initialState[1]
        xEnd = finalGoal[0]
        yEnd = finalGoal[1]
        startingState.costOfPath = matrix[xStart][yStart]
        startingState.cost = matrix[xStart][yStart]
        endingState = Node()
        endingState.state = finalGoal
        endingState.costOfPath = matrix[xEnd][yEnd]
        endingState.cost = matrix[xEnd][yEnd]
        self.initialState = startingState
        self.finalGoal = endingState

    # return the neighbors of a certain node in a clock wise order
    def getNeighbors(self, givenState):
        neighbors = []
        currentState = givenState.getState()
        x = None
        y = None
        if type(currentState) is tuple:
            x = int(currentState[0])
            y = int(currentState[1])
        else:
            x = Coordinates(currentState).getX()
            y = Coordinates(currentState).getY()
        # right up
        if y + 1 <= self.columnNumber - 1 and x - 1 >= 0 and self.matrix[x - 1][y + 1] != -1 and self.matrix[x][
            y + 1] != -1 \
                and self.matrix[x - 1][y] != -1:
            rightUp = Node()
            rightUp.state = (x - 1, y + 1)
            rightUp.setCost(self.matrix[x - 1][y + 1])
            rightUp.setPathCost(self.matrix[x - 1][y + 1])
            neighbors.append(rightUp)
        # up
        if x - 1 >= 0 and self.matrix[x - 1][y] != -1:
            up = Node()
            up.state = (x - 1, y)
            up.setCost(self.matrix[x - 1][y])
            up.setPathCost(self.matrix[x - 1][y])
            neighbors.append(up)

        # left up
        if y - 1 >= 0 and x - 1 >= 0 and self.matrix[x - 1][y - 1] != -1 and self.matrix[x][y - 1] != -1 and \
                self.matrix[x - 1][y] != -1:
            leftUp = Node()
            leftUp.state = (x - 1, y - 1)
            leftUp.setCost(self.matrix[x - 1][y - 1])
            leftUp.setPathCost(self.matrix[x - 1][y - 1])
            neighbors.append(leftUp)

        # left
        if y - 1 >= 0 and self.matrix[x][y - 1] != -1:
            left = Node()
            left.state = (x, y - 1)
            left.setCost(self.matrix[x][y - 1])
            left.setPathCost(self.matrix[x][y - 1])
            neighbors.append(left)

        # left down
        if y - 1 >= 0 and x + 1 <= self.rowsNumber - 1 and self.matrix[x + 1][y - 1] != -1 and self.matrix[x][
            y - 1] != -1 \
                and self.matrix[x + 1][y] != -1:
            leftDown = Node()
            leftDown.state = (x + 1, y - 1)
            leftDown.setCost(self.matrix[x + 1][y - 1])
            leftDown.setPathCost(self.matrix[x + 1][y - 1])
            neighbors.append(leftDown)
        # down
        if x + 1 <= self.rowsNumber - 1 and self.matrix[x + 1][y] != -1:
            down = Node()
            down.state = (x + 1, y)
            down.setCost(self.matrix[x + 1][y])
            down.setPathCost(self.matrix[x + 1][y])
            neighbors.append(down)

        # right down
        if y + 1 <= self.columnNumber - 1 and x + 1 <= self.rowsNumber - 1 and self.matrix[x + 1][y + 1] != -1 and \
                self.matrix[x][y + 1] != -1 and self.matrix[x + 1][y] != -1:
            rightDown = Node()
            rightDown.state = (x + 1, y + 1)
            rightDown.setCost(self.matrix[x + 1][y + 1])
            rightDown.setPathCost(self.matrix[x + 1][y + 1])
            neighbors.append(rightDown)
        # right
        if y + 1 <= self.columnNumber - 1 and self.matrix[x][y + 1] != -1:
            right = Node()
            right.state = (x, y + 1)
            right.setCost(self.matrix[x][y + 1])
            right.setPathCost(self.matrix[x][y + 1])
            neighbors.append(right)
        return neighbors

    # return the initial state of the matrix
    def getInitialState(self):
        return self.initialState

    # return the goal test of the matrix
    def getGoalState(self):
        return self.finalGoal

    # return the smallest value inside the matrix
    def getSmallestValue(self):
        return int(self.smallestValue)

    # return the path as a solution string
    def getPathAsString(self, finalAnswer):
        if isinstance(finalAnswer, str):
            return finalAnswer
        solutionPath = finalAnswer[0]
        pathString = ""
        solutionLen = len(solutionPath)
        currentNode = solutionPath.pop()
        nextNode = solutionPath.pop()
        currIndex = currentNode.getState()
        nextIndex = nextNode.getState()
        for i in range(solutionLen - 1):
            status = ""
            if Coordinates(currIndex).getX() < Coordinates(nextIndex).getX() and Coordinates(
                    currIndex).getY() == Coordinates(nextIndex).getY():
                status = "D-"
            elif Coordinates(currIndex).getX() > Coordinates(nextIndex).getX() and Coordinates(
                    currIndex).getY() == Coordinates(nextIndex).getY():
                status = "U-"
            elif Coordinates(currIndex).getY() < Coordinates(nextIndex).getY() and Coordinates(
                    currIndex).getX() == Coordinates(nextIndex).getX():
                status = "R-"
            elif Coordinates(currIndex).getY() > Coordinates(nextIndex).getY() and Coordinates(
                    currIndex).getX() == Coordinates(nextIndex).getX():
                status = "L-"
            elif Coordinates(currIndex).getY() < Coordinates(nextIndex).getY() and Coordinates(
                    currIndex).getX() < Coordinates(nextIndex).getX():
                status = "RD-"
            elif Coordinates(currIndex).getY() < Coordinates(nextIndex).getY() and Coordinates(
                    currIndex).getX() > Coordinates(nextIndex).getX():
                status = "RU-"
            elif Coordinates(currIndex).getY() > Coordinates(nextIndex).getY() and Coordinates(
                    currIndex).getX() < Coordinates(nextIndex).getX():
                status = "LD-"
            elif Coordinates(currIndex).getY() > Coordinates(nextIndex).getY() and Coordinates(
                    currIndex).getX() > Coordinates(nextIndex).getX():
                status = "LU-"
            pathString += status
            currIndex = nextIndex
            if i != solutionLen - 2:
                nextIndex = solutionPath.pop().getState()
        pathString = pathString[:-1]
        pathString = pathString + " " + str(finalAnswer[1]) + " " + str(finalAnswer[2])
        return pathString
