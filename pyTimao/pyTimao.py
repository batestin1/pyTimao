
#############################################################################################################################
#   filename:pyTimao.py                                                       
#   created: 2023-03-09                                                              
#   import your librarys below                                                    
#############################################################################################################################


import requests
from bs4 import BeautifulSoup
import re
import json

class MeuTimaoScraper:
    def __init__(self):
        self.base_url = "https://www.meutimao.com.br/jogadores-do-corinthians/elenco-atual-do-corinthians"

    def allPlayers(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        jogadores = {}
        posicao_atual = None

        # Expressão regular para verificar se o nome do jogador contém apenas letras e espaços em branco
        regex_jogador = re.compile(r'^[a-zA-Z\s]+$')

        for tag in soup.find_all(['li', 'h3']):
            if tag.name == 'li' and tag.has_attr('class') and 'posicao' in tag['class']:
                posicao_atual = tag.text.strip()
                jogadores[posicao_atual] = []
            elif tag.name == 'h3':
                nome_jogador = tag.text.strip()
                url_jogador = tag.find('a', href=True)
                if url_jogador and 'jogador-do-corinthians' in url_jogador['href'] and regex_jogador.match(nome_jogador):
                    url_jogador = url_jogador['href'].replace('/jogador-do-corinthians/', 'https://www.meutimao.com.br/jogador-do-corinthians/')
                    jogadores[posicao_atual].append({'nome': nome_jogador, 'url': url_jogador})

        jogadores_json = json.loads(json.dumps(jogadores, default=str))
        return jogadores

    def infoPlayer(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        site = soup.text
        linha_nome_completo = re.search(r"Nome completo:\s*(.*)", site).group()
        nome_completo = linha_nome_completo.split(':')[1]
        linha_posicao_completo = re.search(r"Posição:\s*(.*)", site).group().strip()
        posicao = linha_posicao_completo.split(":")[1].replace("\n","").strip()
        linha_nascimento_completo = re.search(r"Data de nascimento:\s*(.*)", site).group().strip()
        data_nascimento = linha_nascimento_completo.split(":")[1].strip()
        linha_idade_completo = re.search(r"Idade:\s*(.*)", site).group().strip()
        idade = linha_idade_completo.split(":")[1].strip()
        linha_contrato_completo = re.search(r"Contrato válido até:\s*(.*)", site).group().strip()
        contrato_valido = linha_contrato_completo.split(":")[1].strip()
        info = f"Nome completo: {nome_completo}\nPosição: {posicao}\nData de nascimento: {data_nascimento}\nIdade: {idade}\nContrato válido até: {contrato_valido}"


        return info
