from vosk import Model,KaldiRecognizer
from time import sleep
from playsound import playsound
from gtts import gTTS
from os import remove
import pyaudio
import json

#Extras

#Speech Recognition
model=Model('model')
recognizer = KaldiRecognizer(model,16000)
capture = pyaudio.PyAudio()
stream =capture.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()


#Text To Speech
def say(A):
    tts=gTTS(A,lang='en')
    tts.save('temp.mp3')
    playsound('temp.mp3')
    remove('temp.mp3')


#Commads
cmd=[
    {'words':'','ans':''},
    {'words':'hello','ans':"hi"},
    {'words':'time','ans':'11 44'},    
    {'words':'how are you','ans':"great"},
    {'words':'what your name','ans':'I dont have a name'}
]

def check(A):
    score=[0]*len(cmd) 
    for i in A:
        for j in range(len(cmd)):
            words=cmd[j]['words'].split(' ')
            if i in words:
                score[j]+=1
    max=0
    for i in range(len(score)):
        if score[i]>max:
            max=i
    return cmd[max]['ans']


# Main Infinate Loop
while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        r=json.loads(recognizer.Result())['text'].split(" ")
        if r==['exit']:
            break
        ans=check(r)
        print(ans) 
        # say(ans)

