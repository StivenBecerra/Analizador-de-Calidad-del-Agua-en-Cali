from PyQt5.QtWidgets import *
import sys
def main():
    #crear ventana
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(800,600)
    win.setWindowTitle('Analizador de Calidad del Agua en Cali')
    layout = QGridLayout()

    #Agregar botones
    Fun= QLabel("Funcionalidades Disponibles:")
    Entre_1= QPushButton("Entrega 1")
    Entre_2= QPushButton("Entrega 2")
    layout.addWidget(Entre_1, 1, 0 )
    layout.addWidget(Entre_2, 1, 1)
    layout.addWidget(Fun, 0, 0)

    win.setLayout(layout)
    win.show()
    sys.exit(app.exec_())
main()
