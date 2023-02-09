# эта программа генерирует код и отправляет его на электронную почту

import smtplib, ssl
from email.message import EmailMessage
from random import randint
import http.client


def code():
    global Code
    Code = ""
    for i in range(4):
        Code += str(randint(0, 9))
    return Code

def mailreg(mail, name):
    message = f"""
    Добрый день, {name}!

    Вы были зарегистрированны в приложении Programmers Dating

    Если же вы регистрировались в приложении Programmers Dating, то код подтверждения ниже
    Code: {code()}

    Если вы получили такое письмо и не регистрировались в приложении Programmers Dating, скорее всего, другой 
    пользователь случайно указал ваш адрес электронной почты, пытаясь создать аккаунт для себя. 
    Не беспокойтесь – от вас не требуется никаких действий. Просто проигнорируйте это письмо, и
    адрес не будет подтвержден.

    """
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Регистрация в приложении Programmers Dating"
    msg["From"] = 'botvvvvtrt@gmail.com'
    msg["To"] = "" + mail
    context=ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], 'BOT228007')
        smtp.send_message(msg)

    return Code

def maillog(mail):

    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    c = str(conn.getresponse().read())
    c = c[2:-1]

    message = f"""
    Добрый день!

    Был выполнен запрос на вход в приложении Programmers Dating
    с IP: {c}

    Если это вы входите в приложении Programmers Dating, то код подтверждения ниже
    Code: {code()}

    Если вы получили такое письмо и не входили в приложении Programmers Dating, скорее всего, другой 
    пользователь случайно указал ваш адрес электронной почты, пытаясь войти в свой аккаунт. 
    Не беспокойтесь – от вас не требуется никаких действий. Просто проигнорируйте это письмо, и
    адрес не будет подтвержден.

    """
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Вход в приложении Programmers Dating"
    msg["From"] = 'botvvvvtrt@gmail.com'
    msg["To"] = "" + mail
    context=ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], 'BOT228007')
        smtp.send_message(msg)

    return Code

if __name__ == '__main__':
    maillog(mail="mike1603@yandex.ru")