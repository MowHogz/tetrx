from block import predefined_block
import threading
from block import block
import time 
from output import printer
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
class game:
    def __init__(self, user, height, width):
        self.user = user 
        self.default = False
        self.full = True
        self.height = height
        self.width = width 
        self.matrix = creator(height,width,self.default)
        self.start_y = 0
        self.start_x = 5
        self.falling_star = block(self, self.start_y, self.start_x)
        self.next_falling_star = block(self, self.start_y, self.start_x)
        self.t = threading.Thread(target= self.the_game, args=())
        self.score = 0 
        self.pending_direction = 'r'
        self.t.start()


    def the_game(self):
        while not self.out():
            self.round()
            self.score += 1
            text = self.display()
            print (text)
            try:
                self.user.manager.bot.bot.edit_message_text(
                        "Buttons", self.user.id, self.user.another_message, reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("←", callback_data='l'), InlineKeyboardButton("↑", callback_data='u'), InlineKeyboardButton("↓", callback_data='d'),InlineKeyboardButton("➜" , callback_data='r') ]]) )
            except:
                print ("many stuff")
            #exit()
                
            try:

                self.user.manager.bot.bot.edit_message_text(text, self.user.id, self.user.board_id)
            except:
                pass

            time.sleep(0.3) 
    def out(self):
        return False
    def display(self): 
        text = ""
        text += printer(self.matrix)

        return text 
    def round(self):
        
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
            y = self.falling_star.y
            x = self.falling_star.x
            
            print (self.falling_star)
            print (self.falling_star.cw())
            exit()
            new_star  = predefined_block( self, y , x ,self.falling_star.cw())
            if new_star.can_insert:
                self.falling_star = new_star
        elif self.current_direction == 'ccw':
            pass
        else: 
            pass

        if self.gravity(): #
            y = self.falling_star.y
            x = self.falling_star.x
            self.falling_star.insert(y, x)
            pass
        else: 
            y = self.falling_star.y
            x = self.falling_star.x
            self.falling_star.insert(y, x)

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
            self.current_direction = False
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