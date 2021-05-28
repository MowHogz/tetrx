from telegram import InlineKeyboardMarkup, InlineKeyboardButton
#2.0.0 - Beta 
# we made some temporary changes (left commented out) used to send the album cover for Beta testing 
from main import download
from snake import snake 
class user:
    def __init__(self,manager, client_info,location , message = " ", admin = False):
        
        self.manager = manager 
        self.admin = admin          #bool
        self.client_info = client_info
        try:    self.name = client_info['first_name']
        except: self.name = "Unknown"

        self.id = client_info['id']
        self.location = location
        self.download = download(self.location)
        
        self.reset()

    def reset(self):
        self.count = 0 

        
        self.board_id = self.send("Good Game!\n Press Right to start again").message_id
        
    def start_new_game(self):
        self.snake = snake(20,20,"Ruby", self)
        self.snake.t.start()

    def send(self, message):
        return self.manager.bot.send_message(self.id, message)
        
    def run(self, message):
        if self.count == 0:
            #first round 
            self.count += 1
            self.another_message = self.send("This messsage should indicate what's going on, I think").message_id
            self.start_new_game()
                

            #self.manager.bot.bot.edit_message_text(
                    #self.snake.d, self.id, self.another_message, reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("←", callback_data='l'), InlineKeyboardButton("↑", callback_data='u'), InlineKeyboardButton("↓", callback_data='d'),InlineKeyboardButton("➜" , callback_data='r') ]]) )
            #self.manager.bot.edit_message_text(text, self.id, self.board_id)
        else: 
            
            self.count += 1
            
            try:
                print ("i got here")
                print (self.snake.d)

                #self.manager.bot.bot.edit_message_text(self.snake.d, self.id, self.another_message)
            except:
                pass
            
            self.snake.direction = message
            #print (self.board_id)
            
            #self.snake.run(message)
            
            
            return "You have accessed the run function of the user, You have done this {} times".format(self.count)
