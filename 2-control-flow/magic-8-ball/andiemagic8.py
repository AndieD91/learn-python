name = "Andie"
question = "Should I go to bed now?"
  
import random
answer = random.randint(1, 13)

if answer == 1:
  answer = "Yes - definitely"
elif answer == 2:
  answer = "It is decidedly so"
elif answer == 3:
  answer = "Without a doubt"
elif answer == 4:
  answer = "Reply hazy, try again"
elif answer == 5:
  answer = "Ask again later"
elif answer == 6:
  answer = "Better not tell you now"
elif answer == 7:
  answer = "My sources say no"
elif answer == 8:
  answer = "Outlook not so good"
elif answer == 9:
  answer = "Very doubtful"
elif answer == 10:
  answer = "Absolutely!"
elif answer == 11:
  answer = "Do you really need to ask? Yes!" 
elif answer == 12:
  answer = "Probably should"  
elif answer == 13:
  answer = "Heck NO!"     
else:
  answer = "Error"               
if name == "":
  print("Question: " + question)
else: 
  print(name + " asks: " + question)  
if question == "":
  print("Please enter your question. I am a Magic 8-Ball, not a mind reader!")
else:
  print("Magic 8-Ball's answer: " + answer)
