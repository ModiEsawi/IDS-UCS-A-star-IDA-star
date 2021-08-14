from Best_First_Graph_Search import Best_First_Graph_Search
"""
The UCS algorithm as implemented in class, calls the best first graph search algorithm with f = g . 
"""
def uniform_cost_search(matrix):
    # cost of path function
    def g(node, fatherNode):
        return fatherNode.getPathCost() + node.getCost()

    # return F function which is actually g
    return Best_First_Graph_Search().search(matrix, f=g)
