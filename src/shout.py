#!/usr/bin/python3

import twitter


class Shout:

    def __init__():
        # get api
        secret = {}
        # consumer_key = "...", etc
        exec(open("secret.py").read(), secret)
        self.api = twitter.Api(
            consumer_key=secret["consumer_key"],
            consumer_secret=secret["consumer_secret"],
            access_token_key=secret["access_token_key"],
            access_token_secret=secret["access_token_secret"])

    def shout(self, message):
        status = self.api.PostUpdate(message)


if __name__ == "__main__":
    shouter = Shout()
    shouter.shout("I'm sick of being alone")
