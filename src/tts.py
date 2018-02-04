#!/usr/bin/python3

from gtts import gTTS

shake_phrases = ["Stop shaking me", "Put me down", "This hurts", "Why are you doing this to me?"]
push_phrases = ["Stop pushing me", "Leave me alone", "I'm so helpless", ]
light_phrases = ["The light, it burns", "I don't like the outside", "Leave me be please"]
sad_phrases = ["Life is so pointless", "I never do anything right", "This is so tiring", "Why was I created to feel pain?", "Why do I push away everyone who loves me?"]


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

