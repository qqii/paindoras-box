#!/usr/bin/python3

import pygame
import os
from random import choice
#light push sad shake

class Scream:

    def __init__(self):
        print("Initialising Sound")
        # sound
        self.mixer = pygame.mixer
        self.mixer.init()
        self.mixer.music.set_volume(0.1)
        for d in ["light", "push", "sad", "shake"]:
            for f in os.listdir(d):
                self.mixer.music.load(d+"/"+f)

    def light(self):
        if not self.mixer.music.get_busy():
            self.mixer.music.load("light/" + choice(os.listdir("light")))
            self.mixer.music.play()

    def push(self):
        if not self.mixer.music.get_busy():
            self.mixer.music.load("push/" + choice(os.listdir("push")))
            self.mixer.music.play()

    def sad(self):
        if not self.mixer.music.get_busy():
            self.mixer.music.load("sad/" + choice(os.listdir("sad")))
            self.mixer.music.play()

    def shake(self):
        if not self.mixer.music.get_busy():
            self.mixer.music.load("shake/" + choice(os.listdir("shake")))
            self.mixer.music.play()



    def scream(self, music="sound/tone.wav"):
        if not self.mixer.music.get_busy():
            self.mixer.music.load(music)
            self.mixer.music.play()

if __name__ == "__main__":
    screamer = Scream()
    screamer.scream()
    while screamer.mixer.music.get_busy():
        continue
    screamer.light()
    while screamer.mixer.music.get_busy():
        continue
    screamer.push()
    while screamer.mixer.music.get_busy():
        continue
    screamer.sad()
    while screamer.mixer.music.get_busy():
        continue
    screamer.shake()
    while screamer.mixer.music.get_busy():
        continue
