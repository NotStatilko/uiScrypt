from PyQt5 import QtWidgets, QtCore
from ui_Scrypt import Ui_mainWindow
from hashlib import scrypt
from sys import exit as sys_exit
from base64 import urlsafe_b64encode

class uiScrypt(QtWidgets.QMainWindow):
    def __init__(self):
        super(uiScrypt, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.label_12.hide() #invalid config
        self.ledits = {
            self.ui.label_12: self.ui.lineEdit,
            self.ui.label_10: self.ui.lineEdit_2,
            self.ui.label_9:  self.ui.lineEdit_3,
        }
        for i in self.ledits:
            i.hide()

        self.ui.pushButton_2.hide() #generate another
        self.ui.label_7.hide() #in process label

        self.ui.label_8.hide() #resulted password
        self.ui.lineEdit_4.hide() #resulted readonly password

        #make password button is pushButton
        #generate password is label_5

        self.ui.pushButton.clicked.connect(self.make_password_clicked)
        self.ui.pushButton_2.clicked.connect(self.erase_to_start)

        self.ui.radioButton.clicked.connect(self.show_text)
        self.ui.radioButton_2.clicked.connect(self.show_text)

        self.ui.pushButton.setDefault(True)
        self.ui.pushButton_2.setDefault(True)

        for i in self.ledits.values():
            i.textChanged.connect(self.hide_with_edit)

        self.ui.lineEdit_5.textChanged.connect(self.hide_with_edit)
        self.ui.lineEdit_6.textChanged.connect(self.hide_with_edit)

        self.all_is_valid = True

    def show_text(self):
        d = {
            self.ui.lineEdit_2: self.ui.radioButton,
            self.ui.lineEdit_3: self.ui.radioButton_2
        }
        for k,v in d.items():
            if v.isChecked():
                k.setEchoMode(0)
            else:
                k.setEchoMode(2)

    def hide_all_empty_errors(self):
        for i in self.ledits: i.hide()

    def make_password_clicked(self):
        self.hide_all_empty_errors()
        for k,v in self.ledits.items():
            if not v.text():
                k.show(); self.all_is_valid = False
        try:
            n = int(self.ui.lineEdit_6.text())
            r = int(self.ui.lineEdit_5.text())
            p = int(self.ui.lineEdit.text())
            self.all_is_valid = True
        except:
            self.all_is_valid = False
            self.ui.label_12.show()

        if self.all_is_valid:
            self.ui.pushButton.hide()
            self.ui.label_5.hide()
            self.ui.label_7.show()
            self.ui.lineEdit_4.show()
            try:
                key = scrypt(
                    password = self.ui.lineEdit_2.text().encode(),
                    salt = self.ui.lineEdit_3.text().encode(),
                    n = n, r = r, p = p, dklen=32,
                    maxmem = 128 * r * (n + p + 2)
                )
            except:
                self.erase_to_start()
                self.ui.label_12.show()
                self.all_is_valid = False
            else:
                self.ui.label_7.hide()
                self.ui.label_8.show()
                self.ui.lineEdit_4.setText(urlsafe_b64encode(key).decode())
                self.ui.lineEdit_4.show()
                self.ui.pushButton_2.show()

    def hide_with_edit(self):
        self.hide_all_empty_errors()

    def erase_to_start(self):
        self.ui.label_7.hide()
        self.ui.label_12.hide()
        self.ui.pushButton_2.hide()
        self.ui.label_8.hide()
        self.ui.lineEdit_4.hide()
        self.ui.label_5.show()
        self.ui.pushButton.show()

    def closeEvent(self,event):
        self.close(); sys_exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = uiScrypt()
    application.show()

    sys_exit(app.exec())
