import speech_recognition as sr
import pyttsx3 # pyttsx3 is a python library that help us to convert text-to-speech.
import webbrowser
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognition = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="Enter Your API"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    # Initializing Pygame, mixer
    pygame.mixer.init()

    # Load Mp3 files
    pygame.mixer.music.load('temp.mp3')

    # Play the Mp3 files
    pygame.mixer.music.play()

    # Keep program running untill music stop playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    OpenAI.api_key = "Enter API keys"
    
    try:
        # Attempt to use gpt-4
        completion = OpenAI.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Google and Alexa. Give short responses."},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message['content']

    except OpenAI.error.OpenAIError as e:
        if "insufficient_quota" in str(e):
            return "I'm sorry, I have reached the usage quota for responses. Please check back later or upgrade the plan."
        else:
            raise e
    
    except OpenAI.error.RateLimitError:
        return "I'm sorry, I have reached the usage quota for responses. Please check back later or upgrade the plan."
    except OpenAI.error.APIError as e:
        return f"An API error occurred: {e}"
    except OpenAI.error.InvalidRequestError as e:
        return f"An invalid request error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def processCommand(c):
    if "Open Google" in c.lower():
        webbrowser.open("https://www.google.com/")
        speak("Google Opened!")
    elif "Open YouTube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("YouTube Opened!")
    elif "Open LinkedIn" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
        speak("LinkedIn Opened!")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey="API Keys" = [newsapi]")
        
        if r.status_code == 200:
            # Parse JSON response
            data = r.json()
            # Extract articles
            articles = data.get('articles',[])
            
            # Read the headlines one by one
            for article in articles:
                speak(article['title'])
    else:
        # Let OpenAI handle requests   
        # pass
        output = aiProcess(c)
        speak(output)


if __name__ == '__main__':
    speak("Initializing jarvis...")
 
    while True:
        # Listen for wakeup words "jarvis"
        # Obtain audio from microphone
        r = sr.Recognizer()
        
        # recognize speech using Google/Sphinx
        print("Recognizing jarvis...")
        try:
            with sr.Microphone() as source:
                print("Litening jarvis...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            command = r.recognize_google(audio)
            # command = r.recognize_sphinx(audio)

            if(command.lower() == "jarvis"):
                speak("Yes, How can I Assist You ?")

                # Listen/Waiting for Command
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print(f"Error; {str(e)}")
            print(" ")
