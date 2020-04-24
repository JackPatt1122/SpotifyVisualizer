import pyaudio
import numpy as np
import serial
import requests
import json
import sys
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

 # Get the username from terminal
username = '9noygby87o3bifbarxgkswfky'

scope = 'user-read-private user-read-playback-state user-modify-playback-state'

token = util.prompt_for_user_token(username, scope)

sp = spotipy.Spotify(auth=token)


def lights():

    toggle = []

    CHUNK = 2**11
    RATE = 44100

    ardu= serial.Serial('COM5',9600, timeout=.1)

    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                frames_per_buffer=CHUNK)
   

    while(True):


        

        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="#"*int(50*peak/2**16)        

        data = sp.current_playback()
        
        playing = data['is_playing']

        volume = data['device']['volume_percent']

        time = data['item']['duration_ms']

        currentTime = data['progress_ms']

        sound = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(sound))*2
        bars="#"*int(50*peak/2**16)

        if(int(50*peak/2**16) < 1 and currentTime < 2000) and volume != 0:
            ardu.write('b'.encode())

        if(int(50*peak/2**16) >= 1 and volume != 0):
            ardu.write('i'.encode())

        if(currentTime < 500 and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('j'.encode())

        if(playing == True and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('c'.encode())

        if(playing == False and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('b'.encode())

        if(volume < 100 and volume > 75 and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('c'.encode())
            toggle.clear()
            if "on" not in toggle:
                toggle.append("on")
                ardu.write('i'.encode())

        if(volume < 75 and volume > 51 and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('d'.encode())


        if(volume < 50 and volume > 26 and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('e'.encode())


        if(volume < 25 and volume > 0 and  int(50*peak/2**16) < 1 and volume != 0):
            ardu.write('f'.encode())


        if(volume == 0 and  int(50*peak/2**16) < 1):
            ardu.write('g'.encode())

    stream.stop_stream()
    stream.close()
    p.terminate()


def changeVolume(volume):
    sp.volume(volume)

lights()