import requests
import os

discordUrl = "https://discord.com/api/webhooks/"
txt = os.path.dirname(os.path.abspath(__file__)) + '/ip.txt'

with open(txt, 'r') as f:
    lines = f.readlines()
    f.close()

r = requests.get('http://ipv4.icanhazip.com')

if lines[0] != r.text:
    message = {
        "content": "IP address has changed from " + lines[0] + " to " + r.text,
        "username": "IP Monitor",
        "avatar_url": "https://i.imgur.com/lCObCxd.gif"
    }
    requests.post(discordUrl, json = message)

    with open(txt, 'w') as f:
        f.write(r.text)
        f.close()
