#!/usr/bin/python3

from gtts import gTTS
from pygame import mixer

shake_phrases = ["Stop shaking me", "Put me down", "This hurts", "Why are you doing this to me?", "Why are you being so violent?", "I beg you, please stop!"]
push_phrases = ["Stop pushing me", "Leave me alone", "Get off me", "I don't appreciate being pushed around", "That hurts", "Ouch! Why did you do that?"]
light_phrases = ["The light, it burns", "I don't like the outside", "Leave me be please", "Let me be alone in the dark, in peace."]
sad_phrases = ["Why did you leave me alone?","Please come back", "I'm so sad by myself", "Why does everyone leave me?", "I'm so alone."]

for shake in shake_phrases:
    print(shake)
    tts = gTTS(shake, "en")
    tts.save("shake/"+shake+".mp3")

for push in push_phrases:
    print(push)
    tts = gTTS(push, "en")
    tts.save("push/"+push+".mp3")


for light in light_phrases:
    print(light)
    tts = gTTS(light, "en")
    tts.save("light/"+light+".mp3")

for sad in sad_phrases:
    print(sad)
    tts = gTTS(sad, "en")
    tts.save("sad/"+sad+".mp3")

mixer.init()

# possibly play all
