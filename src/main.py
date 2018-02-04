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
        self.previous_accel = numpy.array([0,0,0])

    def start(self):
        try:
            while True:
                x, y, z = self.sensors.acceleration()
                # light = self.sensors.light()

                # pain = False
                # pain |= light > self.classifier.light_threshold
                # print("Pain after light is", pain)
                temp_array = numpy.array([x,y,z])
                print(classifier.calculate_jerk(temp_array, previous_accel, delay))
                #if self.classifier.classify(temp_array.reshape(1, -1)) == [1]:
                #    pain = True
                #print("Pain after motion is", pain)
                #if pain:
                #    self.screamer.scream()
                #    #self.shouter.shout("I'm in pain")

                time.sleep(self.delay)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    import sys

    screamer = Scream()
    shouter = Shout()
    classifier = Classifier()
    sensors = Sensors()

    try:
        delay = float(sys.argv[1])
    except (ValueError, IndexError):
        delay = 0.1

    paindoras_box = Paindora(screamer, shouter, classifier, sensors, delay)
    paindoras_box.start()
