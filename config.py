from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBu6zIEZRtoTX7-uFpTUnJhBZkFkDEgXVNH8TSLbLOYKlfVmMMF-GMDlGCCtWwt6quM19tye2bq6L8N3PZRFvhutf_FGkEWNJzevCqijdGLiUGRifmaB7Reuyxnfe7vS26ILobjySLor5Z8KCDtCI-qHMV2tuaTgGBUX6F3eQhMNM-Cj7zD2NgNVgOaJIWSMbJsRrwxWWgRIcStUnVh257PnUwZ09gR0XH6ZsqzljKALoCjHW3hjmi-BYI6pDYvrOxIbsp9XYFMGlXpgEE2Nn7N4c7ecSkpcGHbbA1c2_LkJh-sSLUZRDjzouxqeuOLefI92wzEdGoW2xhX6Cq4wACIqY")
BOT_TOKEN = getenv("5343798470:AAFfBax1Qhib7ZFPebSwaKMzVmC3aGj21zc")
BOT_NAME = getenv("black", "Black") 
API_ID = int(getenv("10318886"))
API_HASH = getenv("8b5e314a1655f64e19bf46083976114f")
BOT_USERNAME = getenv("blackmuzikbot", "blackmuzikbot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("55", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("5306202921").split()))
