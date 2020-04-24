import lightResponse
import Tweet
import givequote
from gtts import gTTS
from playsound import playsound
import os
import time
import pyttsx3
import covid
import polly
import subprocess
import numberConversion
from termcolor import colored, cprint
import startservices 


def boot():
    
    #getOS()
    #time.sleep(1)
    #os.remove("speech.mp3")
    #welcome()
    #time.sleep(1)
    #givequote.getQuote()
    #os.remove("speech.mp3")
    #getCOVID()
    os.remove("speech.mp3")
    polly.synthesize("Main boot complete, starting twitter and spotify services")


    

def getOS():
    version = 1.21
    #playsound('ding.wav')        
    polly.synthesize("Booting CarbonOS version" + str(version))


def welcome():
    polly.synthesize("Welcome Jack")


def getCOVID():
    time.sleep(5)
    #playsound('ding.wav')
    print('--------')
    cprint(covid.getConfirmed(), 'red')
    cprint(covid.getRecovered(), 'red')
    print('--------')
    polly.synthesize("By the way, right now there is " + numberConversion.getConfirmed() + "confirmed cases, and" + numberConversion.getRecovered() + "recovered cases reported this hour, you should probably be inside")


def startSpotifyService():
    os.remove("speech.mp3")
    polly.synthesize("Spotify started")
    subprocess.call(r'creds.bat')
    
    subprocess.call(lightResponse.lights())

def startTwitterService():
    os.remove("speech.mp3")
    polly.synthesize("Twitter started")
    Tweet.Bot().get_last_tweet()  

boot()

