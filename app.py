from flask import Flask, render_template
import gunicorn
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

from scraping import agenda_presidente_lula, buscar_noticias_senado

app = Flask(__name__)

## Primeira parte
# Página de apresentação
@app.route("/")
def home():
  return render_template('apresentacao.html')

# Página do portifólio
@app.route("/portifolio")
def portifolio():
  return render_template('materias.html')

# Página de contato
@app.route("/contato")
def contato():
  return render_template('contato.html')

## Segunda parte

# Credenciais email
smtp_server = 'smtp-relay.brevo.com'
port = 587
email = os.environ['email']
senha = os.environ['senha_email']
remetente = os.environ['email']
destinatarios = os.environ['email']            

@app.route("/atualizacoes")
def atualizacoes():
    compromissos = agenda_presidente_lula()
    noticias_senado = buscar_noticias_senado()

    if compromissos or noticias_senado:
        return render_template('atualizacoes.html', compromissos=compromissos, noticias_senado=noticias_senado)
    else:
        return "Lula não tem compromissos hoje e não há notícias do Senado"

@app.route("/email")
def enviar_email(compromissos, noticias_senado):
    
    titulo = f"Atualizações do dia, {datetime.now().strftime('%Y-%m-%d')}"
    html = """
    <!DOCTYPE html>
    <html>
    <body>
      <h2>Agenda do Lula</h2>
      <p>
        <ul>
    """

    for compromisso in compromissos:
        html += f"<li>{compromisso['horario']}: {compromisso['descrição']} - {compromisso['local']}</li>"
    
    html += """
        </ul>
      </p>
      <h2>Notícias do Senado</h2>
      <p>
        <ul>
    """

    for noticia in noticias_senado:
        html += f"<li> <a href={ noticia['link_senado']}>{ noticia['titulo_senado'] } </a> </li>"
    html += "</ul>"
    
    html += """
    </body>
    </html>
    """
    
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(email, senha)
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = ",".join(destinatarios)
    mensagem["Subject"] = titulo
    conteudo_html = MIMEText(html, "html")
    mensagem.attach(conteudo_html)
    server.sendmail(remetente, destinatarios, mensagem.as_string())
    server.quit()
    return "Email enviado"

if __name__ == "__main__":
    app.run()
