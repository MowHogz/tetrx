from block import block
import time 
from output import printer
class game:
    def __init__(self, height, width):
        self.default = False
        self.full = True
        self.height = height
        self.width = width 
        self.matrix = creator(height,width,self.default)
        self.falling_star = block(self)
        self.next_falling_star = block(self)
        self.start_y = 0
        self.start_x = 5
    
    
    def round(self):
        time.sleep(0.3)
        
        self.update_move()#updates the current_direction variable 


        self.falling_star.remove()
        y = self.falling_star.y
        x = self.falling_star.x

        if self.current_direction == 'r':
            new_x = self.falling_star.x + 1     #mark the new location towards which we are heading 
            if self.falling_star.can_insert(y, new_x): 
                self.falling_star.x = new_x     #declare new changes 
                #self.falling_star.insert(y, new_x)
            else: 
                pass

        elif self.current_direction == 'l':
            new_x = self.falling_star.x - 1
            if self.falling_star.can_insert(y, new_x):
                self.falling_star.x = new_x
                #self.falling_star.insert(y, new_x)
            else: 
                pass

        elif self.current_direction == 'cw':
            pass
        elif self.current_direction == 'ccw':
            pass
        else: 
            pass

        if self.gravity(): #
            pass
        else: 
            self.create_new_falling_star()
    
    
    def update_move(self):
        if self.pending_direction == 'r':
            self.current_direction = 'r'
            self.pending_direction = False

        elif self.pending_direction == 'l':
            self.current_direction = 'l'
            self.pending_direction = False

        elif self.pending_direction == 'cw': 
            self.current_direction = 'cw'
            self.pending_direction = False

        elif self.pending_direction == 'ccw':
            self.current_direction = 'ccw'
            self.pending_direction = False
        
        else: 
            pass

        
    def create_new_falling_star(self): #make there be a new falling star 
        self.falling_star = self.next_falling_star
        self.next_falling_star = block(self, self.start_y, self.start_x)
        


    def gravity(self): #returns True if piece is still falling 
        y = self.falling_star.y
        x = self.falling_star.x
        if self.falling_star.can_insert(y + 1, x): #if we can go down by one 
            self.falling_star.y = y + 1 
            return True
        else: 
            return False

def creator(height, width, default):
    mat = []
    for row in range(height):
        mat.append([])
        for col in range(width):
            mat[row].append(default)
    return mat

mat = creator(10,10, 0)
printer(mat)