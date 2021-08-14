"""
This is the main function which will read an input.txt file , and create an output.txt file with the maze's
path answer, path cost, and number of evaluated nodes.
"""

from IDA import IDA
from Astar import Astar_search
from IDS import IDS
from Uniform_Cost_Search import uniform_cost_search
from Matrix import Matrix

# reading the input file

readIPsFiles = open("input.txt", 'r')
Lines = readIPsFiles.readlines()
readIPsFiles.close()
MatrixSize = int(Lines[3])
init = (int(Lines[1].split(",")[0]), int(Lines[1].split(",")[1]))
final = (int(Lines[2].split(",")[0]), int(Lines[2].split(",")[1]))
algorithm = Lines[0].strip("\n")  # the given search algorithm
smallestValue = float("inf")
matrix = [[0 for x in range(MatrixSize)] for y in range(MatrixSize)]

# creating the matrix
for i in range(MatrixSize):
    for j in range(MatrixSize):
        matrix[i][j] = int(Lines[i + 4].split(",")[j])
        if matrix[i][j] < smallestValue and matrix[i][j] != -1:
            smallestValue = matrix[i][j]
maze = Matrix(matrix, init, final, MatrixSize, MatrixSize, smallestValue)
finalGoal = maze.getGoalState().getCost()
answer = None

# calling the correct algorithm that is required in the text file
if finalGoal == -1:  # if the goal state is -1 then we return no path immediately
    answer = "no path"
elif algorithm == "UCS":
    answer = maze.getPathAsString(uniform_cost_search(maze))
elif algorithm == "IDS":
    answer = maze.getPathAsString(IDS(maze, 20))
elif algorithm == "ASTAR":
    answer = maze.getPathAsString(Astar_search(maze))
elif algorithm == "IDASTAR":
    answer = maze.getPathAsString(IDA(maze))

# writing the answer to an output file
outputFile = open("output.txt", "w")
outputFile.write(answer)
outputFile.close()
