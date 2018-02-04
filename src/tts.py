#!/usr/bin/python3

from gtts import gTTS
import os

from scream import Scream

def main():
    screamer = Scream()
    tts = gTTS(text='Good morning', lang='en')
    tts.save("sound/good.mp3")
    screamer.scream(music="sound/good.mp3")





if __name__ == "__main__":
    main()
