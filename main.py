import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://rcdb.com/r.htm"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
TOTAL_PAGES = 11

coasters = []

for page in range(1, TOTAL_PAGES + 1):
    params = {"page": page, "ot": 2, "op": 2026}
    response = requests.get(URL, headers=HEADERS, params=params)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    rows = soup.find_all("table")[1].find_all("tr")

    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) < 7:
            continue

        time_tag = cells[6].find("time")

        coasters.append({
            "name": cells[1].get_text(strip=True),
            "park": cells[2].get_text(strip=True),
            "type": cells[3].get_text(strip=True),
            "design": cells[4].get_text(strip=True),
            "status": cells[5].get_text(strip=True),
            "opened": time_tag["datetime"] if time_tag else None,
        })

    print(f"Page {page} done, total so far: {len(coasters)}")
    time.sleep(1)

print(len(coasters))



df = pd.DataFrame(coasters)
df.to_csv("coasters_2026.csv", index=False, encoding="utf-8-sig")

print(df.shape)
print(df.head())