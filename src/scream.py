#!/usr/bin/python3

import pygame
import os
import re#eeeeeeeeeeeeeeeeee normies get out of my python script
from shouter import Shouter
from random import choice
#light push sad shake

class Scream:

    def __init__(self):
        print("Initialising Sound")
        # sound
        self.mixer = pygame.mixer
        self.mixer.init()
        self.shouter = Shouter()
        self.mixer.music.set_volume(0.3)
        
        self.screaming = self.mixer.find_channel()
        self.screaming.set_volume(0.3)

    def emote(self, emotion):
        if not self.mixer.music.get_busy():
            f = choice(os.listdir(emotion))
            print(os.listdir(emotion), f)
            self.mixer.music.load(emotion + "/" + f)
            self.mixer.music.play()
            #self.shouter.shout(re.split("\.", f)[0])

    def scream(self, wav="scream/tone.wav"):
        if not self.screaming.get_busy():
            self.screaming.play(self.mixer.Sound(wav))

if __name__ == "__main__":
    screamer = Scream()
    screamer.scream("scream/aaaa.wav")
    while screamer.screaming.get_busy():
        continue

