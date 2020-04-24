

import random
from gtts import gTTS
from playsound import playsound
import os
import polly
import os


def getQuote():
    os.remove("speech.mp3")
    lines = open('quotes.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
    polly.synthesize(myline)
