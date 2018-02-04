#!/usr/bin/python3

from scream import Scream
from gtts import gTTS
import re#eeeeeeeeeeeeeee normie get out of my python script
import os

class TTS:
    def __init__(self):
        print("Loading TTS")
        dot = re.compile("\.")
        self.screamer = Scream()
        self.phrases = {dot.split(f)[0]: self.screamer.Sound(f) for f in os.listdir("phrases")}
        

    def tts(self, sentence, lang="en"):
        if not sentence in phrases:
            tts = gTTS(sentence, lang)
            tts.save("phrases/"+sentence+".mp3")
            self.phrases[sentence] = self.screamer.Sound("phrases/"+sentence+".mp3")
        self.screamer.speach("phrases/"+sentence+".mp3")
            
if __name__ == "__main__":
    tts = TTS()
    texts = ["This is some text", "This is also some text"]
    for text in texts:
        tts.tts(text)
