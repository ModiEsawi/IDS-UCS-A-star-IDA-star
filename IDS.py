from DFS_L import DFS_L
""" The iterative DFS Algorithm as seen in class .
calls the DFS-L algorithm with a depth limit growing till 20  """

def IDS(matrix, maxIter):
    dfs_l = DFS_L()
    for depth in range(maxIter):
        result = dfs_l.search(matrix, depth)
        if result != "no path":
            return result
    return "no path"
