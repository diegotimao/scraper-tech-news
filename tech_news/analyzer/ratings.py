from tech_news.database import db


# Requisito 10
def top_5_news():

    for i in db.news.find():
        print(i)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
