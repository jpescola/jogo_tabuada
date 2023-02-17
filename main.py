import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def novo():
    global r
    # criando os botões de resposta
    while True:
        print('gerando respostas...')

        v1 = round(random.random() * 7) + 2
        v2 = round(random.random() * 7) + 2
        r = v1 * v2
        t.lblDesafio.setText(str(v1) + ' x ' + str(v2))

        vr = [r, r - v1, r + v2]
        print(vr)
        if vr[0] != vr[1] and vr[0] != vr[2] and vr[1] != vr[2]:
            break

    random.shuffle(vr)

    t.btn1.setText(str(vr[0]))
    t.btn2.setText(str(vr[1]))
    t.btn3.setText(str(vr[2]))


def atualizar():
    global jogadas, acertos
    t.lblPontos.setText(str(acertos))
    t.lblJogadas.setText(str(jogadas))


def acertou():
    global jogadas, acertos
    print('acertou')
    t.lblResultado.setText('Acertou! :D')
    jogadas += 1
    acertos += 1
    atualizar()
    novo()


def errou():
    global jogadas
    print('errou')
    t.lblResultado.setText('Errou :(')
    jogadas += 1
    atualizar()
    novo()


def evento1():
    print(t.btn1.text(), r, int(t.btn1.text()) == r)
    if int(t.btn1.text()) == r:
        acertou()
    else:
        errou()


def evento2():
    print(t.btn2.text(), r, int(t.btn2.text()) == r)
    if int(t.btn2.text()) == r:
        acertou()
    else:
        errou()


def evento3():
    print(t.btn3.text(), r, int(t.btn3.text()) == r)
    if int(t.btn3.text()) == r:
        acertou()
    else:
        errou()


# inicializando as variáveis
v1 = 0
v2 = 0
r = 0
jogadas = 0
acertos = 0

# inicializando a janela
Form, Window = uic.loadUiType("tela.ui")
app = QApplication([])
window = Window()
t = Form()
t.setupUi(window)  # carrega os componentes

# define os eventos dos botões
t.btn1.clicked.connect(evento1)
t.btn2.clicked.connect(evento2)
t.btn3.clicked.connect(evento3)

# inicializa o jogo
novo()

# apresenta a janela
window.show()
app.exec()
