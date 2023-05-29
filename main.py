import sqlite3
import random
import time
from selenium import webdriver, common
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

from windows_ui import Ui_MainWindow

global ans
ans=""
urlbing="https://cn.bing.com/"
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
        self.myth=myThead()
        self.ui.pushButton_chatgpt.clicked.connect(self.AskChatGPT)
        # self.myth = myThead()
        self.show()

    # def AskBing(self):
    #     edge_options = webdriver.EdgeOptions()
    #     #屏蔽inforbar
    #     edge_options.add_experimental_option('useAutomationExtension', False)
    #     edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    #
    #
    #     browser = webdriver.Edge(options=edge_options)
    #     browser.get(urlbing)
    #     input_word=browser.find_element(By.ID,'sb_form_q')
    #     input_word.send_keys(self.ui.label_ques.text()+" A、"+self.ui.label_A.text()+" B、"+self.ui.label_B.text()+" C、"+self.ui.label_C.text()+" D、"+self.ui.label_D.text())
    #     # input_word.send_keys("你好")
    #     browser.find_element(By.ID,'search_icon').click()
    #     # time.sleep(100)
    #     browser.quit()
        # ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
    def AskBing(self):
        self.myth.start()


    def AskChatGPT(self):
        browser = webdriver.Chrome()
        browser.get('https://www.chatbot.com.cn/chatgpt/')
        input_word=browser.find_element(By.class_name,'input')
        input_word.send_keys(self.ui.label_ques.text())
        # input_word.send_keys("你好")
        browser.find_element(By.ID,'send').click()
        # time.sleep(100)
        browser.quit()

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


class myThead(MyWindow,QtCore.QThread):
    def __init__(self):
        super(myThead, self).__init__()

    def AskBing(self):
        edge_options = webdriver.EdgeOptions()
        #屏蔽inforbar
        edge_options.add_experimental_option('useAutomationExtension', False)
        edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])


        browser = webdriver.Edge(options=edge_options)
        browser.get(urlbing)
        input_word=browser.find_element(By.ID,'sb_form_q')
        input_word.send_keys(self.ui.label_ques.text()+" A、"+self.ui.label_A.text()+" B、"+self.ui.label_B.text()+" C、"+self.ui.label_C.text()+" D、"+self.ui.label_D.text())
        # input_word.send_keys("你好")
        browser.find_element(By.ID,'search_icon').click()
        time.sleep(100)
        # browser.quit()
    def run(self):
        self.AskBing()


if __name__ == "__main__":
    import sys

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM question")
    datas = cur.fetchall()
    cur.close()
    conn.close()

    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())