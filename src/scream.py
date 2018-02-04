#!/usr/bin/python3

import pygame

class Scream:

    def __init__(self):
        # sound
        self.mixer = pygame.mixer
        self.mixer.init()
        self.mixer.music.set_volume(0.1)
        self.mixer.music.load("sound/tone.wav")

    def scream(self, music="sound/tone.wav"):
        if not self.mixer.music.get_busy():
            self.mixer.music.load(music)
            self.mixer.music.play()

if __name__ == "__main__":
    screamer = Scream()
    screamer.scream()
    while screamer.mixer.music.get_busy():
        continue
