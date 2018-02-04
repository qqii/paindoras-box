#!/usr/bin/python3

import pygame

class Scream:

    def __init__(self):
        # sound
        self.mixer = pygame.mixer
        self.mixer.init()
        
        self.screaming = self.mixer.find_channel()
        self.screaming.set_volume(0.2)
        self.screamings = [self.mixer.Sound("sound/tone.wav")]
        
        self.speach = self.mixer.find_channel()
        self.speach.set_volume(0.4)

    def scream(self):
        if not self.screaming.get_busy():
            self.screaming.play(self.screamings[0])
            
    def speach(self, file):
        self.speach.queue(sound)

if __name__ == "__main__":
    screamer = Scream()
    screamer.scream()
    while screamer.screaming.get_busy():
        continue
