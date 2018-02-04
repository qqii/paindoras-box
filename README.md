# Paindora's Box

A box that feels pain, a 24 hour hackathon project.

* bees MAKE-ATHON 2018

## Getting Started

### Hardware

* Raspberry Pi (made for Pi 3 Model B) and power source 
* Enviro pHat
* Speaker

1. [Souder the Enviro pHAT](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats) 

### System

1. [Install NOOBS (to then install Raspbian)](https://www.raspberrypi.org/help/noobs-setup/2/)
1. Enable I2C
1. Enable SSH (for your own sake)
1. Set the speaker to the default sound device
1. Reboot

### Libraries

1. `sudo apt-get install python3-envirophat`
1. `sudo apt-get install python3-numpy` (already installed)
1. `sudo apt-get install python3-pygame` (already installed)
1. `pip3 install sklearn`
1. `pip3 install python-twitter`
1. Obtain twitter api keys and create a file called `secret.py` in the following format

```
consumer_key="xxx"
consumer_secret="xxx"
access_token_key="xxx"
access_token_secret="xxx"
```

### Installing

1. `git clone https://github.com/qqii/paindoras-box/`

## Usage

### `scream.py`

`Usage: ./scream.py`

Plays the screaming sound.

### `shout.py`

`Usage: ./shout.py`

Tweets a message to [@robot_screaming](https://twitter.com/robot_screaming).

### `classifier.py`

```
Usage:
  ./classifier.py train (shaking|still)
  ./classifier.py classify x y z
```

Currently classifies acceleration data into the class "violent" and "non violent".

### `sensors.py`

`Usage: ./sensors.py (delay)`

Polls acceleration and light sensor every delay seconds. Replace this with your implementation if you have a different sensor kit. 

### `main.py`

`Usage: ./main.py [delay]`

Creates life, with a default polling delay of 0.1s.

## Contributing

Don't. Just don't.

## Acknowledgments

* [RcColes](https://github.com/rccoles) for the initial idea.
* [AnthonyWharton](https://github.com/anthonywharton) for absolutely nothing.
* [qqii](https://github.com/qqii) for expanding the initial idea and making it a reality.
* [alessio-b-zak](https://github.com/alessio-b-zak) for making it a reality.
