#!/usr/bin/python3
import time
import numpy
import numpy.linalg
from envirophat import light, motion, weather, leds

out = open('enviro.log', 'w')
out.write('light\trgb\tmotion\theading\ttemp\tpress\n')

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
    def __init__(self):
        self.shaking = False
        self.lit = False
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
        absolute_value = numpy.linalg.norm(numpy.absolute([x,y,z]))
        print(str(absolute_value))
        if absolute_value > location_change_ps:
            # print("I have no mouth and I must scream because I'm moving too fast")
            self.shaking = True
        else:
            self.shaking = False
            # print("I am not screaming because of movement")

    def scream(self):
        pass


def main():
    paindora = Paindora()
    while True:
        time.sleep(0.1)
        paindora.check_light()
        paindora.check_shaking()

if __name__ == "__main__":
    main()
