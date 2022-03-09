import requests
import pprint
import re
from util import Anoint, Oil
import pickle
from dotenv import dotenv_values

config = dotenv_values(".env")

THRESHOLD = Oil.OPALESCENT

anoints = []
with open('anoints.p', 'rb') as fh:
    anoints = pickle.load(fh)

anoint_map = {}
for anoint in anoints:
    anoint_map[anoint.effect] = anoint

def get_stash_data(poesessid, league, tab_index, account_name, user_agent):
    URL = "https://www.pathofexile.com/character-window/get-stash-items"
    payload = {
        'accountName': account_name,
        'realm': 'pc',
        'league': league,
        'tabs': 0,
        'tabIndex': tab_index
    }
    cookies = dict(POESESSID=poesessid)
    headers = {
        'user-agent': user_agent
    }
    r = requests.get(URL, params=payload, cookies=cookies, headers=headers)
    return r.json()

pattern = re.compile("(\w Ring)|(\w Amulet)")

pp = pprint.PrettyPrinter(indent=2)

data = get_stash_data(config['POESESSID'], config['LEAGUE'], config['TAB_INDEX'], config['ACCOUNT_NAME'], config['USER_AGENT'])
items = data['items']

enchanted_items = list(filter(lambda item: pattern.search(item['baseType']), items))
item_anoint_mapping = list(map(lambda item: {'item': item, 'anoint': anoint_map[item['enchantMods'][0]]}, enchanted_items))

def filter_threshold(mapping):
    oils = mapping['anoint'].oils
    oils.sort(key=lambda x: x.value)
    return oils[len(oils)-1] >= THRESHOLD

oil_threshold_list = list(filter(filter_threshold, item_anoint_mapping))
finished_items = list(map(lambda mapping: {
    'anoint': mapping['anoint'],
    'item': {
        'x': mapping['item']['x'],
        'y': mapping['item']['y'],
        'baseType': mapping['item']['baseType']
        }
    }, oil_threshold_list))

finished_items.sort(key=lambda mapping: mapping['anoint'].oils[len(mapping['anoint'].oils)-1].value, reverse=True)

print("Found Matches:")

for match in finished_items:
    print(match['anoint'])
    print("On %s at x%s, y%s." % (match['item']['baseType'], match['item']['x'], match['item']['y']))
    print('')