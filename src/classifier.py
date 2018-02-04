#!/usr/bin/python3

import os
import numpy
from sklearn.naive_bayes import GaussianNB

def calculate_jerk(accel1, accel2, delta_t):
    pass
    

class Classifier:
    light_threshold = 100

    def __init__(self):
        self.classifier = None

    def train(self, training_type):
        if os.path.isfile("training_data_" + training_type + ".npy"):
            old_data = numpy.load("training_data_" + training_type + ".npy")
            training_data_temp = old_data.tolist()
        else:
            training_data_temp = []
        try:
            while True:
               data = motion.accelerometer()
               training_data_temp.append(numpy.array(acceleration))
               absolute_value = numpy.linalg.norm(acceleration)
               print("|{}| = {}".format(acceleration, absolute_value))
        except KeyboardInterrupt:
            training_data = numpy.array(training_data_temp)
            numpy.save("training_data_" + training_type, training_data)

    def classify(self, data):
        if self.classifier == None:
            shaking_data = numpy.load("training_data_shaking.npy")
            shaking_length = shaking_data.shape[0]
            shaking_labels = numpy.full((shaking_length, 1), 1)

            still_data = numpy.load("training_data_still.npy")
            still_length = still_data.shape[0]
            still_labels = numpy.full((still_length, 1), 2)

            training_data = numpy.concatenate((shaking_data, still_data), axis=0)
            training_labels = numpy.concatenate((shaking_labels, still_labels), axis=0)
            #1 is class label for shaking, 2 is class label for still

            self.classifier = GaussianNB(priors=[0.1, 0.9])
            self.classifier.fit(training_data, training_labels)

        return self.classifier.predict(data);

if __name__ == "__main__":
    import sys

    classifier = Classifier();
    try:
        if sys.argv[1].startswith("train"):
            if sys.argv[2].startswith("shak"):
                classifier.train("shaking")
            elif sys.argv[2].startswith("still"):
                classifier.train("still")
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
