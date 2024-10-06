import requests

discordUrl = "https://discord.com/api/webhooks/"

with open('ip.txt', 'r') as f:
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

    with open('ip.txt', 'w') as f:
        f.write(r.text)
        f.close()
