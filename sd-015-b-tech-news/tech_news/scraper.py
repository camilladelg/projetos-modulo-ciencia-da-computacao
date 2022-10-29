import parsel
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css("h2.entry-title a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css("div.nav-links a.next ::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    dictNews = {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": len(selector.css("ol.comment-list li").getall()),
        "summary": "".join(
            selector.css(
                "div.entry-content > p:nth-of-type(1) *::text"
            ).getall()
        ).strip(),
        "tags": selector.css("section.post-tags a::text").getall(),
        "category": selector.css("a.category-style span.label::text").get(),
    }
    return dictNews


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://blog.betrybe.com/"
    news_inserted = []
    quantity = amount

    while quantity >= 1:
        html = fetch(url)
        news_current_page = scrape_novidades(html)
        for new in news_current_page[:amount]:
            news_page = fetch(new)
            news_data = scrape_noticia(news_page)
            news_inserted.append(news_data)
            quantity -= 1

            if len(news_inserted) == amount:
                create_news(news_inserted)
                return news_inserted
        url = scrape_next_page_link(html)
