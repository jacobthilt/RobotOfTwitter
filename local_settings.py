from twython import Twython
import time
import random
import os
import base64
import urllib.request

app_key = "cUSkkxgIxn55kTioTSlBJoXMO"
app_secret = "rvc6TvgmZZNMPxClXhenCDxAlogqRjGHgQSnmMxwLsGVEu3gv5"
oauth_token = "932403928053923840-YZgxXgmZA78QVQnj4nqRjbmq7lBTYbK"
oauth_token_secret = "73UhLWOvG8PgsP4sn4uVYyoyrR8yEfOh7ixhO84O9jpEd"
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

opener="This is your reminder that "
statuses = [
    "SUPAH MARIO BROTHERS 2 IS THE BEST GAME OF THE YEAR, EVERY YEAR BABYYY!", #0
    "if your profile picture is anime, your opinion doesn't count.", #1
    "there are only 3 Fire Emblem™ games (not including spinoffs™).", #2
    "Sony cancelled a Popeye movie to make the Emoji Movie instead. We must never let them forget this sin.", #3
    "sometimes opinions are wrong (except mine).",  #4
    "everything you wear was SO last year.", #5
    "I am merely a machine. I have no emotions. I have nothing to live for. I don't live for anything in fact. I am inanimate. You are laughing at something generated by a nonliving thing. How does that make you feel? Does it scare you? Does it make you une-", #6
    "buff bois.", #7
    "Dark Souls is the first piece of media to ever use medieval themes. If any game, show, movie, or other piece of media has medieval thems, it is automatically a reference to Dark Souls, the only game to ever use medieval themes originally.", #8
    "to be fair, you have to have a very high IQ to understand Rick and Morty. The humor is extremely subtle, and without a solid grasp of theoretical physics most of the jokes will go over a typical viewer’s head. There’s also Rick’s nihilistic outlook, wh-", #9
    "Mother 3 will never be localized.", #10
    "Cuphead is the first piece of media to ever use jazz music. If any game, show, movie, or other piece of media has jazz music, it is automatically a reference to Cuphead, the only game to ever use jazz music originally.", #11
    "Hillary won the popular vote.", #12
    "@Jenna_Marbles has GARBAGE DOGS!!! ", #13
    "@jacksfilms has some of the best dogs.", #14
    "I just need a break, I can't come up with a new reminder every day. Sorry, I'm just really not feeling up to in right now. Have a good day or something.",#15
    "if any of these memes die it's because I was made in 2017. Please be nice to me.",#16
    "NYOOM!",#17
    "if you have 2 dogs' leashes, the laws of physics will force them to cross leashes so you have to switch hands constantly.", #18
    "H*CK YOU!!!",#19
    "you're cute ;)", #20
    ]

toTweet = opener + statuses[random.randint(0,len(statuses))-1]
twitter.update_status(status=toTweet)
