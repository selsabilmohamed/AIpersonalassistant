import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import datetime
import wikipedia

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
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    
    elif "reminder" in command:
        speak("What should I remind you about?")
        task = listen()
        speak(f"Reminder set for {task}")
    
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
