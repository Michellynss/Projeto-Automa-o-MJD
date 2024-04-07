import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_data_ontem():
    data_hoje = datetime.now()
    data_ontem = data_hoje - timedelta(days=1)
    return data_ontem.strftime('%d/%m/%Y')
ontem = get_data_ontem()
data_atual = datetime.now().strftime('%Y-%m-%d')


# Função para raspar a agenda do Lula
def agenda_presidente_lula():
    data_atual = datetime.now().strftime("%Y-%m-%d")
    url = f'https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica-lula/agenda-do-presidente-da-republica/{data_atual}'
    agenda_lula = requests.get(url)
    html = agenda_lula.content
    soup = BeautifulSoup(html, 'html.parser')
    agenda = soup.find_all('li', class_='item-compromisso-wrapper')
    compromissos = []
    for compromisso in agenda:
        horario = compromisso.find('time', class_='compromisso-inicio').text.strip()
        descricao = compromisso.find('h2', class_='compromisso-titulo').text.strip()
        local = compromisso.find('div', class_='compromisso-local').text.strip()
        link = compromisso.find('a', class_='add-agenda')['href']
        compromisso_info = {
            'horario': horario,
            'descrição': descricao,
            'local': local,
            'link': link}
        compromissos.append(compromisso_info)
    return compromissos

# Função para raspar as notícias do Senado
## Palavras-chave das notícias
palavras_chave = ['internet', 'eleições', 'fake news', 'inteligência artificial', 'redes sociais', 'notícias falsas', 'desinformação', 'notícia falsa', 'checagem de fatos']


def buscar_noticias_senado():
    noticias_senado = []
    urls_senado = []
    for pagina in range(1, 5):
        url_senado = f'https://www12.senado.leg.br/noticias/ultimas/{pagina}'
        urls_senado.append(url_senado)

    for url in urls_senado:
        requisicao_senado = requests.get(url)
        html_senado = requisicao_senado.content
        soup_senado = BeautifulSoup(html_senado, 'html.parser')
        noticia_senado = soup_senado.find_all('ol', {'class': 'list-unstyled lista-resultados'})
        for noticia in noticia_senado:
            data_elementos = noticia.find_all('div', class_="text-muted normalis hidden-xs")
            for data_elemento in data_elementos:
                data = data_elemento.get_text(strip=True)
                if ontem in data:
                    link_elemento = data_elemento.find_next('a')
                    titulo_elemento = link_elemento.find('span', class_="eta normalis-xs")
                    if titulo_elemento:
                        titulo_senado = titulo_elemento.get_text(strip=True).lower()
                        link_elemento = link_elemento['href']
                        link_senado = f'https://www12.senado.leg.br{link_elemento}'
                        if any(palavra in titulo_senado for palavra in palavras_chave):
                            noticias_dia = {"titulo_senado": titulo_senado, "link_senado": link_senado} 
                            noticias_senado.append(noticias_dia)
    return noticias_senado
