from telegram import KeyboardButton , ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# v2.1 - using official Telegram bot (instead of http api thingy)
# made some changes in the the whole system of getting the user variables
# v2.1.1 - added a 'crash report' ish thingy
from users import user
import time 
import random
from bot import  BotHandler, simple_bot

import datetime
from manager import user_manager
import json
from setup import setter
from telegram import InlineKeyboardButton

welcome_message = """
***Wecome to sample tlg bot"""



    

#get general program info 
location, token, ad_token,admin,back_up_message = setter()


#setting up public bot 
magnito_bot = BotHandler(token) 

#setting up 'admin bot'/alternative bot where the 'alternative' messages are sent from (when sending to admin)
ad_bot = simple_bot(ad_token,default_client=admin)


#let admin know that the bot is booting up 
ad_bot.send("Bot booting up!")

#this class manages the multiple users and also logs (logs still need to work done)
manager = user_manager(magnito_bot,admin = admin, admin_bot=ad_bot, location=location)

#should look like this {id:[first name, lastname]}





def main():
    new_offset = 0
    all_updates=magnito_bot.get_updates(new_offset, timeout = 1) #clears chat until now... #i added added up to 1 sec, cause if there were no messages, it waits for the firts messageto come in and clears it
    
    #now we update all users that had pending messages that the bot is back online (we don't process all of there messages cause it can create a overload on the system, and cause the user may have sent more command then needed since the bot was offline)
    
    updated_users = []                                                                              #users which have already been updated 
    if len(all_updates) > 0:                                                                        #if there is at least one pending update 
        for current_update in all_updates:
            try:                                                          #for every update
                first_chat_id = current_update['message']['chat']['id']                                 #the user
                if first_chat_id not in updated_users:                                                  #hasn't been updated yet 
                    magnito_bot.send_message(first_chat_id, back_up_message)                            #update the user 
                    updated_users.append(first_chat_id)                                                 #add to list of updated_users (cause he is updated ;) )
                    print(str(current_update)+"\n")
                else: pass

                first_update_id = current_update['update_id'] #stuff that i'm not sure what they do 
                new_offset = first_update_id + 1              #if you take this out of the code it will probably not work 
            except:
                print ("Something went wrong with Message:\n{}".format(current_update))

    #print on console and send to user that updates are cleared 
    print ("Cleared updates")
    ad_bot.send("Updates Cleared")

    while True: #for the rest of eternity 
        print("on loop")
        all_updates=magnito_bot.get_updates(new_offset, timeout=2)
        #print(new_offset)
        print ("hello world massage changed timeout")
        if len(all_updates) > 0:                    #when there is an update 
            print ("we got updates and stuff and yonatan massaging")
            for current_update in all_updates:      
                
                if True:                            #try
                    print (current_update)
                    


                    #manage users info into variables 
                    #magnito_bot.logger(current_update)
                    #print(str(current_update)+"\n")
                    print ("beginning to deal with all the paramaters")
                    first_update_id = current_update.update_id
                    
                    
                    #print (current_update['message'])
                    
                    query = False
                    try:
                        print ("0.5")
                        first_chat_text = current_update['message']['text']
                        print ("1")
                        
                    
                    except:
                        print ("for some reason we crashed over here")
                        current_update = current_update['callback_query']
                        first_chat_text='New member'
                        #print ("This is the new stuff \n\n\n")
                        query = current_update['data']
                        
                    
                    first_chat_id = current_update['message']['chat']['id'] #id of sender of current message
                    #print ("got chat id")
                    if  current_update['message']['first_name']:
                        #print ("2")
                        first_chat_name = current_update['message']['chat']['first_name']
                    elif   current_update['message']['new_chat_member']:
                        #print ("3")
                        first_chat_name = current_update['message']['new_chat_member']['username']
                    elif   current_update['message']['from']:
                        #print ("3.5")
                        first_chat_name = current_update['message']['from']['first_name']
                    else:
                        first_chat_name = "unknown"
                        #print ("4")

                    #print (current_update['message']['from'])
                    
                    client_info = current_update['message']['chat']
                    
                    message = current_update['message'] ['text']
                    #print (message)
                    print ("i got here")
                    #print("done dealing with all the parameters")



                    update_info = ("""{}
                    USER:{} ID:{}
                    {}
                     """.format( time.strftime("%d %H:%M:%S") , first_chat_name, first_chat_id, message))

                    #magnito_bot.logger(update_info)
                    #print (update_info)
                    new = False 
                    #if this is a new user
                    #print ("Client Info: {} \n\n\n\n Existing Members:".format(client_info))
                    #print (manager.current_members)
                    if not manager.exists(client_info):

                        print ("adding new user")
                        manager.add_user(client_info, message = message)
                        
                        ad_bot.send("New User! Name:{} ID:{}".format(first_chat_name,first_chat_id))
                        magnito_bot.send_message(first_chat_id,welcome_message)  #activate 
                        new = True

                        count = 0 

                    else:
                        pass

                    #if this is a 'regestered' client proceed with normal stuff normal clients do 
                    #print (client_info)
                    client = manager.current_members[client_info['id']]
                    if new: client.send("This is a Very Beta version of the bot, please be gentle and DM me if you find any bugs :)")
                    else: pass
                    
                    
                    
                    

                    if message.lower() == "bug":
                        #magnito_bot.send_message(first_chat_id, "You have reported a bug ")
                        #magnito_bot.send_message(ruby, "There has been a bug reported buy:{}".format(client_info))
                        #print ("\n\n\nThere has been a bug reported buy:{}\n\n\n".format(client_info))
                        #magnito_bot.refresh_logger()
                        #magnito_bot.log_file.close()
                        #magnito_bot.log_file.open()
                        #manager.log.close()
                        #for user in manager.current_members.values():
                        #    user.refresh_logger()
                        #    user.refresh_tlogger()
                        pass
                        
                    else:
                        if False: #reason to reset user 
                            pass    #reset user and stuff
                        else:

                            butt1 = InlineKeyboardButton("Left" , callback_data='1', )
                            butt2 = InlineKeyboardButton("Right", callback_data='2', )
                            
                            but1 = KeyboardButton("Left")
                            but2 = KeyboardButton("Down")
                            but3 = KeyboardButton("Up")
                            but4 = KeyboardButton("Right")
                            #keyboard = ReplyKeyboardMarkup([[but1, but2, but3, but4]])
                            #keyb = InlineKeyboardMarkup([[butt1,butt2]])
                            
                            
                            #ReplyKeyboardMarkup()
                        
                            
                            #magnito_bot.bot.editMessageReplyMarkup(client.id, client.board_id, reply_markup = InlineKeyboardMarkup([[
                            #    InlineKeyboardButton("Right", callback_data='2'),
                            #    InlineKeyboardButton("Left" , callback_data='1') ]]))
                            
                            
                            #comm = BotCommand("asdf","this")
                            #client.send("Successfully defined asdf ")
                            #magnito_bot.bot.setMyCommands([comm])
                            #client.send("Some More Chocolate")
                            #magnito_bot.bot.setMyCommands([comm])
                            
                            
                            print ("Client info:")
                            print (client.id)
                            if query: 
                                message = query
                            print ("\n\n\n\n\n\n\n\n")
                            print ("message")
                            print (message)
                            client.run(message)

                else:

                    print ("something went wrong at the end of tlg, if you get this message a few times, let me know ")
                new_offset = first_update_id + 1


if True:
    if __name__ == '__main__':
        main()
#except KeyboardInterrupt:
#    print ("The bot has shut down due to Keyboard Interruption ")
#    ad_bot.send("The bot has shut down due to Keyboard Interruption ")
#    exit()
else:
    print ("The bot has shut down due to unknown reasons which probably need investigation")
    ad_bot.send("The bot has shut down due to unknown reasons which probably need investigation")
    exit()