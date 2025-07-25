import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def scrape_confluence_docs(start_url, max_depth=2):
    visited = set()
    docs = []

    def crawl(url, depth):
        if depth > max_depth or url in visited or "pdf" in url:
            return
        visited.add(url)

        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            docs.append({'url': url, 'text': text})

            # follow only Atlassian Confluence links
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if "confluence.atlassian.com" in full_url:
                    crawl(full_url, depth + 1)
        except Exception as e:
            print(f"Failed {url}: {e}")

    crawl(start_url, 0)
    return docs
