import boto3
import os
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
from playsound import playsound
from lightResponse import changeVolume
import serial


def synthesize(text=None):
    
    ardu= serial.Serial('COM5',9600, timeout=.1)
    ardu.write('i'.encode())
    print("Writing")

    polly = boto3.client('polly', region_name='us-east-1',  aws_access_key_id='AKIA22RJAGWBA4KZM3F3', aws_secret_access_key= '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')
    data = polly.describe_voices()

    response = polly.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3', Text = text)

    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    changeVolume(75)
    playsound('speech.mp3')
    changeVolume(100)

    return True
    
