import requests
from parsel import Selector
import time
from tech_news.database import create_news


# Requisito 1

def fetch(url):
    try:
        time.sleep(1)
        headers = {"User-Agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        print(response)  # Adicionando esta linha para imprimir o objeto de resposta HTTP

        if response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    list_links = []

    for link in selector.css(".cs-overlay-link::attr(href)").getall():
        list_links.append(link)

    return list_links


# Requisito 3
def scrape_next_page_link(html_content):
    selectors = Selector(text=html_content)

    next_page = selectors.css(".next::attr(href)").get()

    if not next_page:
        return None

    return next_page


# Requisito 4
def scrape_news(html_content):
    selectors = Selector(text=html_content)
    coments = selectors.css("#comments > h5::text").get()
    tags = selectors.css(".post-tags > ul > li > a::text").getall()
    coments_count = ""

    if not tags:
        tags = []

    if not coments:
        coments_count = 0
    else:
        coments_count = coments_count.split(" ")[0]

    return {
        "title": selectors.css(".entry-title::text").get().strip(),
        "timestamp": selectors.css(".meta-date::text").get(),
        "category": selectors.css(".label::text").get(),
        "writer": selectors.css(".author > a::text").get(),
        "tags": tags,
        "comments_count": coments_count,  # problema aqui
        "summary": (
            "".join(
                selectors.css(
                    ".entry-content > p:nth-of-type(1) *::text"
                ).getall()
            ).strip()
        ),
        "url": selectors.css("[rel=canonical]::attr(href)").get(),
    }


# Requisito 5
def get_tech_news(amount):
    list = []
    list_links = []
    url = "https://blog.betrybe.com"

    while len(list_links) <= amount:
        content = fetch(url)
        list_links.extend(scrape_updates(content))

        url = scrape_next_page_link(content)

    for link in list_links[:amount]:
        scrape_page = fetch(link)
        list.append(scrape_news(scrape_page))

    create_news(list)

    return list
