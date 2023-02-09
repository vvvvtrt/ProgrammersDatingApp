from requests import get
from threading import Thread
import program.Notification as noti
import program.DataBase as base

def connected_to_internet(url='http://yandex.ru/', timeout=5):
    try:
        get(url, timeout=timeout)
        return True
    except:
        return False


class LoadingIn:
    def __init__(self, mail, name, lang, code, AboutMe):
        self.mail = mail
        self.name = name
        self.lang = lang
        self.code = code
        self.AboutMe = AboutMe

    def DataRetrieval(self):
        if connected_to_internet():
            try:
                reg = get(
                    f"http://vvvvtrt.pythonanywhere.com/w {self.mail} {self.lang} {self.name} {self.code} {self.AboutMe}"
                    ).content.decode("utf-8")

                return reg
            except:
                return False

class LoadingFrom:
    def __init__(self, mail):
        self.mail = mail

    def check(self):
        if connected_to_internet():
            try:
                index = get(
                    f"http://vvvvtrt.pythonanywhere.com/j {self.mail}").content.decode("utf-8")
                return index
            except:
                return False


class Profile:
    def __init__(self, mail):
        self.mail = mail

    def check(self):
        if connected_to_internet():
            try:
                index = get(
                    f"http://vvvvtrt.pythonanywhere.com/p {self.mail}").content.decode("utf-8")
                return index
            except:
                return False


class Chats:
    def __init__(self, mail):
        self.mail = mail

    def ChatsLoading(self):
        if connected_to_internet():
            try:
                chats = get(
                    f"http://vvvvtrt.pythonanywhere.com/c {self.mail}").content.decode("utf-8")
                return chats.split("/")
            except:
                return [''] * 8


class MyMessageInChat:
    def __init__(self, MyMail, NotMyMail):
        self.MyMail = MyMail
        self.NotMyMail = NotMyMail

    def ChatsLoading(self):
        if connected_to_internet():
            try:
                chats = get(
                    f"http://vvvvtrt.pythonanywhere.com/s {self.MyMail} {self.NotMyMail}").content.decode("utf-8")
                return chats.split("/")
            except:
                return [""]


class NewProfile:
    def __init__(self, mail, name, program, aboutme):
        self.mail = mail
        self.name = name
        self.program = program
        self.aboutme = aboutme

    def profile(self):
        if connected_to_internet():
            try:
                index = get(
                    f"http://vvvvtrt.pythonanywhere.com/n^{self.mail}^{self.name}^{self.program}^{self.aboutme}").content.decode("utf-8")
                return index
            except:
                return False


class Tape:
    def __init__(self, index):
        self.index = index

    def check(self):
        if connected_to_internet():
            try:
                tape = get(
                    f"http://vvvvtrt.pythonanywhere.com/i {self.index}").content.decode("utf-8")
                return tape.split("/")
            except:
                return ""
        return ""


class Like:
    def __init__(self, MailMy, MailHe, mes):
        self.MailMy = MailMy
        self.MailHe = MailHe
        self.mes = mes

    def check(self):
        if connected_to_internet():
            try:
                tape = get(
                    f"http://vvvvtrt.pythonanywhere.com/m/{self.MailMy}/{self.MailHe}/{self.mes}").content.decode("utf-8")
                return tape.split("")
            except:
                return ""
        return ""

class MyMessage:
    def __init__(self, mail):
        self.mail = mail

    def check(self):
        if connected_to_internet():
            try:
                tape = get(
                    f"http://vvvvtrt.pythonanywhere.com/h").content.decode("utf-8")
                return tape.split("")
            except:
                return ""
        return ""

class Notifications(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.letter = 0

    def run(self):
        while True:
            c = base.Read()
            if c != "":
                c = Profile(c).check().split("/")
                try:
                    if self.letter != int(c[-2]):
                        g = int(c[-2]) - self.letter
                        noti.notification2(messeage=f"{g} новых сообщений")
                        self.letter = int(c[-2])
                except:
                    pass


m = Notifications()
#m.start()

if __name__ == '__main__':
    print(Chats("sleim2000@gmail.com").ChatsLoading())
