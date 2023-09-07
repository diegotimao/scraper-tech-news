from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories

def analyzer_menu():
    while True:
        print("Selecione uma das opções a seguir:")
        print("0 - Popular o banco com notícias")
        print("1 - Buscar notícias por título")
        print("2 - Buscar notícias por data")
        print("3 - Buscar notícias por tag")
        print("4 - Buscar notícias por categoria")
        print("5 - Listar top 5 notícias")
        print("6 - Listar top 5 categorias")
        print("7 - Sair")

        option = input("Digite o número da opção desejada: ")

        if option == "0":
            amount = int(input("Digite quantas notícias serão buscadas: "))
            get_tech_news(amount)
            print(f"{amount} notícias foram adicionadas ao banco de dados.")

        elif option == "1":
            title = input("Digite o título da notícia: ")
            results = search_by_title(title)
            if results:
                for result in results:
                    print(result)
            else:
                print("Nenhuma notícia encontrada com esse título.")

        elif option == "2":
            date = input("Digite a data no formato AAAA-mm-dd: ")
            try:
                results = search_by_date(date)
                if results:
                    for result in results:
                        print(result)
                else:
                    print("Nenhuma notícia encontrada para a data especificada.")
            except ValueError as e:
                print(f"Erro: {e}")

        elif option == "3":
            tag = input("Digite a tag: ")
            results = search_by_tag(tag)
            if results:
                for result in results:
                    print(result)
            else:
                print("Nenhuma notícia encontrada com essa tag.")

        elif option == "4":
            category = input("Digite a categoria: ")
            results = search_by_category(category)
            if results:
                for result in results:
                    print(result)
            else:
                print("Nenhuma notícia encontrada com essa categoria.")

        elif option == "5":
            results = top_5_news()
            if results:
                for result in results:
                    print(result)
            else:
                print("Não há notícias disponíveis.")

        elif option == "6":
            results = top_5_categories()
            if results:
                for result in results:
                    print(result)
            else:
                print("Não há categorias disponíveis.")

        elif option == "7":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Digite um número válido.")

if __name__ == "__main__":
    analyzer_menu()
