import speech_recognition as sr
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

def set_voice():
    voices = engine.getProperty('voices')
    # Set the voice to a male voice (0 is usually male on many systems)
    for voice in voices:
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def respond(command):
    if "hello" in command:
        return "Hey, Lishang Gajendra; How can I assist you today?"
    elif "your name" in command:
        return "I am a simple AI chatbot created to assist you."
    elif "how are you" in command:
        return "I'm just a program, but thanks for asking!"
    elif "bye" in command:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

def main():
    set_voice()  # Set the voice to male
    print("Chatbot is ready! You can start talking to it.")
    speak("Hey, Lishang Gajendra; How can I assist you today?")
    
    while True:
        command = listen()
        if command:
            response = respond(command)
            speak(response)
            if "bye" in command:
                break

if __name__ == "__main__":
    main()

