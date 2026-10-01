# RCDB Roller Coaster Scraper

Scrapes the "New for 2026" roller coaster report from [RCDB](https://rcdb.com/)
and exports the results to a CSV file.

## What it collects

253 coasters across 11 pages, with these columns:
`name`, `park`, `type`, `design`, `status`, `opened`

## Tech

Python, requests, BeautifulSoup (lxml), pandas

## How to run

```bash
pip install -r requirements.txt
python main.py
```

The output is saved as `coasters_2026.csv`.