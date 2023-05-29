import sqlite3
import random
import time
import os
import sys
from selenium import webdriver, common
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.chrome.service import Service as ChromeService

from windows_ui import Ui_MainWindow

global ans
ans=""
urlbing="https://cn.bing.com/"
urlchatgpt="https://poe.com/ChatGPT"
global q
q=""
global a
a=""
global b
b=""
global c
c=""
global d
d=""

class MyWindow(QtWidgets.QMainWindow):
    # ui = None

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #
        # self.ui.pushButton_question.setDown(True)
        #设置标题名称
        self.setWindowTitle("Random Question")
        self.ui.pushButton_question.clicked.connect(self.ShowQuestion)

        #判断按钮是否被按下
        self.ui.pushButton_A.pressed.connect(self.A)
        self.ui.pushButton_B.pressed.connect(self.B)
        self.ui.pushButton_C.pressed.connect(self.C)
        self.ui.pushButton_D.pressed.connect(self.D)
        self.ui.pushButton_Bing.clicked.connect(self.AskBing)

        self.show()

    def AskBing(self):
        self.myth = myThead()
        self.myth.start()
        global q,a,b,c,d
        q=self.ui.label_ques.text()
        a=self.ui.label_A.text()
        b=self.ui.label_B.text()
        c=self.ui.label_C.text()
        d=self.ui.label_D.text()


    # def AskChatGPT(self):
    #     self.myth.start()
    #     global q,a,b,c,d
    #     q=self.ui.label_ques.text()
    #     a=self.ui.label_A.text()
    #     b=self.ui.label_B.text()
    #     c=self.ui.label_C.text()
    #     d=self.ui.label_D.text()

    def ShowQuestion(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        line=random.choice(datas)
        self.ui.label_ques.setText(line[0])
        self.ui.label_A.setText(line[1])
        self.ui.label_B.setText(line[2])
        self.ui.label_C.setText(line[3])
        self.ui.label_D.setText(line[4])
        global ans
        ans =str(line[5])
        # print(datas)
    def A(self):
        if self.ui.pushButton_A.isDown():
            print("A")
        if self.ui.pushButton_A.isDown() and ans=="A":
            self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.pushButton_A.isDown() and ans!="A":
            self.ui.stackedWidget.setCurrentIndex(2)
    def B(self):
        if self.ui.pushButton_B.isDown() and ans=="B":
            self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.pushButton_B.isDown() and ans!="B":
            self.ui.stackedWidget.setCurrentIndex(2)

    def C(self):
        if self.ui.pushButton_C.isDown() and ans=="C":
            self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.pushButton_C.isDown() and ans!="C":
            self.ui.stackedWidget.setCurrentIndex(2)
    def D(self):
        if self.ui.pushButton_D.isDown() and ans=="D":
            self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.pushButton_D.isDown() and ans!="D":
            self.ui.stackedWidget.setCurrentIndex(2)


class myThead(QtCore.QThread):
    def __init__(self):
        # QtCore.QThread.__init__(self)
        # MyWindow.__init__(self)
        super(myThead, self).__init__()

    def AskBing(self):
        # edge_options = webdriver.EdgeOptions()
        # #屏蔽inforbar
        # edge_options.add_experimental_option('useAutomationExtension', False)
        # edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        # edge_options.add_argument('--disable-popup-blocking')
        # browser = webdriver.Edge(options=edge_options)
        global q, a, b, c, d
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

        chrome_service = ChromeService('chromedriver')
        chrome_service.creationflags =CREATE_NO_WINDOW
        # chrome_service.add_argument('--headless')
        chrome_service = ChromeService(resource_path("./chromedriver.exe"))
        browser = webdriver.Chrome(service=chrome_service,options=chrome_options)
        browser.get(urlbing)
        input_word=browser.find_element(By.ID,'sb_form_q')
        # input_word.send_keys(self.ui.label_ques.text()+" A、"+self.ui.label_A.text()+" B、"+self.ui.label_B.text()+" C、"+self.ui.label_C.text()+" D、"+self.ui.label_D.text())
        input_word.send_keys(q + " A、" + a + " B、" + b + " C、" + c + " D、" + d)
        browser.find_element(By.ID,'search_icon').click()
        time.sleep(600)
        browser.quit()

    #这部分未完成
    # def AskChatGPT(self):
    #     # edge_options = webdriver.EdgeOptions()
    #     # #屏蔽inforbar
    #     # edge_options.add_experimental_option('useAutomationExtension', False)
    #     # edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    #     # edge_options.add_argument('--disable-popup-blocking')
    #     # browser = webdriver.Edge(options=edge_options)
    #     global q, a, b, c, d
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--disable-popup-blocking')
    #     chrome_options.add_experimental_option('useAutomationExtension', False)
    #     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    #     browser = webdriver.Chrome(options=chrome_options)
    #     browser.get(urlchatgpt)
    #     input_word=browser.find_element(By.CLASS_NAME,'GrowingTextArea_textArea__eadlu')
    #     # input_word.send_keys(self.ui.label_ques.text()+" A、"+self.ui.label_A.text()+" B、"+self.ui.label_B.text()+" C、"+self.ui.label_C.text()+" D、"+self.ui.label_D.text())
    #     input_word.send_keys(q + " A、" + a + " B、" + b + " C、" + c + " D、" + d)
    #     browser.find_element(By.CLASS_NAME,'Button_buttonBase__0QP_m Button_primary__pIDjn ChatMessageSendButton_sendButton__OMyK1 ChatMessageInputContainer_sendButton__s7XkP').click()
    #     time.sleep(600)
    #     # browser.quit()
    def run(self):
        self.AskBing()
        # self.AskChatGPT()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    import sys

    db_path = resource_path('test.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM question")
    datas = cur.fetchall()
    cur.close()
    conn.close()

    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())