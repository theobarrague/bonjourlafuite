import os, re, requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

URL = "https://bonjourlafuite.eu.org/"
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

html = requests.get(URL, timeout=30).text
soup = BeautifulSoup(html, "html.parser")
yesterday = (datetime.now() - timedelta(days=1)).date()

for e in soup.select(".timeline-entry"):
    t = e.select_one(".timestamp time")
    d = datetime.strptime(" ".join(t["datetime"].split()[:4]), "%a %b %d %Y").date()

    if d != yesterday:
        continue

    h2 = BeautifulSoup(str(e.select_one("h2")), "html.parser")
    a = h2.select_one("a")
    if a:
        a.decompose()

    organization = re.sub(r"^[^\wÀ-ÿ]+", "", h2.get_text(" ", strip=True).replace("\xa0", " ")).strip()

    stolen_data = [
        re.sub(r"\s+", " ", li.get_text(" ", strip=True).replace("\xa0", " ")).strip()
        for ul in e.select(".timeline-description ul") if not ul.find("a")
        for li in ul.select("li")
    ]

    sources = [
        f"https://bonjourlafuite.eu.org/{a['href']}"
        for ul in e.select(".timeline-description ul") if ul.find("a")
        for a in ul.select("a[href]")
    ]

    content = f"**{d.isoformat()} — {organization}**"

    if stolen_data:
        content += "\n" + "\n".join(f"- {x}" for x in stolen_data)

    if sources:
        content += "\n\nSources:\n" + "\n".join(f"- {s}" for s in sources)

    requests.post(WEBHOOK_URL, json={"content": content[:2000]}, timeout=30).raise_for_status()