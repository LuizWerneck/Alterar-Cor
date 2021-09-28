from PyQt5 import uic,QtWidgets

def funcao_principal():
    if formulario.azul.isChecked():
        opcao = "Azul"
        background = 'background: rgb(0, 0, 255)'
    elif formulario.amarelo.isChecked():
        opcao = "Amarelo"
        background = 'background: rgb(255, 255, 0)'
    elif formulario.vermelho.isChecked():
        opcao = "Vermelho"
        background = 'background: rgb(255, 0, 0)'
    elif formulario.verde.isChecked():
        opcao = "Verde"
        background = 'background: rgb(0, 255, 0)'
    else:
        opcao = ''

    formulario.corSelecionada.setText(opcao)
    formulario.setStyleSheet(background)


app = QtWidgets.QApplication([])
formulario = uic.loadUi('cores.ui')
formulario.btnEnviar.clicked.connect(funcao_principal)
formulario.show()
app.exec()






