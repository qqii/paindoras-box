#!/usr/bin/python3
import time
import sys
import os.path
import numpy
from sklearn.naive_bayes import GaussianNB
import numpy.linalg
from envirophat import light, motion, weather, leds

shaking = 1
still = 0

location_change_ps = 5
light_threshold = 10

# try:
#     while True:
#         lux = light.light()
#         leds.on()
#         rgb = str(light.rgb())[1:-1].replace(' ', '')
#         leds.off()
#         acc = str(motion.accelerometer())[1:-1].replace(' ', '')
#         heading = motion.heading()
#         temp = weather.temperature()
#         press = weather.pressure()
#         out.write('%f\t%s\t%s\t%f\t%f\t%f\n' % (lux, rgb, acc, heading, temp, press))
#         time.sleep(1)

# except KeyboardInterrupt:
#     leds.off()
#     out.close()

class Paindora:
    def __init__(self, classifier):
        self.shaking = False
        self.lit = False
        self.classifier = classifier
        self.rotated = False

    def check_light(self):
        light_intensity = light.light()
        print("Light intensity is " + str(light_intensity))
        if light_intensity > location_change_ps:
            # print("I have no mouth and I must scream because its too light")
            self.lit = True
        else:
            # print("I am not screaming because of light")
            self.lit = False

    def check_shaking(self):
        x, y, z = motion.accelerometer()
#        absolute_value = numpy.linalg.norm(numpy.absolute([x,y,z]))
        test_array = numpy.array([x,y,z])
        topredict = test_array.reshape(1, -1)
        print(self.classifier.predict(topredict), x, y, z)
        if self.classifier.predict(topredict) == [1]:
            # print("I have no mouth and I must scream because I'm moving too fast")
            self.shaking = True
        else:
            self.shaking = False
            # print("I am not screaming because of movement")

    def scream(self):
        pass

def motion_classifier():
    shaking_data = numpy.load("training_data_shaking.npy")
    shaking_length = shaking_data.shape[0]
    shaking_labels = numpy.full((shaking_length, 1), 1)

    still_data = numpy.load("training_data_still.npy")
    still_length = still_data.shape[0]
    still_labels = numpy.full((still_length, 1), 2)

    training_data = numpy.concatenate((shaking_data, still_data), axis=0)
    training_labels = numpy.concatenate((shaking_labels, still_labels), axis=0)
    #1 is class label for shaking, 2 is class label for still

    classifier = GaussianNB(priors=[0.4, 0.6])
    classifier.fit(training_data, training_labels)
    return classifier

def training_motion(training_type):
    if os.path.isfile("training_data_" + training_type + ".npy"):
        old_data = numpy.load("training_data_" + training_type + ".npy")
        training_data_temp = old_data.tolist()
    else:
        training_data_temp = []
    try:
        while True:
           x, y, z = motion.accelerometer()
           training_data_temp.append(numpy.array([x,y,z]))
           absolute_value = numpy.linalg.norm(numpy.absolute([x,y,z]))
           print(str(absolute_value))
    except KeyboardInterrupt:
        training_data = numpy.array(training_data_temp)
        numpy.save("training_data_" + training_type, training_data)

def main(args):
    if args[1] == "training":
        training_motion(args[2])
    elif args[1] == "classify":
        motion_classifier()
    elif args[1] == "detect":
        classifier = motion_classifier()
        paindora = Paindora(classifier)

        while True:
            time.sleep(0.1)
            paindora.check_shaking()

if __name__ == "__main__":
    main(sys.argv)


