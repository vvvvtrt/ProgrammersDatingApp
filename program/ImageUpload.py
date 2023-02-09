from requests import get
from threading import Thread


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
                index = get(
                    f"http://vvvvtrt.pythonanywhere.com/w {self.mail} {self.name} {self.lang} {self.code} {self.AboutMe}").content.decode(
                    "utf-8")
            except:
                return False

class LoadingFrom:
    def __init__(self, mail):
        self.mail = mail

    def check(self):
        if connected_to_internet():
            try:
                index = get(
                    f"http://vvvvtrt.pythonanywhere.com/с {self.mail}").content.decode("utf-8")
                return index
            except:
                return False



if __name__ == '__main__':
    connected_to_internet()
