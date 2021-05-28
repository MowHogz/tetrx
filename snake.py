import time 
import threading 
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
class snake: 
    def __init__(self, height, width, name, user): 
        self.height = height 
        self.width = width
        self.name = name 
        self.direction = "Right"
        self.d = "r"
        self.user = user
        self.t = threading.Thread(target= self.game, args=())
        self.score = 0 
        self.mat = creator(self.height, self.width, ' ')
        print ("This is me ")
        self.body = [[0,0]]
        self.alive = True
    
    def game(self):
        while self.alive:
            time.sleep(0.1)
            if not self.run():
                #self.alive = False
                return False
            self.score += 1         
            text = self.display()
            #self.user.send(text)
            

            self.user.manager.bot.bot.edit_message_text(text, self.user.id, self.user.board_id)
            #self.user.manager.bot.bot.edit_message_text(text, self.user.id, self.user.board_id)
            #print ("Height", self.height, "Name", self.name)
        self.user.reset()
        

    def update_direction(self):
        #print (self.direction)
        if self.direction == "r":
            self.d = "r"
        elif self.direction == "l":
            self.d = "l"
        elif self.direction == "u":
            self.d = "u"
        else:
            self.d = "d"

    def run(self): 
        #print ("Chocolate")
        head = self.body[0]
        new_head = head[:]
        self.update_direction()
        try:
            self.user.manager.bot.bot.edit_message_text(
                    self.d, self.user.id, self.user.another_message, reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("←", callback_data='l'), InlineKeyboardButton("↑", callback_data='u'), InlineKeyboardButton("↓", callback_data='d'),InlineKeyboardButton("➜" , callback_data='r') ]]) )
        except:
            pass
        if self.d == "r":
            new_head[1] += 1
        
        elif self.d == "l":
            new_head[1] -= 1
        
        elif self.d == "u":
            new_head[0] -= 1
        
        elif self.d == "d":
            new_head[0] += 1
        
        if self.check_if_safe(new_head):    #the snake is making a regular move (not onto a body part, off the map or even food)
            #add new_head to body 
            self.body.insert(0,new_head)
            self.body.pop() #removes tail 
        
        elif self.eating_food(new_head):
            self.body.insert(0,new_head)
        else:
            #if we got here we're not making a regular move and it's not food  
            return False

        return True

    def check_if_safe(self, head):
        y = head[0]
        x = head[1]

        #if collides 
        if y >= self.height or y < 0 or x >= self.width or x < 0 : 
            print ("very dangerous ")
            exit()
            return False 

        #if new locatin is safe 
        if head not in self.body:
            return True
        
        return False





        pass
    def display(self):

        mat = creator(self.height, self.width, '‏‏‎ ‎')

        for unit in self.body:
            mat[unit[0]][unit[1]] = 'X'
        
        text = "Score: {}".format(self.score)
        text += printer(mat)
        #print (text)

        return text
    

def printer(matrix):
    text = ""
    for row in range(len(matrix)):
        text += "\n"
        for column in range(len(matrix[0])):
            if matrix[row][column] == ' ':
                text += "   "
            else: 
                text += matrix[row][column]
    return text

def creator(height, width, default_space):
    mat = []
    for row in range(height):
        mat.append([])
        for column in range(width):
            mat[row].append(default_space)
    return mat