import sys
import os
from rich import print
from rich.progress import track
import smtplib
import time
from email.message import EmailMessage
from senha import senha
from senha import email
#V1.0
#github.com/bueroficial

try:
    os.system('cls')
except:
    os.system('clear')

#Configurar email, senha
EMAIL_ADDRESS = email
EMAIL_PASSWORD = senha

if email == '' or senha == '':
    print('[red] Email e/ou Senha não declarado!! Consulte o arquivo senha.py. \n Apenas emails da google suportados! \n Consulte o README.md para mais detalhes![/]')
    time.sleep(1)
    sys.exit()
else:
    pass


print('[bold]ENVIE SEU EMAIL! [/]')
time.sleep(1)
tema = input('[*] -> Digite o subject do email:   ')
time.sleep(1)
dest = input('[*] -> Para quem o email vai ser enviado?   ')
time.sleep(1)
body = input('[*] ->Digite o corpo da mensagem:   ')


# Criar o E-mail:
msg = EmailMessage()
msg['Subject'] = tema
msg['From'] = email
msg['To'] = dest
msg.set_content(body)

# Enviar o email
try:
    for tarefa in track(range(1), 'Enviando...'):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    print('[bold]Enviado com sucesso!![/]')
except:
    print('[red]Não foi possível completar o envio! Tente novamente...[/]')