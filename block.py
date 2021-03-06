from shapes import random_shape
class block:
    def __init__(self, game, y , x):
        self.game = game
        self.y = y
        self.x = x
        self.shape = random_shape()
        self.shapes = [
            [False, True, False],
            [True, True, True]]
        self.height = len(self.shape)
        self.width = len(self.shape[0])
    def remove (self):
        for row in range(self.y, self.y + self.height):
            for column in range(self.x, self.x + self.width):
                self.game.matrix[row][column] = self.game.default



    def insert(self, y , x):
        self.y = y 
        self.x = x
        for row in range(self.height):
            for column in range(self.width):
                if self.shape[row][column] == self.game.full:
                    self.game.matrix[row + y ][column + x] = self.game.full
        



    def can_insert(self, y, x):
        if y < 0 or x < 0       or      y + self.height > self.game.height or x + self.width > self.game.width:
            return False
        for row in range(self.height):
            for column in range(self.width):
                if  self.shape[row][column] == self.game.full  and  self.game.matrix[row + y][column + x] == self.game.full:
                    return False
                else: 
                    pass
        return True
    
    def cw(self):
        matrix = []
        for column in range(self.width):
            matrix.append([])
        for column in range(self.width):
            for row in range(self.height):
                matrix[column].append(self.shape[row][self.width-1 - column])
        return matrix



class predefined_block:
    def __init__(self, game, y , x, shape):
        self.game = game
        self.y = y
        self.x = x
        self.shape = shape
        #self.shapes = shape
        self.height = len(self.shape)
        self.width = len(self.shape[0])
    def remove (self):
        for row in range(self.y, self.y + self.height):
            for column in range(self.x, self.x + self.width):
                self.game.matrix[row][column] = self.game.default



    def insert(self, y , x):
        self.y = y 
        self.x = x
        for row in range(self.height):
            for column in range(self.width):
                if self.shape[row][column] == self.game.full:
                    self.game.matrix[row + y ][column + x] = self.game.full
        



    def can_insert(self, y, x):
        if y < 0 or x < 0       or      y + self.height > self.game.height or x + self.width > self.game.width:
            return False
        for row in range(self.height):
            for column in range(self.width):
                if  self.shape[row][column] == self.game.full  and  self.game.matrix[row + y][column + x] == self.game.full:
                    return False
                else: 
                    pass
        return True

    def cw(self):
        matrix = []
        for column in range(self.width):
            matrix.append([])
        for column in range(self.width):
            for row in range(self.height):
                matrix[column].append(self.shape[row][self.width-1 - column])
        return matrix
