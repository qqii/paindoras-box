#!/usr/bin/python3

from scream import Scream
from shout import Shout
#from let it all out import Let It All out
from classifier import Classifier
from sensors import Sensors

import time
import numpy

class Paindora:
    def __init__(self, screamer, shouter, classifier, sensors, delay):
        self.screamer = screamer
        self.shouter = shouter
        self.classifier = classifier
        self.sensors = sensors
        self.delay = delay

    def start(self):
        try:
            while True:
                acceleration = self.sensors.acceleration()
                light = self.sensors.light()

                pain = False
                pain |= light > self.classifier.light_threshold
                pain |= self.classifier.classify(numpy.array((acceleration, )))

                if pain:
                    self.screamer.scream()
                    self.shouter.shout()

                time.sleep(self.delay)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    import sys

    screamer = Screamer()
    shouter = Shouter()
    classifier = Classifier()
    sensors = Sensors()

    try:
        delay = float(sys.argv[1])
    except ValueError, IndexError:
        delay = 0.1

    paindoras_box = Paindora(screamer, shouter, classifier, sensors, delay)
    paindoras_box.start()
