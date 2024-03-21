from PySide6.QtWidgets import (QApplication,  QWidget, QLabel)
from PySide6 import QtCore
from Gerador import Ui_Form
import sys
import random

class Tela_main(QWidget, Ui_Form):
    def __init__(self):
        super(Tela_main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Gerador de Senhas Python')
        self.botoes()

    def botoes(self):
        self.btn_gerar.clicked.connect(self.gerarSenha)

    def gerarSenha(self):
        self.txt_senha.setStyleSheet(u"border: none; color: black; font-size: 20px;")
        
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
        newString = ""
        for c in range(12):
            index = random.randint(0, len(text))
            letter = text[index - 1]
            newString +=  letter
        self.txt_senha.setText(newString)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tela_main()
    window.show()
    app.exec()