# Projeto Tech News Scraper

Este é um projeto para criar um scraper que coleta notícias de tecnologia do site da Trybe, armazena essas notícias em um banco de dados MongoDB e oferece funcionalidades para buscar e listar essas notícias.

# Funcionalidades

### Função `fetch`

* A função `fetch` é responsável por fazer uma requisição HTTP ao site da Trybe e obter o conteúdo HTML da página de notícias. Essa função respeita um Rate Limit de 1 requisição por segundo. Se a requisição for bem-sucedida (Status Code 200: OK), ela retorna o conteúdo HTML da resposta. Caso contrário, retorna None.

### Função `scrape_updates`

* A função `scrape_updates` faz o scrape da página inicial do blog da Trybe para obter as URLs das notícias listadas. Ela retorna uma lista de URLs das notícias encontradas. Não inclui a notícia em destaque da primeira página, apenas as notícias dos cards.

### Função `scrape_next_page_link`

* A função `scrape_next_page_link` faz o scrape do HTML da página de novidades para obter a URL da próxima página. Retorna a URL obtida ou None se não encontrar o link da próxima página.

### Função `scrape_news`

* A função `scrape_news` recebe o conteúdo HTML da página de uma única notícia e extrai as informações da notícia para preencher um dicionário. As informações incluem URL, título, data, autor, contagem de comentários, resumo, tags e categoria.

### Função `get_tech_news`

* A função `get_tech_news` busca as últimas n notícias do site da Trybe usando as funções anteriores e as insere no banco de dados MongoDB. Em seguida, retorna essas notícias.

### Função `search_by_title`

* A função `search_by_title` busca notícias por título no banco de dados MongoDB. Recebe um título como entrada e retorna uma lista de tuplas com os títulos e URLs das notícias encontradas.

### Função `search_by_date`

* A função `search_by_date` busca notícias por data no formato AAAA-mm-dd no banco de dados MongoDB. Retorna uma lista de tuplas com os títulos e URLs das notícias encontradas. Lança uma exceção ValueError se a data for inválida.

### Função `search_by_tag`

* A função `search_by_tag` busca notícias por tag no banco de dados MongoDB. Recebe o nome da tag como entrada e retorna uma lista de tuplas com os títulos e URLs das notícias encontradas.

### Função `search_by_category`

* A função `search_by_category` busca notícias por categoria no banco de dados MongoDB. Recebe o nome da categoria como entrada e retorna uma lista de tuplas com os títulos e URLs das notícias encontradas.

### Função `top_5_news`

* A função `top_5_news` lista as cinco notícias mais populares com base no número de comentários. Retorna uma lista de tuplas com os títulos e URLs das notícias.

### Função `top_5_categories`

* A função `top_5_categories` lista as cinco categorias mais populares com base no número de ocorrências. Retorna uma lista de categorias em ordem decrescente de popularidade.


## Instalação

Para instalar as dependências e configurar o banco de dados para o projeto Tech News Scraper, siga estas etapas:

### 1. Instale o Python:

Certifique-se de que você tenha o Python instalado em seu sistema. Você pode verificar a versão do Python com o seguinte comando no terminal:

```bash
python --version
```

Se o Python não estiver instalado, você pode baixá-lo e instalá-lo a partir do site oficial: https://www.python.org/downloads/

### 2. Instale o MongoDB:

Você precisará do MongoDB como banco de dados para este projeto. Você pode instalá-lo seguindo as instruções oficiais de acordo com o seu sistema operacional:

- Para sistemas Windows: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
- Para sistemas macOS: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
- Para sistemas Linux: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

Após a instalação, você pode executar o MongoDB localmente. Por padrão, o MongoDB será executado na porta 27017.

### 3. Clone o repositório:

Clone o repositório do projeto Tech News Scraper do GitHub para o seu computador:

```bash
git clone https://github.com/seu-usuario/tech-news-scraper.git
```

### 4. Navegue para o diretório do projeto:

```bash
cd tech-news-scraper
```

### 5. Crie um ambiente virtual (opcional):

Embora não seja estritamente necessário, é uma boa prática criar um ambiente virtual para isolar as dependências do projeto. Você pode criar um ambiente virtual usando o seguinte comando:

```bash
python -m venv venv
```

Em seguida, ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

### 6. Instale as dependências:

Dentro do diretório do projeto, instale as dependências listadas no arquivo `requirements.txt` usando o seguinte comando:

```bash
pip install -r requirements.txt
```

### 7. Configure as variáveis de ambiente:

Crie um arquivo `.env` no diretório do projeto com as seguintes informações:

```env
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DATABASE=tech_news
```

Isso configura a URI do MongoDB e o nome do banco de dados que o projeto usará. Certifique-se de que a URI esteja correta e aponte para o servidor MongoDB local.

### 8. Popule o banco de dados:

Você pode usar a função `get_tech_news` para popular o banco de dados com notícias. Basta executar o programa principal:

```bash
python tech_news/menu.py
```

Escolha a opção "0 - Popular o banco com notícias" no menu e siga as instruções para inserir a quantidade de notícias que deseja buscar e armazenar no banco de dados.

Agora, o banco de dados está configurado e populado com notícias.

## Executando o Programa

Para executar o programa, você pode importar o módulo `tech_news.menu` e chamar a função `analyzer_menu`. Isso abrirá um menu de opções onde você pode interagir com as funcionalidades do projeto.

```python
from tech_news.menu import analyzer_menu

analyzer_menu()
```

### Função `analyzer_menu`

A função `analyzer_menu` é o menu do programa que permite operar as funcionalidades. Ele exibe um menu de opções e solicita informações necessárias para executar as ações correspondentes.

### Implementação das Funcionalidades do Menu

Quando uma opção do menu é selecionada e as informações necessárias são inseridas, a ação adequada é realizada. Isso inclui popular o banco de dados, buscar notícias por título, data, tag ou categoria, listar as top 5 notícias e listar as top 5 categorias.

## Dependências

Aqui está a lista de dependências especificadas no arquivo requirements.txt para o projeto Tech News Scraper:

```
Copy code
certifi==2021.5.30
charset-normalizer==2.0.4
idna==3.2
parso==0.8.2
ply==3.11
py==1.10.0
pymongo==3.12.0
requests==2.26.0
six==1.16.0
tomli==1.2.1
tomli-w==0.5.2
urllib3==1.26.6
```