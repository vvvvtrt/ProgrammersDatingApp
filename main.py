from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QLabel, QPushButton, QComboBox, QProgressBar, \
    QMessageBox, QTextEdit, QVBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
import sys
from threading import Thread
from time import sleep
import program.TranslateUI as translete
import program.LetterMail as mmail
import program.AccountCheck as Check
import program.Notification as communication
import program.DataBase as base


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1200, 800)

        self.setWindowTitle('Programmers Dating')
        self.pixmap = QPixmap("image/fonStart.jpg")
        self.fon = QLabel(self)
        self.fon.move(0, 0)
        self.fon.resize(1200, 800)
        self.fon.setPixmap(self.pixmap)

        self.pixmap = QPixmap("image/icon.png")
        self.icon = QLabel(self)
        self.icon.resize(300, 300)
        self.icon.setPixmap(self.pixmap)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowIcon(QIcon('program/icons/client.ico'))

        self.code = QLineEdit(self)
        self.code.setValidator(QIntValidator())
        self.code.setMaxLength(4)
        self.code.textChanged.connect(self.ReadCode)
        self.code.resize(140, 50)
        self.code.setStyleSheet('border-radius: 20px;')
        self.code.setFont(QFont("Monospac821 BT", 25))

        self.namereg = QLineEdit(self)
        self.namereg.textChanged.connect(self.Name)
        self.namereg.setFont(QFont("Bernard MT", 15))
        self.namereg.setStyleSheet('border-radius: 20px;')
        self.namereg.resize(500, 50)

        self.name = QLabel(self)
        self.name.setText("Введити свое имя:")
        self.name.setStyleSheet('color: rgb(255, 255, 255);')
        self.name.setFont(QFont("Bernard MT", 15))
        self.name.resize(1000, 50)

        self.maillog = QLineEdit(self)
        self.maillog.textChanged.connect(self.Mail)
        self.maillog.setStyleSheet('border-radius: 20px;')
        self.maillog.setFont(QFont("Bernard MT", 15))
        self.maillog.resize(500, 50)

        self.mailreg = QLineEdit(self)
        self.mailreg.textChanged.connect(self.textchanged)
        self.mailreg.setFont(QFont("Bernard MT", 15))
        self.mailreg.resize(500, 50)

        self.SendingMessage = QLineEdit(self)
        self.SendingMessage.textChanged.connect(self.TextSendingMessage)
        self.SendingMessage.setStyleSheet('border-radius: 20px;')
        self.SendingMessage.setFont(QFont("Bernard MT", 15))
        self.SendingMessage.resize(500, 50)

        self.welcome = QLabel(self)
        self.welcome.setText('<h2 style="color: rgb(255, 255, 255);">Доборо пожаловать в Programmers Dating</h2>')
        self.welcome.setFont(QFont("Bernard MT", 15))
        self.welcome.resize(1000, 50)

        self.mailinput = QLabel(self)
        self.mailinput.setText("Введите свой адрес электронной почты:")
        self.mailinput.setStyleSheet('color: rgb(255, 255, 255);')
        self.mailinput.setFont(QFont("Bernard MT", 15))
        self.mailinput.resize(1000, 50)

        self.mailconfirm = QLabel(self)
        self.mailconfirm.setText("Введите код потверждения:")
        self.mailconfirm.setStyleSheet('color: rgb(255, 255, 255);')
        self.mailconfirm.setFont(QFont("Bernard MT", 15))
        self.mailconfirm.resize(1000, 50)

        self.lang = QLabel(self)
        self.lang.setText("Выберите язык:")
        self.lang.setStyleSheet('color: rgb(255, 255, 255);')
        self.lang.setFont(QFont("Bernard MT", 15))
        self.lang.resize(1000, 50)

        self.install = QLabel(self)
        self.install.setText("")
        self.install.setStyleSheet('color: rgb(255, 255, 255);')
        self.install.setFont(QFont("Bernard MT", 15))
        self.install.resize(1000, 50)

        self.error = QLabel(self)
        self.error.setText("Error")
        self.error.setStyleSheet('color: rgb(255, 0, 0);')
        self.error.setFont(QFont("Bernard MT", 15))
        self.error.resize(1000, 50)

        self.program = QLabel(self)
        self.program.setAlignment(Qt.AlignLeft)
        self.program.setText("")
        self.program.setStyleSheet('color: rgb(255, 255, 255);')
        self.program.setFont(QFont("Courier new", 15))
        self.program.resize(800, 650)

        self.nametape = QLabel(self)
        self.nametape.setAlignment(Qt.AlignLeft)
        self.nametape.setText("")
        self.nametape.setStyleSheet('color: rgb(255, 255, 255);')
        self.nametape.setFont(QFont("Bernard MT", 15))
        self.nametape.resize(500, 450)

        self.aboutme = QLabel(self)
        self.aboutme.setAlignment(Qt.AlignLeft)
        self.aboutme.setText("")
        self.aboutme.setStyleSheet('color: rgb(255, 255, 255);')
        self.aboutme.setFont(QFont("Bernard MT", 15))
        self.aboutme.resize(500, 450)

        self.InterlocutorName = QLabel(self)
        self.InterlocutorName.setAlignment(Qt.AlignLeft)
        self.InterlocutorName.setText("")
        self.InterlocutorName.setStyleSheet('color: rgb(255, 255, 255);')
        self.InterlocutorName.setFont(QFont("Bernard MT", 15))
        self.InterlocutorName.resize(500, 450)

        self.nameiz = QLineEdit(self)
        self.nameiz.textChanged.connect(self.Name)
        self.nameiz.setFont(QFont("Bernard MT", 15))
        self.nameiz.setStyleSheet('background: rgb(51,72,83); color: rgb(255,255,255); border-radius: 20px;')
        self.nameiz.resize(400, 50)

        self.Program = QPlainTextEdit(self)
        self.Program.setFont(QFont("Courier new", 15))
        self.Program.setStyleSheet('background: rgb(51,72,83); color: rgb(255,255,255); border-radius: 20px;')
        self.Program.resize(600, 750)

        self.AboutMe = QPlainTextEdit(self)
        self.AboutMe.setFont(QFont("Bernard MT", 15))
        self.AboutMe.setStyleSheet('background: rgb(51,72,83); color: rgb(255,255,255); border-radius: 20px;')
        self.AboutMe.resize(400, 550)

        self.next = QPushButton(self)
        self.next.setText('Далее >')
        self.next.setFont(QFont("Bernard MT", 18))
        self.next.setStyleSheet('background: rgb(41,62,73); color: rgb(255,255,255); border-radius: 20px;')
        self.next.clicked.connect(self.Next)
        self.next.resize(250, 100)

        self.back = QPushButton(self)
        self.back.setText('< Назад')
        self.back.setFont(QFont("Bernard MT", 18))
        self.back.setStyleSheet('background: rgb(41,62,73); color: rgb(255,255,255); border-radius: 20px;')
        self.back.clicked.connect(self.Start)
        self.back.resize(250, 100)

        self.complete = QPushButton(self)
        self.complete.setText('Завершить')
        self.complete.setFont(QFont("Bernard MT", 18))
        self.complete.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.complete.clicked.connect(self.Complete)
        self.complete.resize(250, 100)

        self.login = QPushButton(self)
        self.login.setText('Войти')
        self.login.setFont(QFont("Bernard MT", 18))
        self.login.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.login.clicked.connect(self.Login)
        self.login.resize(250, 100)

        self.regist = QPushButton(self)
        self.regist.setText('Регистрироваться')
        self.regist.setFont(QFont("Bernard MT", 18))
        self.regist.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.regist.clicked.connect(self.Registration)
        self.regist.resize(270, 100)

        self.combo = QComboBox(self)
        self.combo.addItem('Russian')
        self.combo.addItem('English')
        self.combo.addItem('German')
        self.combo.addItem('Spanish')
        self.combo.addItem('French')
        self.combo.resize(200, 50)
        self.combo.setStyleSheet('border-radius: 20px;')
        self.combo.setFont(QFont("Bernard MT", 18))
        self.combo.activated[str].connect(self.Language)

        self.pbar = QProgressBar(self)
        self.pbar.setFont(QFont("Bernard MT", 18))
        self.pbar.setStyleSheet(
            '''background: rgb(41,62,73); 
            color: rgb(255,255,255); 
            border-radius: 5xpx; 
            border: 2px solid grey; 
            text-align: center;
            ''')
        self.pbar.setValue(0)
        self.pbar.resize(600, 40)

        self.dating = QPushButton(self)
        self.dating.resize(100, 100)
        self.dating.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.dating.setIcon(QIcon('image/line.png'))
        self.dating.clicked.connect(self.Search)
        self.dating.setIconSize(QSize(100, 100))

        self.message = QPushButton(self)
        self.message.resize(100, 100)
        self.message.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.message.setIcon(QIcon('image/message.png'))
        self.message.clicked.connect(self.Message)
        self.message.setIconSize(QSize(100, 100))

        self.profile = QPushButton(self)
        self.profile.resize(100, 100)
        self.profile.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.profile.setIcon(QIcon('image/profile.png'))
        self.profile.clicked.connect(self.Profile)
        self.profile.setIconSize(QSize(100, 100))

        self.exit = QPushButton(self)
        self.exit.resize(100, 100)
        self.exit.setStyleSheet('background: rgb(69,190,77); color: rgb(255,255,255); border-radius: 20px;')
        self.exit.setIcon(QIcon('image/exit.png'))
        self.exit.clicked.connect(self.Exit)
        self.exit.setIconSize(QSize(100, 100))

        self.like = QPushButton(self)
        self.like.setText('✔')
        self.like.setFont(QFont("Bernard MT", 35))
        self.like.setStyleSheet('background: rgb(0,150,0); color: rgb(0,255,0); border-radius: 50px;')
        self.like.clicked.connect(self.Like)
        self.like.resize(100, 100)

        self.notlike = QPushButton(self)
        self.notlike.setText('×')  # Х
        self.notlike.setFont(QFont("Bernard MT", 50))
        self.notlike.setStyleSheet('background: rgb(150,0,0); color: rgb(255,0,0); border-radius: 50px;')
        self.notlike.clicked.connect(self.NotLike)
        self.notlike.resize(100, 100)

        self.save = QPushButton(self)
        self.save.setText('🖬')  # Х
        self.save.setFont(QFont("Bernard MT", 45))
        self.save.setStyleSheet('background: rgb(41,62,73); color: rgb(255,255,255); border-radius: 50px;')
        self.save.clicked.connect(self.Save)
        self.save.resize(100, 100)

        self.send = QPushButton(self)
        self.send.setText('➥')  # Х
        self.send.setFont(QFont("Bernard MT", 45))
        self.send.setStyleSheet('background: rgb(41,62,73); color: rgb(255,255,255); border-radius: 50px;')
        self.send.clicked.connect(self.Send)
        self.send.resize(100, 100)

        self.letters = []

        for i in range(6):
            self.letters.append(QLabel(self))
            self.letters[-1].setText("техт")
            self.letters[-1].setStyleSheet("""background: rgb(51,72,73); color: rgb(255, 255, 255); 
                            border-top-left-radius: 20px;
                            border-top-right-radius: 20px;
                            border-bottom-left-radius: 20px""")
            self.letters[-1].setFont(QFont("Bernard MT", 15))
            self.letters[-1].resize(400, 100)

        self.chats = []
        self.chatss = [self.Chat1, self.Chat2, self.Chat3, self.Chat4, self.Chat5, self.Chat6, self.Chat7, self.Chat8]
        for i in range(8):
            self.chats.append(QPushButton(self))
            self.chats[-1].setText("")
            self.chats[-1].resize(400, 100)
            self.chats[-1].setStyleSheet(
                'background: rgb(51,72,83); color: rgb(255,255,255); border: 1px solid white; border-left: none; border-right: none;')
            self.chats[-1].setFont(QFont("Bernard MT", 20))
            self.chats[-1].clicked.connect(self.chatss[i])
            self.chats[-1].setIconSize(QSize(100, 100))
            self.chats[-1].move(100, 100 * i)

        self.mail = "sleim2000@gmail.com"
        self.namee = ""
        self.codeen = ""
        self.codde = 0
        self.language = "Russian"
        self.words = ["Напишите свое имя", "Вставьте свою программу",
                      "Напишите немного о себе", "Нет подключения к интернету",
                      "Вы действительно хотите выйти?", "Вы действительно хотите сохранить?"]
        self.index = 0
        self.strangermail = ""
        self.Aboutme = ""
        self.programm = ""
        self.MailChats = [""] * 8
        self.Letter = [""] * 8
        self.TextMessage = ""

        self.Window = "clear"

        self.Start()

    def Clear(self):
        self.icon.move(-1000, 0)
        self.code.move(-1000, 0)
        self.namereg.move(-1000, 0)
        self.maillog.move(-1000, 0)
        self.mailreg.move(-1000, 0)
        self.welcome.move(-1000, 0)
        self.login.move(-1000, 520)
        self.regist.move(-1000, 520)
        self.mailinput.move(-1000, 0)
        self.next.move(-1000, 0)
        self.back.move(-1000, 100)
        self.mailconfirm.move(-1000, 0)
        self.error.move(-1000, 0)
        self.complete.move(-1000, 0)
        self.name.move(-1000, 0)
        self.combo.move(-1000, 0)
        self.lang.move(-1000, 0)
        self.pbar.move(-1000, 0)
        self.install.move(-1000, 0)
        self.dating.move(-1000, 0)
        self.message.move(-1000, 100)
        self.profile.move(-1000, 200)
        self.exit.move(-1000, 700)
        self.program.move(-1000, 0)
        self.nametape.move(-1000, 0)
        self.aboutme.move(-1000, 0)
        self.like.move(-1000, 0)
        self.notlike.move(-1000, 0)
        self.Program.move(-1000, 0)
        self.AboutMe.move(-1000, 0)
        self.nameiz.move(-1000, 0)
        self.save.move(-1000, 0)
        self.InterlocutorName.move(-1000, 0)
        self.send.move(-1000, 0)
        self.SendingMessage.move(-1000, 0)
        for i in range(6):
            self.letters[i].move(-1000, 0)
        for i in range(8):
            self.chats[i].move(-1000, 0)

    def Start(self):
        base.Write(self.mail)
        self.index = 0
        self.Clear()
        self.Window = "start"
        self.icon.move(450, 50)
        self.welcome.move(320, 350)
        self.login.move(220, 520)
        self.regist.move(720, 520)
        self.w = Welcome(self)
        self.w.start()

    def StartWelcome(self, wel, log, reg):
        self.welcome.setText(f'<h2 style="color: rgb(255, 255, 255);">{wel}</h2>')
        self.login.setText(log)
        self.regist.setText(reg)

    def Registration(self):
        self.Window = "regist"
        self.Clear()
        self.icon.move(450, -20)
        self.name.move(350, 250)
        self.namereg.move(350, 310)
        self.mailinput.move(350, 370)
        self.maillog.move(350, 430)
        self.lang.move(350, 490)
        self.combo.move(350, 550)
        self.next.move(700, 650)
        self.back.move(250, 650)

    def Login(self):
        self.Window = "login"
        self.Clear()
        self.icon.move(450, 50)
        self.mailinput.move(350, 350)
        self.maillog.move(350, 460)
        self.next.move(700, 600)
        self.back.move(250, 600)

    def Code(self):
        self.Clear()
        self.icon.move(450, 50)
        self.mailconfirm.move(350, 350)
        self.code.move(350, 420)
        self.back.move(250, 600)
        self.complete.move(700, 600)

    def Next(self):
        if self.Window == "regist" and len(self.namee) < 2:
            self.error.setText("❗ Введите имя ❗")
            self.error.move(350, 600)
        else:
            try:
                c = Check.LoadingFrom(self.mail).check()
                if self.Window == "login" and c != "true":
                    raise
                elif self.Window == "regist" and c == "true":
                    self.error.setText("❗ Этот адрес электронной почты уже занят ❗")
                    self.error.move(170, 600)
                else:
                    if self.Window == "login":
                        c = mmail.maillog(mail=self.mail)
                    else:
                        c = mmail.mailreg(mail=self.mail, name=self.namee)
                    self.codeen = c
                    self.Code()
            except:
                if self.Window == "login":
                    self.error.setText("❗ Неверный адрес электронной почты или нет подключения к интернету ❗")
                    self.error.move(170, 530)
                else:
                    self.error.setText("❗ Неверный адрес электронной почты или нет подключения к интернету ❗")
                    self.error.move(170, 600)

    def Complete(self):
        if self.codde == self.codeen:
            if self.Window == "regist":
                Check.LoadingIn(self.mail, self.namee, self.language, "", "")
                self.InstallerLanguage()
            else:
                g = Info(self)
                g.start()

        else:
            self.error.setText("❗ Неверный код подтверждения ❗")
            self.error.move(350, 530)

    def InstallerLanguage(self):
        word = {"Russian": "Идет загрузка вашего языка ...", "English": "Loading your language ...",
                "German": "Laden Sie Ihre Sprache ...",
                "Spanish": "Cargando su idioma ...", "French": "Chargement de votre langue ..."}
        base.Write(self.mail)
        if self.language != "Russian":
            self.Clear()
            self.install.setText(word[self.language])
            translete.Translate().loading(self.words, self.language)
            g = Loaging(self)
            g.start()
            self.install.move(320, 340)
            self.pbar.move(320, 400)
        else:
            self.Search()

    def Search(self):
        self.Clear()
        self.dating.move(0, 0)
        self.message.move(0, 100)
        self.profile.move(0, 200)
        self.exit.move(0, 700)
        self.program.move(150, 20)
        self.like.move(950, 680)
        self.notlike.move(1080, 680)
        self.program.move(150, 20)
        self.nametape.move(770, 20)
        self.aboutme.move(770, 120)
        g = Tape(self, self.index)
        g.start()

    def Message(self):
        self.Clear()
        self.dating.move(0, 0)
        self.message.move(0, 100)
        self.profile.move(0, 200)
        self.exit.move(0, 700)
        g = ChatLoading(self)
        g.start()
        for i in range(8):
            self.chats[i].move(120, 100 * i)

    def Profile(self):
        self.Clear()
        self.dating.move(0, 0)
        self.message.move(0, 100)
        self.profile.move(0, 200)
        self.exit.move(0, 700)
        self.Program.move(150, 20)
        self.Program.appendPlainText(self.words[1])
        self.AboutMe.move(770, 120)
        self.AboutMe.appendPlainText(self.words[2])
        self.nameiz.move(770, 20)
        self.nameiz.setText(self.words[0])
        self.save.move(1080, 705)

    def Exit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Выход из приложения Programmers Dating")
        msg.setText(self.words[4])
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setStyleSheet('background: rgb(41,62,73); color: rgb(255,255,255); border-radius: 20px;')
        msg.setWindowIcon(QIcon('program\icons\client.ico'))
        retval = msg.exec_()
        if retval == QMessageBox.Ok:
            self.Start()

    def Save(self):
        msg = QMessageBox()
        msg.setWindowTitle("Сохранение данных в приложении Programmers Dating")
        msg.setText(self.words[5])
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setStyleSheet('background: rgb(41,62,73); color: rgb(255,255,255); border-radius: 20px;')
        msg.setWindowIcon(QIcon('program\icons\client.ico'))
        retval = msg.exec_()
        self.Aboutme = self.AboutMe.toPlainText()
        self.programm = self.Program.toPlainText()
        if retval == QMessageBox.Ok:
            Check.NewProfile(self.mail, self.namee, self.programm, self.Aboutme).profile()
            self.Search()

    def LoadingChat(self):
        self.Clear()
        self.dating.move(0, 0)
        self.message.move(0, 100)
        self.profile.move(0, 200)
        self.exit.move(0, 700)
        self.InterlocutorName.setText(self.strangermail)
        self.InterlocutorName.move(550, 20)
        self.send.move(1080, 680)
        self.SendingMessage.move(550, 710)
        for i in range(8):
            self.chats[i].move(120, 100 * i)
        if len(self.Letter) > 6:
            self.Letter = self.Letter[-6:-1]
            for i in range(5):
                m = self.Letter[i].split("*")
                if m[0] == self.mail:
                    self.letters[i].setText(m[1])
                    self.letters[i].setStyleSheet("""background: rgb(51,72,73); color: rgb(255, 255, 255); 
                                                border-top-left-radius: 20px;
                                                border-top-right-radius: 20px;
                                                border-bottom-left-radius: 20px""")
                    self.letters[i].move(780, 100 + 110 * i)
                else:
                    self.letters[i].setText(m[1])
                    self.letters[i].setStyleSheet("""background: rgb(51,72,73); color: rgb(255, 255, 255); 
                                                                    border-top-left-radius: 20px;
                                                                    border-top-right-radius: 20px;
                                                                    border-bottom-right-radius: 20px""")
                    self.letters[i].move(550, 100 + 110 * i)
        else:
            for i in range(len(self.Letter)):
                m = self.Letter[i].split("*")
                if m[0] == self.mail:
                    self.letters[i].setText(m[1])
                    self.letters[i].setStyleSheet("""background: rgb(51,72,73); color: rgb(255, 255, 255); 
                                                border-top-left-radius: 20px;
                                                border-top-right-radius: 20px;
                                                border-bottom-left-radius: 20px""")
                    self.letters[i].move(780, 100 + 110 * i)
                else:
                    self.letters[i].setText(m[1])
                    self.letters[i].setStyleSheet("""background: rgb(51,72,73); color: rgb(255, 255, 255); 
                                                                    border-top-left-radius: 20px;
                                                                    border-top-right-radius: 20px;
                                                                    border-bottom-right-radius: 20px""")
                    self.letters[i].move(550, 100 + 110 * i)

    def Chat1(self):
        if self.MailChats[0]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[0]).ChatsLoading()
            self.strangermail = self.MailChats[0]
            self.LoadingChat()

    def Chat2(self):
        if self.MailChats[1]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[1]).ChatsLoading()
            self.strangermail = self.MailChats[1]
            self.LoadingChat()

    def Chat3(self):
        if self.MailChats[2]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[2]).ChatsLoading()
            self.strangermail = self.MailChats[2]
            self.LoadingChat()

    def Chat4(self):
        if self.MailChats[3]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[3]).ChatsLoading()
            self.strangermail = self.MailChats[3]
            self.LoadingChat()

    def Chat5(self):
        if self.MailChats[4]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[4]).ChatsLoading()
            self.strangermail = self.MailChats[4]
            self.LoadingChat()

    def Chat6(self):
        if self.MailChats[5]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[5]).ChatsLoading()
            self.strangermail = self.MailChats[5]
            self.LoadingChat()

    def Chat7(self):
        if self.MailChats[6]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[6]).ChatsLoading()
            self.strangermail = self.MailChats[6]
            self.LoadingChat()

    def Chat8(self):
        if self.MailChats[7]:
            self.Letter = Check.MyMessageInChat(self.mail, self.MailChats[7]).ChatsLoading()
            self.strangermail = self.MailChats[7]
            self.LoadingChat()

    def Send(self):
        Check.Like(self.mail, self.strangermail, self.TextMessage).check()
        g = self.MailChats.index(self.strangermail)
        self.chatss[g]()

    def TextSendingMessage(self, text):
        self.TextMessage = text

    def Like(self):
        Check.Like(self.mail, self.strangermail, "Hello!")
        self.index += 1
        self.Search()

    def NotLike(self):
        self.index += 1
        self.Search()

    def Back(self):
        self.Start()

    def ReadCode(self, text):
        self.codde = text

    def textchanged(self, text):
        print(text)

    def Language(self, lang):
        self.language = lang

    def Mail(self, text):
        self.mail = text

    def Name(self, text):
        self.namee = text


