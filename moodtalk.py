# MoodTalk
# A baby chatbot made while learning python


N= input("ENTER YOUR NAME: ")

A= input(f"Hello,{N}! How are you feeling? Happy, Sad, Angry, Bored?    ").lower()
if A== "happy":
        print("That sounds great! Make sure to make someone happy too.")
elif A== "sad":
             print("You are allowed to feel that way. Unlike me, you are a human after all. Watch an ASMR with personal attention on YouTube.") 
elif A== "angry":
             print("Do one thing for me. Take a blank piece of paper and pen. Then, start doodling. Get it all out on that paper. If I were a human, it might have worked for me.")
elif A== "bored":
             print("You can take a nap. However, if you wish to feel something...Let's say that you want to be traumatized, go watch The Mist (2007).")

else:
    print("I do not recognize that. I am just a baby chatbot. Please choose from those four options above.")  