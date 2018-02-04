#!/usr/bin/python3

from gtts import gTTS

shake_phrases = ["Stop shaking me", "Put me down", "This hurts"]
push_phrases = ["Stop pushing me", "Leave me alone", "I'm so helpless"]
light_phrases = ["The light, it burns", "I don't like the outside", "Leave me be please"]
sad_phrases = ["Life is so pointless", "I never do anything right", "This is so tiring"]

for shake in shake_phrases:
    tts = gTTS(shake, "en")
    tts.save("shake/"+shake+".mp3")

for push in push_phrases:
    tts = gTTS(shake, "en")
    tts.save("push/"+push+".mp3")


for light in light_phrases:
    tts = gTTS(light, "en")
    tts.save("light/"+light+".mp3")

for sad in sad_phrases:
    tts = gTTS(sad, "en")
    tts.save("sad/"+sad+".mp3")

