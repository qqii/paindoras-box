#!/usr/bin/python3

from gtts import gTTS
import os

from scream import Scream

def main():
    screamer = Scream()
    tts = gTTS(text='Good morning', lang='en')
    tts.save("sound/good.wav")
    screamer.scream(music="sound/good.wav")





if __name__ == "__main__":
    main()
