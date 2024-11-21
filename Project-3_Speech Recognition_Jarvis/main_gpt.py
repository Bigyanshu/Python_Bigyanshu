import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import openai
from gtts import gTTS
import pygame
import os

# Initialize recognizer, text-to-speech engine, and set API keys
recognition = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = "your_openai_api_key"  # Replace with your actual OpenAI API key
newsapi = "your_newsapi_key"  # Replace with your actual NewsAPI key

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    # Initialize Pygame and play the mp3 file
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Keep program running until music stops
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    try:
        # Create a completion using the GPT-3.5-turbo model
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Google and Alexa. Give short responses."},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message['content']

    except openai.error.RateLimitError:
        return "I'm sorry, I've reached the usage quota for responses. Please try again later."
    except openai.error.APIError as e:
        return f"An API error occurred: {e}"
    except openai.error.InvalidRequestError as e:
        return f"An invalid request error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
        speak("Google opened!")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("YouTube opened!")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
        speak("LinkedIn opened!")
    elif c.lower().startswith("play"):
        search_term = c.lower().replace("play", "").strip()
        
        if search_term:
            youtube_search_url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
            webbrowser.open(youtube_search_url)
            speak(f"Playing {search_term} on YouTube.")
        else:
            speak("Please specify what you'd like to play.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit to top 5 headlines
                speak(article['title'])
        else:
            speak("Failed to retrieve news.")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == '__main__':
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Waiting for Wake-up word 'Jarvis'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio)

            if command.lower() == "jarvis":
                speak("Yes, how can I assist you?")
                with sr.Microphone() as source:
                    print("Jarvis is active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    # Check if the command is to stop Jarvis
                    if "stop" in command.lower() or "exit" in command.lower():
                        speak("Goodbye!")
                        print("Jarvis is stopping...")
                        break  # Exit the loop to stop the program

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error; {str(e)}")
