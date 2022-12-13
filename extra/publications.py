import hashlib
import json
import os
import re
from itertools import chain

from tqdm import tqdm
from pyppeteer import launch
import asyncio


async def get_page(page, url: str, wait_for: str):
  await page.goto(url)

  try:
    # Throws exception in case of page redirect
    await page.waitFor(wait_for)
  except:
    await page.waitFor(wait_for)

  content = await page.content()
  return content


async def main():
  browser = await launch(headless=False, executablePath=os.getenv('CHROME_EXECUTABLE_PATH'))
  page = await browser.newPage()

  CITATION_URL = "/citations?view_op=view_citation&hl=en&user=$USER&citation_for_view=$CITATION"
  BASE_URL = "https://scholar.google.co.il"

  people = list(chain.from_iterable(list(json.load(open("src/data/people.json")).values())))
  scholars = {p["name"]: p["scholarId"] for p in people if "scholarId" in p}

  for name, scholar_id in tqdm(scholars.items()):
    print("Crawling", name, scholar_id)

    last_publications_url = BASE_URL + "/citations?hl=en&user=" + scholar_id + "&pagesize=100&view_op=list_works&sortby=pubdate"
    content = await get_page(page, last_publications_url, '#gsc_prf_in')

    matches = list(re.findall(r';citation_for_view=(.*?)\"', content, flags=re.MULTILINE))

    for citation in tqdm(matches):
      link = CITATION_URL.replace("$USER", scholar_id).replace("$CITATION", citation)
      local_path = 'extra/publications/' + hashlib.md5(link.encode()).hexdigest() + '.html'
      if not os.path.isfile(local_path):
        page_url = await get_page(page, BASE_URL + link, "#gsc_oci_title")
        with open(local_path, "w", encoding="utf-8") as f:
          f.write(page_url)

  await browser.close()


asyncio.run(main())
