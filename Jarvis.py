import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)
wikipedia.set_lang("pt")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo")
        command = r.recognize_google(audio, language= "pt-BR")
        print("usúario falou: " + command + "\n")
    except Exception as e:
        print(e)
        speak("Não entendi senhor")
        return ""
    return command

if __name__ == "__main__":
    speak("Olá senhor, como posso ajudar?")
    speak("Tudo bem com o senhor?")

    while(True):
        command = getCommand().lower()
        if 'wikipedia' in command:
            command =command.replace("wikipedia", "")
            command =command.replace("proucure na", "")
            command =command.replace("pesquise na", "")

            results = wikipedia.summary(command, sentences=2) 
            speak("De acordo com a wikipédia")    
            speak(results)
        elif 'youtube' in command:
            speak("Abrindo o youtube")
            webbrowser.open("https://www.youtube.com/")
            exit(0)
        elif 'google' in command:
            speak("Abrindo o google")
            webbrowser.open("https://www.google.com/")
            exit(0)
        elif 'tchau' in command:
            speak("Até mais senhor")
            exit(0)

