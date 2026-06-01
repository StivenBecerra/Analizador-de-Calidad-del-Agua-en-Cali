from PyQt5.QtWidgets import *
import sys
def main():
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(800,600)
    win.setWindowTitle('Analizador de Calidad del Agua en Cali')
    layout = QHBoxLayout()
    btn = QPushButton('Enviar')
    Entre_1= QPushButton("Funcionalidades Entrega 1")
    Entre_2= QPushButton("Funcionalidades Entrega 2")

    for i in [Entre_1, Entre_2]:
        layout.addWidget(i)
    win.setLayout(layout)
    win.show()
    sys.exit(app.exec_())
