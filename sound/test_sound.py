#!/usr/bin/python3

import pygame

pygame.mixer.init()
pygame.mixer.music.load("tone.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

