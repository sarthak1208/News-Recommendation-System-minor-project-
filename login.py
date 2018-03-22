# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from welcome import Ui_MainWindow
from signup import Ui_signUp
import sqlite3


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def welcomeWindowShow(self):
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
    def signUpShow(self):
        self.signUpWindow = QtGui.QDialog()
        self.ui = Ui_signUp()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
    def loginCheck(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall()) > 0):
            print("User Found ! ")
            self.welcomeWindowShow()
        else:
            print("User Not Found !")
            self.showMessageBox('Warning','Invalid Username And Password')
        connection.close()
        
    def signUpCheck(self):
        print(" Sign Up Button Clicked !")
        self.signUpShow()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(742, 533)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);"))
        self.u_name_label = QtGui.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(130, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName(_fromUtf8("u_name_label"))
        self.pass_label = QtGui.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(130, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(280, 140, 221, 31))
        self.uname_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);"))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.pass_lineEdit = QtGui.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(280, 200, 221, 31))
        self.pass_lineEdit.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.pass_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(220, 270, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        ######################### Button Event ##############################3
        self.login_btn.clicked.connect(self.loginCheck)
        #####################################################################
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(220, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signup_btn.setFont(font)
        self.signup_btn.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        ######################### Button Event ##############################3
        self.signup_btn.clicked.connect(self.signUpCheck)
        #####################################################################
       
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.u_name_label.setText(_translate("Dialog", "USERNAME ", None))
        self.pass_label.setText(_translate("Dialog", "PASSWORD", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))
        self.signup_btn.setText(_translate("Dialog", "Sign Up", None))
        self.label.setText(_translate("Dialog", "News Recommendation System", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

