#!/usr/bin/python3

from envirophat import light, motion, weather, leds

class Sensors:
    def __init__(self):
        pass

    def acceleration(self):
        return motion.accelerometer()

    def light(self):
        return light.light()


if __name__ == "__main__":
    import sys
    import time

    sensors = Sensors()
    try:
        delay = float(sys.argv[1])
        while True:
            print("acceleration = {}\tlight = {}", sensors.acceleration(), sensors.light())
            os.sleep(delay)
    except ValueError:
        print("Usage: ./{} (delay)".format(sys.argv[0]))
    except KeyboardInterrupt:
        pass
