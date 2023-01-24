from tech_news.database import db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    list_news = []

    for i in db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": True, "url": True, "_id": False},
    ):
        list_news.append((i["title"], i["url"]))

    return list_news


# Requisito 7
def search_by_date(date):
    try:
        list_news = []
        date_now = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        for i in db.news.find(
            {"timestamp": date_now}, {"title": True, "url": True, "_id": False}
        ):
            list_news.append((i["title"], i["url"]))
        return list_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
