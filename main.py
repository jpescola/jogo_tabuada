import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class TelaPrincipal(QDialog):
    v1 = 0
    v2 = 0
    r = 0
    jogadas = 0
    acertos = 0

    def __init__(self):
        super(TelaPrincipal, self).__init__()
        loadUi('tela.ui', self)
        jogadas = 0
        acertos = 0

        self.novo()

        self.btn1.clicked.connect(self.evento1)
        self.btn2.clicked.connect(self.evento2)
        self.btn3.clicked.connect(self.evento3)

    def acertou(self):
        print('acertou')
        self.lblResultado.setText('Acertou! :D')
        self.jogadas += 1
        self.acertos += 1
        self.atualizar()
        self.novo()

    def errou(self):
        print('errou')
        self.lblResultado.setText('Errou :(')
        self.jogadas += 1
        self.atualizar()
        self.novo()

    def atualizar(self):
        self.lblPontos.setText(str(self.acertos))
        self.lblJogadas.setText(str(self.jogadas))

    def novo(self):
        # criando os botões de resposta
        while True:
            print('gerando respostas...')

            self.v1 = round(random.random() * 7) + 2
            self.v2 = round(random.random() * 7) + 2
            self.r = self.v1 * self.v2
            self.lblDesafio.setText(str(self.v1) + ' x ' + str(self.v2))

            vr = [self.r, self.r - self.v1, self.r + self.v2]
            print(vr)
            if vr[0] != vr[1] and vr[0] != vr[2] and vr[1] != vr[2]:
                break

        random.shuffle(vr)

        self.btn1.setText(str(vr[0]))
        self.btn2.setText(str(vr[1]))
        self.btn3.setText(str(vr[2]))

    def evento1(self):
        print(self.btn1.text(), self.r, int(self.btn1.text()) == self.r)
        if int(self.btn1.text()) == self.r:
            self.acertou()
        else:
            self.errou()

    def evento2(self):
        print(self.btn2.text(), self.r, int(self.btn2.text()) == self.r)
        if int(self.btn2.text()) == self.r:
            self.acertou()
        else:
            self.errou()

    def evento3(self):
        print(self.btn3.text(), self.r, int(self.btn3.text()) == self.r)
        if int(self.btn3.text()) == self.r:
            self.acertou()
        else:
            self.errou()


app = QApplication(sys.argv)
tela_principal = TelaPrincipal()
w = QtWidgets.QStackedWidget()
w.addWidget(tela_principal)
w.setFixedWidth(497)
w.setFixedHeight(300)
w.setWindowTitle('Jogo da Tabuada')
w.show()
try:
    sys.exit(app.exec_())
except:
    print('Exiting')
