from Searcher import Searcher
""" The DFS - limit Algorithm as seen in class , which is a kind of a Searcher.
performs depth first search to a given depth limit """

class DFS_L(Searcher):
    # The actual searching method
    def search(self, matrix, limit):
        goalIsFound = None
        initialState = matrix.getInitialState()
        finalGoal = matrix.getGoalState()
        statesStack = [initialState]
        while len(statesStack) != 0:
            top = statesStack.pop()
            if top.getState() == finalGoal.getState():
                goalIsFound = top
                break
            self.evaluatedNodes += 1
            if top.getDepth() < limit:
                neighbors = matrix.getNeighbors(top)

                for neighbor in neighbors:
                    neighbor.setPathCost(top.getPathCost() + neighbor.getCost())
                    statesStack.append(neighbor)
                    neighbor.setFather(top)
                    neighbor.setDepth(top.getDepth() + 1)

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
