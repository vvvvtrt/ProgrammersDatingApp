from translate import Translator
from threading import Thread

class Translate:
    def __init__(self):
        global name, lang, UI

    def loading(self, arr, tongue):
        global UI
        UI = [""] * len(arr)
        for i in range(len(arr)):
            self.t = transfer(arr, i, tongue)
            self.t.start()


class transfer(Thread):
    def __init__(self, arr, index, tongue):
        Thread.__init__(self)
        self.arr = arr
        self.index = index
        self.tongue = tongue

    def run(self):
        global UI
        translator = Translator(from_lang="Russian", to_lang=self.tongue)
        UI[self.index] = translator.translate(self.arr[self.index])


name = "Hacker Dating"
lang = ["Russian", "English", "German", "Spanish", "French"]
UI = []
if __name__ == '__main__':
    g = Translate()
    g.loading(["привет", "пока"], lang[1])
    while min(UI) == "": pass
    print(UI)