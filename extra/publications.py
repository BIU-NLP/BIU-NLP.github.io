import hashlib
import json
import os
import re
import time
import urllib
from itertools import chain
from random import randint
from tqdm import tqdm
from urllib.request import urlretrieve, urlopen

CITATION_URL = "/citations?view_op=view_citation&hl=en&user=$USER&citation_for_view=$CITATION"
BASE_URL = "https://scholar.google.co.il"

people = list(chain.from_iterable(list(json.load(open("src/data/people.json")).values())))
scholars = {p["name"]: p["scholarId"] for p in people if "scholarId" in p}

for name, scholar_id in tqdm(scholars.items()):
  print("Crawling", name, scholar_id)

  last_publications_url = BASE_URL + "/citations?hl=en&user=" + scholar_id + "&pagesize=100&view_op=list_works&sortby=pubdate"
  with urlopen(last_publications_url) as f:
    content = str(f.read())

  matches = re.findall(r'data-href=\".*?user=(.*?)&.*?citation_for_view=(.*?)\"', content, flags=re.MULTILINE)
  for user, citation in tqdm(matches):
    link = CITATION_URL.replace("$USER", user).replace("$CITATION", citation)
    local_path = 'extra/publications/' + hashlib.md5(link.encode()).hexdigest() + '.html'
    if not os.path.isfile(local_path):
      print("MISS", user, citation)
      urlretrieve(BASE_URL + link, local_path)
