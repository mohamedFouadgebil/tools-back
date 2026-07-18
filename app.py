from PyQt5 import QtWidgets
from core.keylogger import KeyLogger
from core.reverse_shell import ReverseShell
from core.network_scanner import NetworkScanner
from utils.legal_warning import legal_warning
from core.encryption_tool import EncryptionTool
from core.arp_spoof import ARPSpoof
import sys

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Red Phantom OPS X")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.keylogger_btn = QtWidgets.QPushButton("Run Keylogger", self)
        self.keylogger_btn.setGeometry(50, 50, 200, 50)
        self.keylogger_btn.clicked.connect(self.run_keylogger)

        self.reverse_btn = QtWidgets.QPushButton("Run Reverse Shell", self)
        self.reverse_btn.setGeometry(50, 120, 200, 50)
        self.reverse_btn.clicked.connect(self.run_reverse_shell)

        self.network_btn = QtWidgets.QPushButton("Run Network Scanner", self)
        self.network_btn.setGeometry(50, 190, 200, 50)
        self.network_btn.clicked.connect(self.run_network)

    def run_keylogger(self):
        legal_warning("Keylogger")
        kl = KeyLogger()
        kl.start()

    def run_reverse_shell(self):
        legal_warning("Reverse Shell")
        rs = ReverseShell()
        rs.start()

    def run_network(self):
        legal_warning("Network Scanner")
        ns = NetworkScanner()
        ns.start()
    
    def run_encryption(self):
        et = EncryptionTool()
        msg = "Hello Red Phantom"
        enc = et.encrypt(msg)
        print("Encrypted:", enc)
        dec = et.decrypt(enc)
        print("Decrypted:", dec)

    def run_arp(self):
        arp = ARPSpoof()
        arp.start("192.168.1.1")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
