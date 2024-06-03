import os
import random
import winsound

import speech_recognition
import pyttsx3
import cv2
import pyjokes
import webbrowser


r = speech_recognition.Recognizer()

def SpeakText(command):

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-800000000000)
    engine.say(command)
    engine.runAndWait()

def Listen():

    with speech_recognition.Microphone() as source2:

        r.adjust_for_ambient_noise(source2, duration=1)
        SpeakText("say something")

        audio2 = r.listen(source2)

        try:
            MyText = r.recognize_google(audio2)

        except:
            SpeakText("Didnt recognize voice")
            SpeakText("try again")
            Listen()
            return

        MyText = MyText.lower()

    if MyText == "shut down" or MyText == "shutdown" or MyText == "turn off" or MyText == "turnoff":
        SpeakText("Shutting down computer in 5")
        SpeakText("5")
        SpeakText("4")
        SpeakText("3")
        SpeakText("2")
        SpeakText("1")
        SpeakText("Goodbye")

        os.system('shutdown -s')

    elif MyText == "record video":
        cam = cv2.VideoCapture(0)

        recording = True
        SpeakText("Press escape to stop recording")

        while recording:
            check, frame = cam.read()

            cv2.imshow('video', frame)

            key = cv2.waitKey(1)
            if key%256 == 27:
                break
        cam.release()
        cv2.destroyAllWindows()

    elif MyText == "joke":
        SpeakText(pyjokes.get_joke())

    elif MyText == "search youtube":
        with speech_recognition.Microphone() as source2:
            SpeakText("What video do you want to search?")
            r.adjust_for_ambient_noise(source2, duration=1)
            audio2 = r.listen(source2)
            try:
                video = r.recognize_google(audio2)
            except:
                SpeakText("Didnt recognize voice")
                SpeakText("try again")
                Listen()
                return

            video = video.lower()

        SpeakText("Searching"+video)

        webbrowser.open('http://www.youtube.com/results?search_query='+video)


    elif MyText == "game":
        t = ["rock", "paper", "scissors"]

        player_score = 0
        computer_score = 0

        computer = t[random.randint(0,2)]

        SpeakText("Starting rock paper scissors game.")

        while True:

            with speech_recognition.Microphone() as source2:
                SpeakText("Say rock paper or scissors")
                r.adjust_for_ambient_noise(source2, duration=1)
                audio2 = r.listen(source2)
            try:
                player = r.recognize_google(audio2)
            except:
                SpeakText("Didnt recognize voice")
                SpeakText("Trya again")
                continue
            player = player.lower()

            print(player)
            print(computer)

            if player == computer:
                SpeakText("tie!")
            elif player == "rock":
                if computer == "paper":
                    SpeakText("You lose!"+ computer +"covers"+ player)
                    computer_score +=1
                else:
                    SpeakText("You win!"+ player+ "smashes"+ computer)
                    player_score +=1
            elif player == "paper":
                if computer == "scissors":
                    SpeakText("You lose!"+ computer+ "cut"+ player)
                    computer_score +=1
                else:
                    SpeakText("You win!"+ covers+ "cut"+ computer)
                    player_score += 1
            elif player == "scissors":
                if computer == "rock":
                    SpeakText("You lose..."+ computer+ "smashes"+ player)
                    computer_score +=1
                else:
                    SpeakText("You win!"+ player+ "cut"+ computer)

            else:
                SpeakText("That's not a valid play. Check your spelling!")
            computer = t[random.randint(0, 2)]

            SpeakText("Current Score")
            if player_score < 3 and computer_score < 3:
                if computer_score > player_score:
                    SpeakText("You lose!"+ str(player_score)+ " "+ str(computer_score))
                elif computer_score < player_score:
                    SpeakText("You win!" + str(player_score) + " " + str(computer_score))
                else:
                    SpeakText("Tie!" + str(player_score) + " " + str(computer_score))
            elif player_score >= 3:
                SpeakText("Congatulations you win the game" + str(player_score) + " " + str(computer_score))
                Listen()
                return

            else:
                SpeakText("Oh no you lose the game" + str(player_score)+ " " + str(computer_score))
                SpeakText("Loser")
                Listen()
                return


Listen()

