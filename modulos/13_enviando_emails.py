from dotenv import load_dotenv
import os
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

#Caminho HTML
HTML_PATH = Path(__file__).parent / '13_enviando_emails.html'

#Dados do remetente
sender = os.getenv('FROM_EMAIL')
recipient = sender

#Configuracoes do SMTP
smtp_server = os.getenv('SMTP_SERVER')
print(smtp_server)
smtp_port = os.getenv('SMTP_PORT')
print(smtp_port)
smtp_user = os.getenv('FROM_EMAIL')
print(smtp_user)
smtp_password = os.getenv('EMAIL_PASSWORD')
print(smtp_password)

#Mensagem de texto
with open(HTML_PATH, 'r') as file:
    html_text = file.read()
    template = Template(html_text)
    email_text = template.substitute(name='Pedro')

#Transformando nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'Python mail'

email_body = MIMEText(email_text, 'html', 'utf-8') #Se fosse .txt --> plain no lugar de html

mime_multipart.attach(email_body)

#Enviando o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    
    print('E-mail enviado com sucesso.')