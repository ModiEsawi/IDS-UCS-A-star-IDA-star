from queue import PriorityQueue

# check if a certain node is inside a queue
def checkIfInQueue(node, pq, nodesDic):
    if pq.empty():
        return False
    tempQ = PriorityQueue()
    nodeState = node.getState()
    for i in pq.queue: tempQ.put(i)
    while not tempQ.empty():
        index = int(tempQ.get()[1])
        if index in nodesDic:
            got = nodesDic.get(index).getState()
            if nodeState == got:
                return True
    return False


# get the priority of a node in the queue (which is it's f value)
def getPriority(node, pq, nodesDic):
    tempQ = PriorityQueue()
    for i in pq.queue: tempQ.put(i)
    nodeState = node.getState()
    while not tempQ.empty():
        nodeNumber = tempQ.get()
        currentNode = nodesDic.get(int(nodeNumber[1]))
        got = currentNode.getState()
        if nodeState == got:
            return nodeNumber[0]


# after we change a nodes F value we pop it from the queue and then return it so it will have its right place
def resetPriority(node, pq, needed, smallestValue):
    newQueue = PriorityQueue()
    nodesDic = needed[1]
    numberDic = needed[0]
    nodeNumber = numberDic[node]
    while not pq.empty():
        temp = pq.get()
        if temp[1] != nodeNumber:
            newQueue.put(temp)
    newQueue.put((needed[2], needed[3]))
    fatherNode = needed[4]
    node.setFather(fatherNode)
    finalGoal = needed[5]
    goalX = int(finalGoal.getState()[0])
    goalY = int(finalGoal.getState()[1])
    pathCost = fatherNode.getPathCost() + node.getCost()
    node.setfValue(pathCost + (smallestValue * max(abs(node.getState()[0] - goalX), abs(node.getState()[1] - goalY))))
    node.setPathCost(pathCost)
    nodesDic[needed[3]] = node
    numberDic[node] = needed[3]
    return newQueue


# find the node in the dictionary
def findNodeInDic(nodeToLookFor, nodesDic):
    for key, value in nodesDic.items():
        state = value.getState()
        if state == nodeToLookFor.getState():
            return value
    return None


# look for a certain node in the queue and return it
def returnNodeFromQueue(node, pq, nodesDic):
    tempQ = PriorityQueue()
    nodeState = node.getState()
    for i in pq.queue: tempQ.put(i)
    while not tempQ.empty():
        index = int(tempQ.get()[1])
        got = nodesDic.get(index)
        state = got.getState()
        if nodeState == state:
            return got
    return False


# after we change a nodes F value we pop it from the queue and then return it so it will have its right place
def UCSresetPriority(node, pq, numberDic, nodesDic, newPriority, newNodeNumber, fatherNode):
    newQueue = PriorityQueue()
    nodeNumber = numberDic[node]
    while not pq.empty():
        temp = pq.get()
        if temp[1] != nodeNumber:
            newQueue.put(temp)
    newQueue.put((newPriority, newNodeNumber))
    node.setFather(fatherNode)
    node.setPathCost(fatherNode.getPathCost() + node.getCost())
    nodesDic[newNodeNumber] = node
    numberDic[node] = newNodeNumber
    return newQueue


"""
 * The Searcher abstract class.
 * defines methods that are common among all the searchers.
"""


class Searcher:
    def __init__(self, totalPathCost=0, evaluatedNodes=0):
        self.totalPathCost = totalPathCost
        self.evaluatedNodes = evaluatedNodes
        self.priorityQueue = []

    # return the number of nodes evaluated in the algorithm (expanded)
    def getNumberOfNodesEvaluated(self):
        return self.evaluatedNodes

    # trace back from the goal node to its ancestors and return the path/
    def traceBack(self, goalState):
        fathers = [goalState]
        while goalState.getWhereWeCameFrom() is not None:
            fathers.append(goalState.getWhereWeCameFrom())
            goalState = goalState.getWhereWeCameFrom()
        return fathers
