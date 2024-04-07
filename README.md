## Projeto final da disciplina de Algoritmos de Automação do Master em Jornalismo de Dados do Insper.

### Bibliotecas usadas:
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [requests](https://requests.readthedocs.io/en/latest/) 
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [datetime](https://docs.python.org/pt-br/3/library/datetime.html)
- [os](https://docs.python.org/pt-br/3/library/os.html)
- [email.mime](https://docs.python.org/pt-br/3.7/library/email.mime.html)
- [smtplib](https://docs.python.org/3/library/smtplib.html)


## Este projeto foi dividido em duas partes:

### Primeira parte
Foram colocadas online três páginas HTML do portfólio de uma das alunas do curso. Estas páginas incluem apresentação, contato e matérias publicadas.
Nesta parte foi utilizado apenas o Flask.

### Segunda parte
Foi criada uma página dinâmica que permite visualizar a agenda do presidente Lula e notícias recentes do Senado relacionadas à internet e desinformação. 

enviar um email com atualizações diárias da agenda.
Primeiro, foi preciso criar um raspador usando as bibliotecas requests, datetime e BeautifulSoup.

Em seguida, foi criada uma função para visualizar os dados da agenda no site e enviar o email com os compromissos de Lula.
Aqui foram utilizadas as bibliotecas: Flask, email.mime, smtplib.

Usei a biblioteca OS para acessar informações sensíveis, como senha e número do servidor, armazenadas no render.