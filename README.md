
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=PYTIMAO%20POR&message=bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center"> PYTIMAO </p> </h3>
<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> <i> O pyTimão </i> é uma ferramenta indispensável para todos os torcedores fanáticos do Corinthians que querem acompanhar as últimas novidades sobre o time.
Com esta biblioteca você pode obter informações sobre todos os jogadores do time e informações sobre contrato, idade, posição de cada jogador.
Então, se você é um torcedor do Corinthians que não aguenta mais ter que passar horas navegando pelo na internet em busca de informações sobre seus jogadores favoritos, não perca mais tempo e instale o <i> O pyTimão </i>  agora mesmo! Com esta ferramenta poderosa e divertida, você nunca mais perderá uma notícia importante sobre o seu time do coração! </p>

>> <h3> How install </h3>

```

pip install pyTimao


```

>> <h3> How Works </h3>

```

from pyTimao import *

##  instanciando o script ###
scraper = MeuTimaoScraper()

## Obtendo todos os jogadores atuais do corinthians ##

jogadores = scraper.allPlayers()
print(jogadores)

### Obtendo todos jogadores de uma determinada posição ####
goleiros = jogadores['Goleiros']

### Obtendo informações de um determinado jogador ####
primeiro_goleiro_url = goleiros[0]['url']
info_primeiro_goleiro = scraper.infoPlayer(primeiro_goleiro_url)

```
    