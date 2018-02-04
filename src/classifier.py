#!/usr/bin/python3

import os
import time
import numpy
import numpy.linalg
from sklearn.naive_bayes import GaussianNB
from sensors import Sensors
from envirophat import light, motion, weather, leds

class Classifier:
    light_threshold = 100

    def __init__(self, delay):
        self.classifier = None
        self.delay = delay

    def train(self, training_type):
        if os.path.isfile("training_data_" + training_type + ".npy"):
            old_data = numpy.load("training_data_" + training_type + ".npy")
            training_data_temp = old_data.tolist()
        else:
            training_data_temp = []
        try:
            last_accel = numpy.array([float(0),float(0),float(0)])
            while True:
                time.sleep(self.delay)
                x,y,z = motion.accelerometer()
                current_accel = numpy.array([x,y,z])
                jerk = self.calculate_jerk(current_accel, last_accel, self.delay) 
                training_data_temp.append(jerk)
#                absolute_value = numpy.linalg.norm(acceleration)
                print("|{}|".format(jerk))
        except KeyboardInterrupt:
            training_data = numpy.array(training_data_temp)
            numpy.save("training_data_" + training_type, training_data)

    def classify(self, data):
        if self.classifier == None:
            shaking_data = numpy.load("training_data_shaking.npy")
            shaking_length = shaking_data.shape[0]
            shaking_labels = numpy.full((shaking_length, 1), 1)

            pushed_data = numpy.load("training_data_pushed.npy")
            pushed_length = pushed_data.shape[0]
            pushed_labels = numpy.full((pushed_length, 1), 3)

            still_data = numpy.load("training_data_still.npy")
            still_length = still_data.shape[0]
            still_labels = numpy.full((still_length, 1), 2)

            training_data = numpy.concatenate((shaking_data, still_data, pushed_data), axis=0)
            training_data = training_data
            training_labels = numpy.concatenate((shaking_labels, still_labels, pushed_labels), axis=0)
            #1 is class label for shaking, 2 is class label for still

            self.classifier = GaussianNB()
            self.classifier.fit(training_data, training_labels)

        return self.classifier.predict(data);

    def calculate_jerk(self, accel1, accel2, delta_t):
        delta_accel = numpy.subtract(accel1, accel2)
        jerk = numpy.divide(delta_accel, delta_t)
#        value = numpy.linalg.norm(jerk) 
#        print(value)
        return jerk


if __name__ == "__main__":
    import sys

    classifier = Classifier(0.1);
    try:
        if sys.argv[1].startswith("train"):
            if sys.argv[2].startswith("shak"):
                classifier.train("shaking")
            elif sys.argv[2].startswith("still"):
                classifier.train("still")
            elif sys.argv[2].startswith("push"):
                classifier.train("pushed")
        elif sys.argv[1].startswith("classify"):
            temp_array = numpy.array([float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])])
            data = temp_array.reshape(1, -1) 
            print(classifier.classify(data))
        else:
           print("Usage:")
           print("\t./{} train (shaking|still)".format(sys.argv[0]))
           print("\t./{} classify x y z".format(sys.argv[0]))
    except IndexError:
        print("Usage:")
        print("\t./{} train (shaking|still)".format(sys.argv[0]))
        print("\t./{} classify x y z".format(sys.argv[0]))
