from PyQt5.QtWidgets import *
import sys

from modulos.guardar_csv import guardar_resultados

# aqui vamos a almacenar los resultados obtenidos por búsquedas, filtros, análisis
resultados_actuales = []


def exportar_csv():

    global resultados_actuales

    if not resultados_actuales:

        QMessageBox.warning(None, "Advertencia", "No hay resultados para exportar")
        return

    guardar_resultados(resultados_actuales)

    QMessageBox.information(None, "Exportación", "Resultados exportados correctamente")


def main():

    # crear ventana
    app = QApplication(sys.argv)

    win = QWidget()
    win.resize(800, 600)
    win.setWindowTitle('Analizador de Calidad del Agua en Cali')

    layout = QGridLayout()

    # Agregar botones
    Fun = QLabel("Funcionalidades Disponibles:")

    Entre_1 = QPushButton("Entrega 1")
    Entre_2 = QPushButton("Entrega 2")

    B_export = QPushButton("Exportar CSV")

    B_exit = QPushButton("Salida")

    layout.addWidget(Fun, 0, 0)

    layout.addWidget(Entre_1, 1, 0)
    layout.addWidget(Entre_2, 1, 1)

    layout.addWidget(B_export, 3, 0)
    layout.addWidget(B_exit, 3, 1)

    # Funciones botones
    B_export.clicked.connect(exportar_csv)
    B_exit.clicked.connect(win.close)

    win.setLayout(layout)
    win.show()

    sys.exit(app.exec_())


main()
