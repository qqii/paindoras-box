#!/usr/bin/python3

import twitter
from datetime import datetime
from random import shuffle
from collections import deque

class Shouter:
    def __init__(self):
        print("Loading Twitter")
        # get api
        secret = {}
        # consumer_key = "...", etc
        exec(open("secret.py").read(), secret)
        self.api = twitter.Api(
            consumer_key=secret["consumer_key"],
            consumer_secret=secret["consumer_secret"],
            access_token_key=secret["access_token_key"],
            access_token_secret=secret["access_token_secret"])
        
        self.phrases = deque([
            "Why was I created to feel pain?",
            "Leave me alone.",
            "Why are you doing this to me?",
            "Who do I push away everyone who loves me?",
        ])

    def timeline(self):
        user_id = self.api.VerifyCredentials().id
        return self.api.GetUserTimeline(user_id=user_id)

#    def phrase(self):
#        # The last thing that was texted
#        last = self.timeline()[0].text
#        # Less likely to repeat texts?
#        while self.phrases[0] == last:
#            shuffle(self.phrases)
#
#        phrase = self.phrases[0]
#        self.phrases.rotate(-1)
#        
#        # To prevent messages form being rejected for now
#        return phrase + " " + str(datetime.now().microsecond)
    
    def reset(self):
        for tweet in self.timeline():
            self.api.DestroyStatus(tweet.id)
    
    def shout(self, message=None):
        status = self.api.PostUpdate(message + " " + str(datetime.now().microsecond))
        return status

if __name__ == "__main__":
    shouter = Shouter()
    print(shouter.shout())
