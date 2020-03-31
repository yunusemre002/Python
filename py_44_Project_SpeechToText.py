# Requires PyAudio and PySpeech for Win10 do in Terminal:
#          pip install pipwin
#          pipwin install pyaudio
import speech_recognition as sr
from os import system as komut

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

flag = False
try:
    text = r.recognize_google(audio, language="tr")    # Dili silersen algılamaya çalışır biz boşa uğraşma tr dedik.
    text = text.lower()
    print("Algılanan : " + text)
    flag= True
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if flag:
    if text ==  "chrome'u aç":
        komut("start chrome")
