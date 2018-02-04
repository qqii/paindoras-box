#!/usr/bin/python3

from gtts import gTTS
from scream import Scream
import re#eeeeeeeeeeeeeee normie get out of my python script
import os

class TTS:
    def __init__(self):
        print("Loading TTS")
        self.re = re.compile("[^a-zA-Z]")
        dot = re.compile("\.")
        self.words = {dot.split(f)[0]: f for f in os.listdir("words")}
        self.screamer = Scream()

    def tts(self, sentence, lang="en"):
        words = self.re.split(sentence)
        for word in words:
            word = word.lower()
            if not word in self.words:
                tts = gTTS(word, lang)
                tts.save("words/" + word + ".mp3")
            self.screamer.mixer.music.set_volume(0.5)
            self.screamer.scream(music="words/" + word + ".mp3")
            while self.screamer.mixer.music.get_busy():
                continue


if __name__ == "__main__":
    tts = TTS()
    texts = ["This is some text", "This is also some text"]
    for text in texts:
        tts.tts(text)
