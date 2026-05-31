from pathlib import Path

import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw"


# ---------------------------------------------------
# URLs To Ingest
# ---------------------------------------------------

URLS = [
    "https://docs.python.org/3/tutorial/controlflow.html",
    "https://fastapi.tiangolo.com/tutorial/",
    "https://git-scm.com/docs/git-commit",
]


# ---------------------------------------------------
# Scraper
# ---------------------------------------------------

def scrape_page(url: str):

    response = requests.get(
        url,
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    # Remove noisy page elements
    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
    ]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    text = text.encode("utf-8", errors="ignore").decode("utf-8")

    # Clean whitespace
    cleaned = "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )

    return cleaned


# ---------------------------------------------------
# Save Scraped Documents
# ---------------------------------------------------

def save_scraped_docs():

    DATA_PATH.mkdir(
        parents=True,
        exist_ok=True,
    )

    for index, url in enumerate(URLS):

        print(f"\nScraping: {url}")

        try:

            text = scrape_page(url)

            file_path = (
                DATA_PATH /
                f"scraped_doc_{index}.md"
            )

            file_path.write_text(
                text,
                encoding="utf-8",
            )

            print(f"Saved: {file_path}")

        except Exception as e:

            print(
                f"Failed to scrape {url}"
            )

            print(e)


# ---------------------------------------------------
# Local Test
# ---------------------------------------------------

if __name__ == "__main__":

    save_scraped_docs()