class Welcome(Thread):
    def __init__(self, selff):
        Thread.__init__(self)
        self.selff = selff

    def run(self):
        lang = ["Доборо пожаловать в", "Welcome to", "Willkommen zu", "Bienvenida a la", "Bienvenue à"]
        log = ["Войти", "Login", "Betreten", "Entrar", "Entrer"]
        reg = ["Регистрироваться", "Register", "Registrieren", "Registrarse", "S'inscrire"]
        while self.selff.Window == "start":
            for i in range(5):
                sleep(3)
                self.selff.StartWelcome(lang[i] + " Programmers Dating", log[i], reg[i])


class Loaging(Thread):
    def __init__(self, selff):
        Thread.__init__(self)
        self.selff = selff

    def run(self):
        while "" in translete.UI:
            self.selff.pbar.setValue(
                int(100 / len(self.selff.words)) * (len(self.selff.words) - translete.UI.count("")) - 1)
        self.selff.words = translete.UI
        self.selff.Search()


class ChatLoading(Thread):
    def __init__(self, selff):
        Thread.__init__(self)
        self.selff = selff

    def run(self):
        self.selff.MailChats = Check.Chats(self.selff.mail).ChatsLoading()[::-1]
        self.selff.MailChats.pop(0)
        if len(self.selff.MailChats) > 8:
            self.selff.MailChats = self.selff.MailChats[0:8]
        else:
            for i in range(8 - len(self.selff.MailChats)):
                self.selff.MailChats.append("")
        for i in range(8):
            self.selff.chats[i].setText(self.selff.MailChats[i])


