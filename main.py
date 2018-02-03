#!/usr/bin/python3
import time
import numpy
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


#takes a list of x,y,z vectors of acceleration and calculates magnitude
# absolute :: [Int] -> Int
def check_light():
    light_intensity = light.light()
    print("Light intensity is " + str(light_intensity))
    if light_intensity > location_change_ps:
        print("I have no mouth and I must scream because its too light")



#takes a list of x,y,z vectors of acceleration and calculates magnitude
# absolute :: [Int] -> Int
def check_movement():
    x, y, z = motion.acceleration()
    absolute_value = numpy.absolute([x,y,z])
    if absolute_value > location_change_ps:
        print("I have no mouth and I must scream because I'm moving too fast")



if __name__ == "__main__":
    main()