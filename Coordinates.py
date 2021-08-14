""" Coordinates class
 X and Y coordinates of the each given point in the matrix
"""


class Coordinates:
    # creating the instance via the constructor
    def __init__(self, position):
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]

    # return the point's X
    def getX(self):
        return int(self.x)

    # return the point's Y
    def getY(self):
        return int(self.y)

    # set the point's X
    def SetX(self, newX):
        self.x = newX

    # set the point's Y
    def setY(self, newY):
        self.y = newY
