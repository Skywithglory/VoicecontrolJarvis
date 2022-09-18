import pyttsx3 # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random
# import pyaudio as pa
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0  and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am your assistant Jarvis, Please tell me What do you want')
def takecommand():
    # It take microphone input from the user  and return string output
    r=sr.Recognizer()
    with  sr.Microphone(device_index=1) as source:
       print('Listening.....')
       r.pause_threshold =.5
       r.enregy_threshold=150
       audio = r.listen(source)
    try:
       print("Recognizing....")
       query=r.recognize_google(audio)
       print(f'User said: {query}\n')
    except Exception as e:
        # print(e)
       # speak('Say that again please..')
       print("Say that again please...")
       return 'None'
    return query
if __name__=="__main__":
    speak('Hello Abhishek')
    wishMe()
    i=0
    while True:
    # if 1:
        query=takecommand().lower()

    # Logic for executing take based an query
        if "wikipedia" in query:
           speak('Searching Wikipedia...')
           query=query.replace('wikipedia',"")
           results=wikipedia.summary(query, sentences=2)
           speak('According to wikipedia')
           print(results)
           speak(results)
        elif 'open youtube' in query:
           webbrowser.open('youtube.com')

        elif 'open google' in query:
           webbrowser.open('google.com')

        elif 'open email' in query:
           webbrowser.open('email.com')

        elif 'play song' in query:
           music_dir="C:\\Users\\Lenovo\\Music\\My music"
           songs=os.listdir(music_dir)
           print(songs)
           n=random.randint(0,(len(songs)-1))
           os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
           strTime=datetime.datetime.now().strftime('%H:%M:%S')
           speak(f'Sir, The time is: {strTime}')

        elif 'open vs code' in query:
           codepath="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)

        elif 'play movie' in query:
           moviepath="E:\\Movie"
           m=os.listdir(moviepath)
           print(m)
           n=random.randint(0, len(m)-1)
           os.startfile(os.path.join(moviepath,m[n]))

        elif 'play video song' in query:
          vmusic='C:\\Users\\Lenovo\\Videos\\4K Video Downloader'
          music=os.listdir(vmusic)
          print(music)
          n=random.randint(0,len(music)-1)
          os.startfile(os.path.join(vmusic,music[n]))
        elif 'open chrome' in query:
            chromepath='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chromepath)
        elif 'open Download folder' in query:
            D_path='C:\\Users\\Lenovo\\Downloads'
            os.startfile(D_path)




# r=sr.Recognizer()
# mic=sr.Microphone(device_index=1)
#
# with mic as source:
#     audio=r.listen(source)
# print(r.recognize_google(audio))
