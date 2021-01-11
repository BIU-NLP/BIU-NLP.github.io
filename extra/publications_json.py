import html
import json
import os
import re
import re
from collections import Counter
from datetime import datetime


regexs = {
  "authors": "Authors</div><div.*?>(.*?)</div>",
  "date": "Publication date</div><div.*?>(.*?)</div>",
  "journal": "Journal</div><div.*?>(.*?)</div>",
  "abstract": "Description</div><div.*?>.*?>.*?>(.*?)</div>",
}

pubs = {}
pubs_ignore = {"e2ed7e2c0528b1d77c188d0d9779257a.html"}

p_dir = 'extra/publications'
for filename in os.listdir(p_dir):
  if filename in pubs_ignore:
    continue

  f_path = p_dir + '/' + filename

  with open(f_path, "r") as f:

    content = str(f.read())

    try:
      content = html.unescape(content)
    except:
      pass

    matches = re.findall('gsc_vcd_title\".*?href=\"(.*?)\".*?>(.*?)</a>', content)
    if len(matches) > 0:
      link, title = matches[0]

      pub = {
        "id": filename,
        "title": title,
        "url": link,
      }

      for key, regex in regexs.items():
        vals = re.findall(regex, content)
        if len(vals) > 0:
          val = vals[0]
          while "  " in val:
            val = val.replace("  ", " ")
          pub[key] = val

      if "authors" not in pub:
        print("Skipping no authors", f_path)
        continue

      pub["authors"] = [a.replace(",", "") for a in
                        pub["authors"].replace("I Dagan", "Ido Dagan").replace("IDO Dagan", "Ido Dagan").replace(
                          " Ido Dagan", ", Ido Dagan").replace("Dagan, Ido", ", Ido Dagan").split(", ")]

      # if "Reut Tsarfaty" not in pub["authors"] and "Yoav Goldberg" not in pub["authors"] and "Ido Dagan" not in pub[
      #   "authors"] and "Amit Moryossef" not in pub["authors"]:
      #   print("Skipping authors", f_path, pub["authors"])
      #   continue

      if "date" in pub:
        d = pub["date"] + "/z"
        for i in range(1, 10):
          d = d.replace("/" + str(i) + "/", "/0" + str(i) + "/")
        pub["date"] = d[:-2]

      pub_key = pub["title"].lower()
      if pub_key in pubs:
        this_title = sum(1 for c in pub["title"] if c.isupper())
        other_title = sum(1 for c in pubs[pub_key]["title"] if c.isupper())
        if this_title > other_title:
          pubs[pub_key] = pub
      else:
        pubs[pub_key] = pub


pubs_list = sorted(pubs.values(), key=lambda p: p["date"] + "/00" if "date" in p else "00", reverse=True)

json.dump(pubs_list, open("src/data/publications.json", "w"))

authors = Counter()
for p in pubs_list:
  for a in p["authors"]:
    authors[a] += 1

# for k, v in authors.most_common():
#   try:
#     print(v, "\t", k)
#   except:
#     pass
