import smtplib
import email.message
import random


class Codigo_verific:

    def __init__(self, email):
        self.email = email

    def enviar_email(self):  

        codigo_verific = random.randint(100000,999999)

        corpo_email = f"""
        <p>PassKey código de verificação: </p>
        <b>{codigo_verific}</b>
        """

        msg = email.message.Message()
        msg['Subject'] = "Código de verificação"
        msg['From'] = 'passkey2022@gmail.com'
        msg['To'] = self.email
        password = 'combinacaodesenha741' 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        return codigo_verific

