from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    dataDB = search_news({"title": {"$regex": f"{title.lower()}"}})
    tuplaList = []
    for data in dataDB:
        tuplaList.append((data["title"], data["url"]))

    return tuplaList


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        dataDB = search_news(
            {
                "timestamp": datetime.strptime(date, "%Y-%m-%d").strftime(
                    "%d/%m/%Y"
                )
            }
        )
        tuplaList = []
        for data in dataDB:
            tuplaList.append((data["title"], data["url"]))
        return tuplaList
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    dataDB = search_news({"tags": {"$regex": f"{tag.lower().capitalize()}"}})
    tuplaList = []
    for data in dataDB:
        tuplaList.append((data["title"], data["url"]))

    return tuplaList


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    dataDB = search_news(
        {"category": {"$regex": f"{category.lower().capitalize()}"}}
    )
    tuplaList = []
    for data in dataDB:
        tuplaList.append((data["title"], data["url"]))

    return tuplaList
