import random

# messages and responses
greetings = ["hello", "hi", "greetings", "hola", "sup", "hey", "howdy", "yello", "bonjour", "ciao"]
greetingsResp = ["Hi there", "Howdy there", "Greetings"]

questions = ["what's up", "how are you", "how goes it", "how are you doing"]
questionResp = ["Just talking with you !", "Busy", "Nothing much", "I am doing well"]

statements = ["cool", "awesome", "narly", "rad"]
statementResp = ["Not really", "For sure", "Alright", "Yup"]

byes = ["bye", "goodbye", "see you later"]

'''
  Displays an intro message to the user
'''
def intro():
  print("**************************")
  print("Welcome to Rowdy Messenger")
  print("**************************")
  print("<<< type \"Bye\" to exit >>>")
  

'''
  Returns a random index in a dictionary
'''
def randIndex(dataList):
  return random.randint(0, len(dataList) - 1)

'''
  Responds to a message recieved from the user.
  If a response pool has more than one response, a
  random response is chosen from the pool.
'''
def respond(message):
    
    if message in greetings:
      i = randIndex(greetingsResp)
      print("Bot: %s" %(greetingsResp[i]))
      
    elif message in questions:
      i = randIndex(questionResp)
      print("Bot: %s" %(questionResp[i]))
      
    elif message in statements:
      i = randIndex(statementResp)
      print("Bot: %s" %(statementResp[i]))
      
    elif message in byes: 
      print("Bot: See ya next time")
      
    else:
      print("Bot: Sorry, I do not understand")
      
'''
  Entry point into application
'''
def main():
  
  intro()
  
  while(True):  
    
    message = input("You: ").lower().strip('.;!?').strip()
    
    respond(message)
    
    if(message == "bye"):
      break
    
main()
    
