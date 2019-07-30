import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def readstory():
    storyName = int(input("Enter the no of the Story you want to listen to :  "))
    if storyName == 1:
        f = open("the_gift_of_magi.txt")
        f1 = f.readlines()
    elif storyName == 2:
        f = open("a_dead_womens_secret.txt")
        f1 = f.readlines()
    elif storyName == 3:
        f = open("the_cask_of_amontillado.txt")
        f1 = f.readlines()
    elif storyName == 4:
        f = open("after_twenrty_years.txt")
        f1 = f.readlines()   
    for x in f1:
        speak(x)

print('''List of stories:
1. The Gift of Magi
2. A Dead Woman's Secret
3. The Cast of Amontillado 
4. After Twenty Years''')
readstory()


