#!/usr/bin/python3

from scream import Scream
from shouter import Shouter
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
                light = self.sensors.light()

                pain = False
                pain |= light > self.classifier.light_threshold
                print("Pain after light is", pain)
                temp_array = numpy.array([x,y,z])

                jerk = classifier.calculate_jerk(temp_array, self.previous_accel, delay)
                jerk = jerk.reshape(1, -1)
                print(self.classifier.classify(jerk))
                if self.classifier.classify(jerk) == [1]:
                    pain = True
                elif self.classifier.classify(jerk) == [3]:
                    pain = True
                if pain:
                    self.screamer.scream()
                    #self.shouter.shout("I'm in pain")

                time.sleep(self.delay)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    import sys

    screamer = Scream()
    shouter = Shouter()
    sensors = Sensors()

    try:
        delay = float(sys.argv[1])
    except (ValueError, IndexError):
        delay = 0.1

    classifier = Classifier(delay)
    paindoras_box = Paindora(screamer, shouter, classifier, sensors, delay)
    paindoras_box.start()
