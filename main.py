import speech_recognition as sr
import webbrowser
import gtts
import musicLibrary
import requests
import ai_integration
import cowsay
import os
import pygame
import config

newsapi = config.config["news_api_key"]

username = os.getlogin()

recognizer = sr.Recognizer()


def speak(text):
    tts = gtts.gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processCommand(c):
    print(c)

    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    
    elif ("open twitter" or "open x") in c:
        webbrowser.open("https://x.com/?lang=en")
    
    elif "open github" in c:
        webbrowser.open("https://github.com/")
    
    
    elif c.startswith("play"):

        try:
            music = c.split(" ")[1]
            link = musicLibrary.music[music]
            webbrowser.open(link)
        
        except:
            song = c.split(" ", 1)[1]

            song = song.split(" ")

            song = "+".join(song)

            link = f"https://www.youtube.com/results?search_query={song}"

            webbrowser.open(link)
    
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")

        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article["title"])
    
    elif ("greet" or "greet me") in c:
        cowsay.cow(f"Hello, {username}")
        speak(f"Hello, {username}")

    else:
        chatbot_response = ai_integration.get_chatbot_response(c)
        speak(chatbot_response)
        print(chatbot_response)     


def main():
    speak("Initializing Sky....")

    while True:

        # Listen for wake word "Sky"
        # obtain audio from the microphone

        r = sr.Recognizer()

        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            
            print("Recognizing....")
            word = r.recognize_google(audio)

            if "sky" in word.lower():
                speak("Ya")

            # Listen for command
                with sr.Microphone() as source:
                    print("Sky Active....")
                    print("Listening....")
                    audio = r.listen(source, timeout=1, phrase_time_limit=3)

                command = r.recognize_google(audio)            
                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

        

if __name__ == "__main__":
    main()
    