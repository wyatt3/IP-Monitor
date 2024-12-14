from dotenv import load_dotenv
import requests
import os

load_dotenv()

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

    requests.get('https://www.duckdns.org/update?domains=' + os.getenv('DUCK_DNS_DOMAIN') + '&token=' + os.getenv('DUCK_DNS_TOKEN'))

    with open(txt, 'w') as f:
        f.write(r.text)
        f.close()

    message = {
        "content": "IP address has changed from " + lines[0] + " to " + r.text + "\n IP address updated on DuckDNS.",
        "username": "IP Monitor",
        "avatar_url": "https://i.imgur.com/lCObCxd.gif"
    }
    requests.post(os.getenv('DISCORD_URL'), json = message)
