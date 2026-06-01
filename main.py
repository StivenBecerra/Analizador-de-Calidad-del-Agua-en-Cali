from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QHeaderView
import sys
import os
from modulos import logica_funciones
from modulos import logica_historial
from modulos import logica_guardar_csv
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

base = os.path.dirname(__file__)

ruta = os.path.join(
    base,
    "data",
    "Agua_cali_2012_2018_Completo.csv"
)

class VentanaPrincipal(QWidget):

    def __init__(self):
      super().__init__()

      self.datos = logica_funciones.cargar_datos(ruta)

      self.resultados_actuales = []   # <-- agregar

      self.setWindowTitle(
         "Analizador de Calidad del Agua en Cali"
        )

      self.resize(1200, 800)

      self.crear_interfaz()

      self.actualizar_grafico_rios()
      self.actualizar_grafico_ph()

    def crear_interfaz(self):

        layout = QGridLayout()

        # ==========================
        # TITULO
        # ==========================

        titulo = QLabel(
            "Analizador de Calidad del Agua en Cali"
        )

        titulo.setStyleSheet(
            "font-size:18px; font-weight:bold;"
        )

        grupo = QLabel("AquaAnalytics")

        layout.addWidget(titulo, 0, 0, 1, 4)
        layout.addWidget(grupo, 1, 0, 1, 4)

        # ==========================
        # BUSCAR
        # ==========================

        layout.addWidget(QLabel("Buscar:"), 2, 0)

        self.txt_buscar = QLineEdit()

        layout.addWidget(
            self.txt_buscar,
            2,
            1,
            1,
            2
        )

        self.btn_buscar = QPushButton("Buscar")

        layout.addWidget(
            self.btn_buscar,
            2,
            3
        )

        # ==========================
        # FILTRAR
        # ==========================

        layout.addWidget(
            QLabel("Filtrar:"),
            3,
            0
        )

        layout.addWidget(
            QLabel("Columna:"),
            4,
            0
        )

        self.txt_columna = QLineEdit()

        layout.addWidget(
            self.txt_columna,
            4,
            1
        )

        layout.addWidget(
            QLabel("Valor >"),
            4,
            2
        )

        self.txt_valor = QLineEdit()

        layout.addWidget(
            self.txt_valor,
            4,
            3
        )

        self.btn_filtrar = QPushButton(
            "Filtrar"
        )

        self.btn_estadisticas = QPushButton(
            "Estadísticas"
        )

        layout.addWidget(
            self.btn_filtrar,
            5,
            0
        )

        layout.addWidget(
            self.btn_estadisticas,
            5,
            1
        )

        # ==========================
        # AGRUPAR
        # ==========================

        layout.addWidget(
            QLabel("Agrupar:"),
            6,
            0
        )

        layout.addWidget(
            QLabel("Columna:"),
            7,
            0
        )

        self.txt_agrupar = QLineEdit()

        layout.addWidget(
            self.txt_agrupar,
            7,
            1
        )

        self.btn_agrupar = QPushButton(
            "Agrupar"
        )

        layout.addWidget(
            self.btn_agrupar,
            7,
            2
        )

        # ==========================
        # BOTONES AUXILIARES
        # ==========================

        self.btn_columnas = QPushButton(
            "Columnas"
        )

        self.btn_historial = QPushButton(
            "Historial"
        )

        self.btn_archivos = QPushButton(
            "Archivos guardados"
        )

        layout.addWidget(
            self.btn_columnas,
            8,
            0
        )

        layout.addWidget(
            self.btn_historial,
            8,
            1
        )

        layout.addWidget(
            self.btn_archivos,
            8,
            2,
            1,
            2
        )

        # ==========================
        # RESULTADOS
        # ==========================

        lbl_resultados = QLabel(
            "RESULTADOS"
        )

        lbl_resultados.setStyleSheet(
            "font-size:16px; font-weight:bold;"
        )

        layout.addWidget(
            lbl_resultados,
            9,
            0,
            1,
            4
        )

        self.tabla = QTableWidget()

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(
            self.tabla,
            10,
            0,
            1,
            4
        )

        # ==========================
        # GRAFICOS
        # ==========================

        # ==========================
        # GRAFICO 1
        # ==========================

        grafico1 = QGroupBox("Distribución por Río")

        layout_g1 = QVBoxLayout()

        self.fig1 = Figure(figsize=(5,4))
        self.canvas1 = FigureCanvas(self.fig1)

        layout_g1.addWidget(self.canvas1)

        grafico1.setLayout(layout_g1)

        # ==========================
        # GRAFICO 2
        # ==========================

        grafico2 = QGroupBox("Promedio de pH por Río")

        layout_g2 = QVBoxLayout()

        self.fig2 = Figure(figsize=(5,4))
        self.canvas2 = FigureCanvas(self.fig2)

        layout_g2.addWidget(self.canvas2)

        grafico2.setLayout(layout_g2)

        grafico1.setMinimumHeight(250)
        grafico2.setMinimumHeight(250)

        layout.addWidget(
            grafico1,
            11,
            0,
            1,
            2
        )

        layout.addWidget(
            grafico2,
            11,
            2,
            1,
            2
        )

        # ==========================
        # BOTONES INFERIORES
        # ==========================

        self.btn_exportar = QPushButton(
            "Exportar CSV"
        )

        self.btn_salir = QPushButton(
            "Salir"
        )

        layout.addWidget(
            self.btn_exportar,
            12,
            0
        )

        layout.addWidget(
            self.btn_salir,
            12,
            3
        )

        # ==========================
        # CONEXIONES
        # ==========================

        self.btn_buscar.clicked.connect(
            self.buscar
        )

        self.btn_filtrar.clicked.connect(
            self.filtrar
        )

        self.btn_agrupar.clicked.connect(
            self.agrupar
        )

        self.btn_estadisticas.clicked.connect(
            self.estadisticas
        )

        self.btn_columnas.clicked.connect(
            self.mostrar_columnas
        )
        self.btn_exportar.clicked.connect(
          self.exportar_csv
        )

        self.btn_historial.clicked.connect(
           self.mostrar_historial
        )

        self.btn_archivos.clicked.connect(
          self.archivos_guardados
        )

        self.btn_salir.clicked.connect(
            self.close
        )
        self.setLayout(layout)

    # =====================================
    # FUNCIONES DE INTERFAZ
    # =====================================

    def buscar(self):

        termino = self.txt_buscar.text()

        resultados = logica_funciones.buscar(
            self.datos,
            termino
        )

        self.mostrar_tabla(
            resultados
        )

    def filtrar(self):

        columna = self.txt_columna.text()

        valor = self.txt_valor.text()

        resultados = logica_funciones.filtrar(
            self.datos,
            columna,
            valor
        )

        self.mostrar_tabla(
            resultados
        )

    def agrupar(self):

        columna = self.txt_agrupar.text()

        resultados = logica_funciones.agrupar(
            self.datos,
            columna
        )

        self.mostrar_tabla(
            resultados
        )

    def estadisticas(self):

        columna = self.txt_columna.text()

        resultado = logica_funciones.estadisticas(
            self.datos,
            columna
        )

        if resultado is None:

            QMessageBox.warning(
                self,
                "Error",
                "No hay datos válidos"
            )

            return

        QMessageBox.information(
            self,
            "Estadísticas",
            f"Cantidad: {resultado['cantidad']}\n"
            f"Máximo: {resultado['maximo']}\n"
            f"Mínimo: {resultado['minimo']}\n"
            f"Promedio: {resultado['promedio']:.2f}"
        )

    def mostrar_columnas(self):

        columnas = logica_funciones.mostrar_columnas(
            self.datos
        )

        QMessageBox.information(
            self,
            "Columnas disponibles",
            "\n".join(columnas)
        )

    def mostrar_historial(self):

        datos = logica_historial.obtener_historial()

        if not datos:

            QMessageBox.information(
                self,
                "Historial",
                "No hay consultas registradas"
            )

            return

        self.mostrar_tabla(datos)

    def archivos_guardados(self):

        archivos = (
            logica_guardar_csv.obtener_archivos_guardados()
        )

        if not archivos:

            QMessageBox.information(
                self,
                "Archivos",
                "No hay archivos guardados"
            )

            return

        archivo, ok = QInputDialog.getItem(
            self,
            "Archivos guardados",
            "Seleccione un archivo:",
            archivos,
            0,
            False
        )

        if ok:

            datos = (
                logica_guardar_csv.cargar_resultados(
                    archivo
                )
            )

            if datos:

                self.mostrar_tabla(datos)

    def exportar_csv(self):

        if not self.resultados_actuales:

            QMessageBox.warning(
                self,
                "Error",
                "No hay resultados para exportar"
            )

            return

        nombre, ok = QInputDialog.getText(
            self,
            "Guardar CSV",
            "Nombre del archivo:"
        )

        if not ok or not nombre:

            return

        if not nombre.endswith(".csv"):

            nombre += ".csv"

        logica_guardar_csv.guardar_resultados(
            self.resultados_actuales,
            nombre
        )

        QMessageBox.information(
            self,
            "Éxito",
            "Archivo exportado correctamente"
        ) 

    def mostrar_tabla(self, datos):
     
        self.resultados_actuales = datos       
        if not datos:

            QMessageBox.information(
                self,
                "Información",
                "No se encontraron resultados"
            )

            return

        columnas = list(
            datos[0].keys()
        )

        self.tabla.setRowCount(
            len(datos)
        )

        self.tabla.setColumnCount(
            len(columnas)
        )

        self.tabla.setHorizontalHeaderLabels(
            columnas
        )

        for fila, registro in enumerate(datos):

            for columna, clave in enumerate(columnas):

                self.tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(
                        str(registro[clave])
                    )
                )
    def actualizar_grafico_rios(self):

      conteo = {}

      for fila in self.datos:

          rio = fila["Rio"]

          if rio in conteo:
            conteo[rio] += 1
          else:
            conteo[rio] = 1

      self.fig1.clear()
  
      ax = self.fig1.add_subplot(111)

      ax.bar(
        conteo.keys(),
        conteo.values()
      )

      ax.set_title(
        "Cantidad de registros por río"
      )

      ax.tick_params(
        axis="x",
        rotation=45,
        labelsize=8
      )
      self.fig1.tight_layout()
      self.canvas1.draw()


    def actualizar_grafico_ph(self):

       suma = {}
       cantidad = {}

       for fila in self.datos:

          rio = fila["Rio"]

          try:

              ph = float(fila["pH"])

              if rio not in suma:

                  suma[rio] = 0
                  cantidad[rio] = 0

              suma[rio] += ph
              cantidad[rio] += 1

          except:

              pass

       rios = []
       promedios = []

       for rio in suma:

          rios.append(rio)
 
          promedios.append(
              suma[rio] / cantidad[rio]
         )

       self.fig2.clear()

       ax = self.fig2.add_subplot(111)

       ax.bar(
          rios,
          promedios
        )

       ax.set_title(
          "Promedio pH por río"
        )

       ax.tick_params(
          axis="x",
          rotation=45,
          labelsize=8
        )
       self.fig2.tight_layout()
       self.canvas2.draw()

    

def main():

    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()

    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()