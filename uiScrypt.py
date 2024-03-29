from qrcode import QRCode

from ui_Scrypt import Ui_mainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap

from hashlib import scrypt as scrypt_, sha256
from sys import exit as sys_exit, argv as sys_argv

from os import cpu_count
from base64 import urlsafe_b64encode

from multiprocessing import Process, Queue
from random import randrange # We will use it with prbg for animation.


# Will be used for generating passwords fingerprints in App Title
SALT = bytes.fromhex('3e430bceacb85e6cfca2bf10d18c8f82')

# Pseudo random bytes generator
prbg = lambda x: bytes([randrange(255) for _ in range(x)])

def scrypt(queue: Queue, **kwargs) -> None:
    '''Will put resulted key to the queue.'''
    s = scrypt_(**kwargs)
    queue.put(s)
    
class uiScrypt(QtWidgets.QMainWindow):
    def __init__(self):
        super(uiScrypt, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        if len(sys_argv[1:]) >= 3:
            self.ui.lineEdit_6.setText(sys_argv[1]) # N
            self.ui.lineEdit_5.setText(sys_argv[2]) # R
            self.ui.lineEdit.setText(sys_argv[3])   # P
        
        self.ui.label_12.hide() #invalid config

        self.ledits = {
            self.ui.label_12: self.ui.lineEdit,
            self.ui.label_10: self.ui.lineEdit_2,
            self.ui.label_9:  self.ui.lineEdit_3,
        }
        for i in self.ledits:
            i.hide()
        
        self.ui.lineEdit_2.setFocus()
        
        self.ui.pushButton_2.hide() #generate another
        self.ui.label_7.hide() #in process label

        self.ui.label_8.hide() #resulted password
        self.ui.lineEdit_4.hide() #resulted readonly password

        #make password button is pushButton
        #generate password is label_5

        self.ui.pushButton_3.hide() # QR Code view
        self.ui.pushButton_4.hide() # Close QR Code view
        self.ui.qr_mask_label.hide()
        
        self.ui.pushButton.clicked.connect(self.make_password_clicked)
        self.ui.pushButton_2.clicked.connect(self.erase_to_start)
        self.ui.pushButton_3.clicked.connect(self.as_qr_clicked)
        self.ui.pushButton_4.clicked.connect(self.return_back_from_qr)

        self.ui.radioButton.clicked.connect(self.show_text)
        self.ui.radioButton_2.clicked.connect(self.show_text)
                
        self.ui.pushButton.setDefault(True)
        self.ui.pushButton_2.setDefault(True)
        self.ui.pushButton_3.setDefault(True)
        self.ui.pushButton_4.setDefault(True)

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
    
    def as_qr_clicked(self):
        qr_code = QRCode()
        qr_code.add_data(self.ui.lineEdit_4.text())

        pil_image = qr_code.make_image().get_image()
        pil_image = pil_image.resize((256, 256))

        self.ui.label_2.hide()
        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.label_5.hide()
        self.ui.label_7.hide()
        self.ui.label_8.hide()
        self.ui.label_9.hide()
        self.ui.label_10.hide()
        self.ui.label_12.hide()

        self.ui.lineEdit.hide()
        self.ui.lineEdit_2.hide()
        self.ui.lineEdit_3.hide()
        self.ui.lineEdit_4.hide()
        self.ui.lineEdit_5.hide()
        self.ui.lineEdit_6.hide()

        self.ui.pushButton.hide()
        self.ui.pushButton_2.hide()
        self.ui.pushButton_3.hide()

        self.ui.radioButton.hide()
        self.ui.radioButton_2.hide()

        self.ui.qr_mask_label.setPixmap(pil_image.toqpixmap())
        self.ui.qr_mask_label.show()

        self.ui.pushButton_4.show()
        self.ui.pushButton_4.setFocus()

    def return_back_from_qr(self):
        self.ui.qr_mask_label.hide()
        self.ui.pushButton_4.hide()

        self.ui.label_2.show()
        self.ui.label_3.show()
        self.ui.label_4.show()
        self.ui.label_8.show()

        self.ui.lineEdit.show()
        self.ui.lineEdit_2.show()
        self.ui.lineEdit_3.show()
        self.ui.lineEdit_4.show()
        self.ui.lineEdit_5.show()
        self.ui.lineEdit_6.show()

        self.ui.pushButton_2.show()
        self.ui.pushButton_3.show()

        self.ui.radioButton.show()
        self.ui.radioButton_2.show()

        self.ui.pushButton_3.setFocus()

    def make_password_clicked(self):
        self.hide_all_empty_errors()
        self.all_is_valid = True
        
        for k,v in self.ledits.items():
            if not v.text():
                k.show(); self.all_is_valid = False
        try:
            n = int(self.ui.lineEdit_6.text())
            r = int(self.ui.lineEdit_5.text())
            p = int(self.ui.lineEdit.text())
        except:
            self.all_is_valid = False
            self.ui.label_12.show()

        if self.all_is_valid:
            self.ui.pushButton.hide()
            self.ui.label_5.hide()
            self.ui.label_7.show()
            self.ui.lineEdit_4.show()
            self.ui.lineEdit_4.setFocus()
            try:
                queue = Queue()
                p = Process(
                    target=scrypt, args=(queue,), 
                    kwargs={
                        'password': self.ui.lineEdit_2.text().encode(),
                        'salt': self.ui.lineEdit_3.text().encode(),
                        'n': n, 'r': r, 'p': p, 'dklen': 32,
                        'maxmem': (128 * r * (n + p + 2))
                    }
                ); p.start()
                if cpu_count() < 2:
                    self.ui.lineEdit_4.setText('Please wait...')
                while not queue.qsize():
                    QtCore.QCoreApplication.processEvents()
                    assert not p.exitcode # Will False if invalid Scrypt configuration
                    if cpu_count() > 1:
                        self.ui.lineEdit_4.setText(
                            urlsafe_b64encode(prbg(32)).decode()
                        )
                else:
                    key = queue.get(); p.join()
                    fingerprint = sha256(key + SALT).digest()[:6].hex()

                    _translate = QtCore.QCoreApplication.translate

                    self.setWindowTitle(_translate(
                        "mainWindow", f"uiScrypt [{fingerprint.upper()}]")
                    )
                    self.ui.label_7.hide()
                    self.ui.label_8.show()
                    self.ui.lineEdit_4.setText(urlsafe_b64encode(key).decode())
                    self.ui.lineEdit_4.selectAll()
                    self.ui.lineEdit_4.setFocus()
                    self.ui.lineEdit_4.show()
                    self.ui.pushButton_2.show()
                    self.ui.pushButton_3.show()
            except:
                self.erase_to_start()
                self.ui.label_12.show()

    def hide_with_edit(self):
        self.hide_all_empty_errors()

    def erase_to_start(self):
        self.ui.pushButton_3.hide()
        self.ui.label_7.hide()
        self.ui.label_12.hide()
        self.ui.pushButton_2.hide()
        self.ui.label_8.hide()
        self.ui.lineEdit_4.hide()
        self.ui.label_5.show()
        self.ui.pushButton.show()
        self.ui.lineEdit_2.setFocus()

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("mainWindow", "uiScrypt [000000000000]"))

    def closeEvent(self,event):
        self.close(); sys_exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = uiScrypt()
    application.show()

    sys_exit(app.exec())