class Info(Thread):
    def __init__(self, selff):
        Thread.__init__(self)
        self.selff = selff

    def run(self):
        i = 0
        while True:
            t = Check.Tape(i).check()
            i += 1
            if t[0] == self.selff.mail:
                if not t:
                    t = [self.selff.words[3] + " "] * 5
                    t.append("0")
                self.selff.language = t[1]
                self.selff.namee = t[2]
                if int(t[-2]) > 0:
                    communication.notification(messeage=f"{t[-2]} новых сообщений")
                break
        self.selff.InstallerLanguage()


class Tape(Thread):
    def __init__(self, selff, index):
        Thread.__init__(self)
        self.selff = selff
        self.index = index

    def run(self):
        t = Check.Tape(self.selff.index).check()
        if t[0] == self.selff.mail:
            self.selff.index += 1
            self.run()
            return 0
        if not t:
            t = [self.selff.words[3] + " "] * 5
            t.append("0")
        self.selff.strangermail = t[0]
        self.selff.program.setText(t[3])
        self.selff.nametape.setText(t[2])
        self.selff.aboutme.setText(t[4])
        # if int(t[-2]) > 0:
        #     communication.notification(messeage=f"{t[-2]} новых сообщений")


class Messengers(Thread):
    def __init__(self, selff):
        Thread.__init__(self)
        self.selff = selff

    def run(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
