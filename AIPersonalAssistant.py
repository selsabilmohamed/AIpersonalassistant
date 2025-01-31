import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import datetime
import wikipedia
import requests
import json
import random

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")
        return command.lower()

# Function to get weather information
def get_weather():
    api_key = "your_api_key_here"  # You need to get an API key from a weather service like OpenWeatherMap
    location = "New York"  # You can set a default location or ask the user for one
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data['cod'] == 200:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        speak(f"The current temperature in {location} is {temp}°C with {description}.")
    else:
        speak("Sorry, I couldn't get the weather information.")

# Function to tell a joke
def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I asked the librarian if the library had any books on paranoia. She whispered, 'They're right behind you.'",
        "Why don't some couples go to the gym? Because some relationships don't work out."
    ]
    joke = random.choice(jokes)
    speak(joke)

# Function to perform basic actions
def execute_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
    
    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        kit.playonyt(song)  # Play on YouTube
    
    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query} on Wikipedia")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    
    elif "reminder" in command:
        speak("What should I remind you about?")
        task = listen()
        speak(f"Reminder set for {task}")
    
    elif "weather" in command:
        get_weather()  # Fetch weather information
    
    elif "joke" in command:
        tell_joke()  # Tell a joke
    
    elif "how are you" in command:
        speak("I am just a program, but I'm doing great! How can I help you today?")
    
    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
def main():
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        command = listen()
        if "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        execute_command(command)

if __name__ == "__main__":
    main()
