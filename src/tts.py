#!/usr/bin/python3

from gtts import gTTS
import os

from scream import Scream

def main():
    screamer = Scream()
    tts = gTTS(text='Fuck Kenny', lang='en')
    print(tts)
    tts.save("sound/good.mp3")
    screamer.scream(music="sound/good.mp3")
    while screamer.mixer.get_busy():
        continue






if __name__ == "__main__":
    main()
