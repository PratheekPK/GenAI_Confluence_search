import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin

BASE_URL = "https://support.atlassian.com/confluence-cloud/docs/learn-how-confluence-cloud-works/"#"https://support.atlassian.com/confluence-cloud/resources/"#"https://confluence.atlassian.com/alldoc/"
OUTPUT_DIR = "scraped_docs"
CRAWL_DEPTH = 1  # only crawl links listed on this page

def extract_text_from_page(url):
    try:
        #print(f"Scraping: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        #content_div = soup.find("div", {"id": "main-content"})
        #content_div = soup.find("div", {"id": "topic__body"})
        #print(content_div)
        #if not content_div:
        #    return "", url

        text = soup.get_text(separator="\n", strip=True)
        return text, url
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "", url

def get_all_links():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(response.text)
    links = soup.select("a[href]")
    #print(links)
    filtered_links = []

    for link in links:
        href = link['href']
        print(href)
        if href.startswith("/"):
            href = urljoin(BASE_URL, href)
        #print(type(href))
        if "confluence" in href and "/docs/" in href:
        #if "/doc/" in href:
            filtered_links.append(href)
    #print(filtered_links)
    filtered_links = ["https://support.atlassian.com/confluence-cloud/docs/what-is-confluence-cloud/","https://support.atlassian.com/confluence-cloud/docs/learn-about-confluence-cloud-plans/","https://support.atlassian.com/confluence-cloud/docs/confluence-standard/"]
    return list(set(filtered_links))

def save_to_disk(text, idx, url):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = os.path.join(OUTPUT_DIR, f"doc_{idx}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"URL: {url}\n\n{text}")

def scrape_main():
    print("Starting get all links")
    links = get_all_links()
    print("Finishing get all links")
    for idx, link in enumerate(links):
        text, url = extract_text_from_page(link)
        #print(text.strip())
        if text.strip():
            print("Saving to disk now")
            save_to_disk(text, idx, url)
        time.sleep(1)  


