from bs4 import BeautifulSoup
import requests
from pprint import PrettyPrinter
from util import oil_map, Anoint, Oil
import pickle

def scrape_amulet_anoints():
    URL = "https://www.poewiki.net/wiki/List_of_amulet_or_blight_unique_anointments"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.find_all('tbody')
    anoints = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if(len(cols) == 5):
                oils = [oil_map[cols[0]], oil_map[cols[1]], oil_map[cols[2]]]
                anoints.append(Anoint(oils, "Allocates " + cols[3]))
    return anoints

def scrape_ring_anoints():
    URL = "https://www.poewiki.net/wiki/List_of_ring_anointments"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.find_all('tbody')
    anoints = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if(len(cols) == 4):
                oils = [oil_map[cols[0]], oil_map[cols[1]]]
                anoints.append(Anoint(oils, cols[3]))
    return anoints
pp = PrettyPrinter()

anoints = scrape_ring_anoints() + scrape_amulet_anoints()

pickle.dump(anoints, open('anoints.p', 'wb'))