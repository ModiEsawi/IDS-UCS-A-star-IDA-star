"""
 * The Node class
 * defines a Node with a cost, parent(whereWeCameFrom) Fvalue, state, and path cost , which is
 * the cost of whole ancestors.
 """


class Node:
    # creating the instance via the constructor
    def __init__(self, state=None, cost=None, costOfPath=None, fValue=None, father=None):
        self.state = state
        self.cost = cost
        self.costOfPath = costOfPath
        self.fValue = fValue
        self.father = father
        self.depth = 0

    # getters

    # return the nodes state
    def getState(self):
        return self.state

    # return the F value
    def getFvalue(self):
        return self.fValue

    # return the cost of the node
    def getCost(self):
        return self.cost

    # return the path cost
    def getPathCost(self):
        return self.costOfPath

    # return the nodes father
    def getWhereWeCameFrom(self):
        return self.father

    # return the nodes depth
    def getDepth(self):
        return self.depth

    # setters

    # set the nodes F value
    def setfValue(self, newFValue):
        self.fValue = newFValue

    # set the nodes cost
    def setCost(self, newCost):
        self.cost = newCost

    # set the nodes path cost
    def setPathCost(self, newPathCost):
        self.costOfPath = newPathCost

    # set the nodes father
    def setFather(self, newFather):
        self.father = newFather

    # set the nodes depth
    def setDepth(self, newDepth):
        self.depth = newDepth
