from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QFileDialog, QVBoxLayout, QWidget
import scipy.io as sio
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap
import os

class VentanaPrincipal(QMainWindow):

    def __init__(self, ppal=None):

        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('Vistas/vista_login.ui', self)
        self.setup()

    def setup(self):

        self.boton_ingresar.clicked.connect(self.iniciarSesion)
        self.boton_ingresar.setAutoDefault(True)

        ruta_imagen = os.path.abspath('Escudo-UdeA.svg.png')  # Usa la ruta correcta de tu imagen
        print(f"Ruta de la imagen: {ruta_imagen}")

        if not os.path.exists(ruta_imagen):
            print("Error: No se encontró la imagen en la ruta especificada")
            return

        # Cargar la imagen en QPixmap
        pixmap = QPixmap(ruta_imagen)
        if pixmap.isNull():
            print("Error: No se pudo cargar la imagen. Revisa el formato o la ruta.")
            return
            
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setScaledContents(True)
        print("Imagen cargada correctamente en QLabel.")
        
def asignarControlador(self, controlador):

        self.__controlador = controlador
    
def iniciarSesion(self):

        usuario = self.nombre_usuario_campo.text()
        contrasena = self.contrasena_campo.text()
        # esta informacion se pasa al controlador
        resultado = self.__controlador.verificarUsuario(usuario, contrasena)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Resultado")

        if resultado is None:

            self.verMenu()

        else:

            msg.setText(resultado)
            msg.show()
            self.nombre_usuario_campo.clear()
            self.contrasena_campo.clear()
            
def verMenu(self):

        self.nombre_usuario_campo.clear()
        self.contrasena_campo.clear()
        ventana_nueva = VentanaMenu(self)
        ventana_nueva.asignarControlador(self.__controlador)
        ventana_nueva.agregarNombre()
        self.hide()
        ventana_nueva.show()
    
class VentanaMenu(QDialog): 

    def __init__(self, ppal=None):

        super().__init__(ppal)
        loadUi("Vistas/vista_menu_principal.ui", self)
        self.__ventanaPadre = ppal
        self.__resultado_lista = []
        self.__controlador = None
        self.setup()

    def setup(self):

        self.boton_mat.clicked.connect(self.verMat)
        self.boton_dicom.clicked.connect(self.verDicom)
        self.boton_usuario.clicked.connect(self.crearUsuario)
        self.boton_salir.clicked.connect(self.salir)
    def agregarNombre(self):

        self.titulo.setText(f'Bienvenida {self.__controlador.obtenerNombre()}')

    def asignarControlador(self, controlador):
        
        self.__controlador = controlador

    def verMat(self):

        ventana_nueva = VistaMat(self)
        ventana_nueva.asignarControlador(self.__controlador)
        self.hide()
        ventana_nueva.show()

    def verDicom(self):

        ventana_nueva = VistaDicom(self)
        ventana_nueva.asignarControlador(self.__controlador)
        self.hide()
        ventana_nueva.show()

    def crearUsuario(self):

        ventana_nueva = VentanaCrearUsuario(self)
        ventana_nueva.asignarControlador(self.__controlador)
        self.hide()
        ventana_nueva.show()
        
    def salir(self):

        self.hide()
        self.__ventanaPadre.show()

class VentanaCrearUsuario(QDialog):

    def __init__(self, ppal=None):

        super().__init__(ppal)
        loadUi("Vistas/vista_crear_usuario.ui", self)
        self.__ventanaPadre = ppal
        self.__resultado_lista = []
        self.setup()

    def setup(self):

        self.boton_crear.clicked.connect(self.crearUsuario)
        self.boton_salir.clicked.connect(self.salir)

    def asignarControlador(self, c):
        self.__controlador = c

    def crearUsuario(self):

        usuario = self.nombre_usuario_campo.text()
        contrasena = self.contrasena_campo.text()
        nombre = self.nombre_campo.text()
        
        resultado = self.__controlador.crearUsuario(usuario, contrasena, nombre)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Resultado")

        msg.setText(resultado)

        if resultado == 'Usuario creado exitosamente':

            self.hide()

            self.__ventanaPadre.show()

        else:

            msg.show()

            self.nombre_usuario_campo.clear()
            self.contrasena_campo.clear()
            self.nombre_campo.clear()

    def salir(self):

        self.hide()
        self.__ventanaPadre.show()
class graficoMat(FigureCanvas):

    def __init__(self, parent=None, width=4, height=2, dpi=100):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)

    def graficarSenal(self, datos):

        self.axes.clear()

        for c in range(datos.shape[0]):

            self.axes.plot(datos[c, :] + c * 25)

        self.axes.set_xlabel('Muestras')
        self.axes.set_ylabel('Voltaje (uV)')
        self.axes.set_title('Señales EEG')

        self.draw()
class VistaMat(QDialog):

    def __init__(self, ppal=None):

        super().__init__(ppal)
        loadUi("Vistas/vista_mat.ui", self)
        self.__ventanaPadre = ppal
        self.__j = 0
        self.setup()
        
    def asignarControlador(self, c):

        self.__controlador = c

    def setup(self):

        self.__campo_grafico = graficoMat(self, width=6, height=4.7, dpi=100)
        
        self.layout.addWidget(self.__campo_grafico)

        self.boton_original.setEnabled(False)
        self.boton_promedio.setEnabled(False)
        self.boton_proyeccion.setEnabled(False)
        self.boton_siguiente.setEnabled(False)
        self.boton_anterior.setEnabled(False)

        self.boton_salir.clicked.connect(self.salir)
        self.boton_nuevo.clicked.connect(self.cargarArchivo)
        self.boton_original.clicked.connect(self.mostrarOriginal)
        self.boton_promedio.clicked.connect(self.mostrarPromedio)
        self.boton_proyeccion.clicked.connect(self.mostrarProyeccion2D)
        self.boton_siguiente.clicked.connect(self.mostrarSiguiente)
        self.boton_anterior.clicked.connect(self.mostrarAnterior)

    def salir(self):

        self.hide()
        self.__ventanaPadre.show()

    def cargarArchivo(self):

        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir archivo .mat", "./Archivos/mat", "MAT Files (*.mat)")

        if archivo_cargado != '':
            
            #Cargamos los datos
            data = sio.loadmat(archivo_cargado) # Diccionario
            data = data["set"]
            self.__controlador.cargarArchivoMat(data)
            self.x_min = 0
            self.x_max = data.shape[1]

            self.boton_original.setEnabled(True)
            self.boton_promedio.setEnabled(True)
            self.boton_proyeccion.setEnabled(True)
            self.boton_siguiente.setEnabled(True)
            self.boton_anterior.setEnabled(True)

    def mostrarOriginal(self):

        self.__campo_grafico.graficarSenal(self.__controlador.mostrarOriginal())
        self.boton_siguiente.setEnabled(True)
        self.boton_anterior.setEnabled(True)

    def mostrarPromedio(self):

        self.__campo_grafico.graficarSenal(self.__controlador.mostrarPromedio())
        self.boton_siguiente.setEnabled(False)
        self.boton_anterior.setEnabled(False)
      
    def mostrarProyeccion2D(self):

        self.__campo_grafico.graficarSenal(self.__controlador.mostrarProyeccion2D())
        self.boton_siguiente.setEnabled(False)
        self.boton_anterior.setEnabled(False)

    def mostrarSiguiente(self):

        p = self.__controlador.obtenerLista()

        if self.__j < p[0]-1:

            self.boton_anterior.setEnabled(True)

            self.__j=self.__j+1
            self.__campo_grafico.graficarSenal(self.__controlador.mostrarSiguiente(self.__j))

        else:

            self.boton_siguiente.setEnabled(False)

            texto = ("No hay una prueba siguiente")
            msj = QMessageBox.warning(self, "Alerta", texto,  QMessageBox.Ok, QMessageBox.Cancel)         
    def mostrarAnterior(self):
        
        if self.__j > -1:

            self.boton_siguiente.setEnabled(True)

            self.__j = self.__j-1
            self.__campo_grafico.graficarSenal(self.__controlador.mostrarAnterior(self.__j))

        else:

            self.boton_anterior.setEnabled(False)

            texto = ("No hay una prueba anterior")
            msj = QMessageBox.warning(self, "Alerta", texto,  QMessageBox.Ok, QMessageBox.Cancel) 


class graficoDicom(FigureCanvas):

    def __init__(self, parent= None, width=32, height=30, dpi=100):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.axis("off")        
        FigureCanvas.__init__(self, self.fig)
    
    def graficarImagen(self, datos):

        self.axes.clear()
        self.axes.axis("off")
        self.axes.imshow(datos)
        self.axes.figure.canvas.draw()

    def limpiarImagen(self):

        self.axes.clear()
        self.axes.axis("off")
        self.axes.figure.canvas.draw()

class VistaDicom(QDialog):

    def __init__(self, ppal=None):

        super().__init__(ppal)
        loadUi("Vistas/vista_dicom.ui", self)
        self.__ventanaPadre = ppal
        self.setup()

    def asignarControlador(self, controlador):

        self.__controlador = controlador

    def setup(self):

        self.boton_salir.clicked.connect(self.salir)
        self.boton_nuevo.clicked.connect(self.cargarImagen)
        self.boton_contraste.clicked.connect(self.obtenerImagenContrastada)
        self.boton_suavizada.clicked.connect(self.obtenerImagenSuavizada)
        self.boton_bordes.clicked.connect(self.obtenerImagenBordes)
        self.boton_original.clicked.connect(self.obtenerImagenOriginal)
        
        self.graf = graficoDicom(self, width=8, height=5, dpi=100)
        self.layout.addWidget(self.graf)

        self.boton_contraste.setEnabled(False)
        self.boton_suavizada.setEnabled(False)
        self.boton_bordes.setEnabled(False)
        self.boton_original.setEnabled(False)

    def salir(self):

        self.hide()
        self.__ventanaPadre.show()
    
    def cargarImagen(self):

        file, _  = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo .dcm", "./Archivos/dcm", "DICOM Files (*.dcm)")

        if file != '':

            self.boton_original.setEnabled(False)

            y = self.__controlador.cargarImagen(file)
            self.graf.graficarImagen(y)

            self.datos_paciente.setText(self.__controlador.obtenerDatosPaciente())

            self.boton_contraste.setEnabled(True)
            self.boton_suavizada.setEnabled(True)
            self.boton_bordes.setEnabled(True)
            self.boton_original.setEnabled(True)

        else:

            pass

    def obtenerImagenContrastada(self):

        self.boton_contraste.setEnabled(False)
        self.boton_suavizada.setEnabled(True)
        self.boton_bordes.setEnabled(True)
        self.boton_original.setEnabled(True)

        y = self.__controlador.obtenerImagenContrastada()

        self.graf.graficarImagen(y)

    def obtenerImagenSuavizada(self):

        self.boton_contraste.setEnabled(True)
        self.boton_suavizada.setEnabled(False)
        self.boton_bordes.setEnabled(True)
        self.boton_original.setEnabled(True)

        y = self.__controlador.obtenerImagenSuavizada()

        self.graf.graficarImagen(y)

    def obtenerImagenBordes(self):

        self.boton_contraste.setEnabled(True)
        self.boton_suavizada.setEnabled(True)
        self.boton_bordes.setEnabled(False)
        self.boton_original.setEnabled(True)

        y = self.__controlador.obtenerImagenBordes()

        self.graf.graficarImagen(y)

    def obtenerImagenOriginal(self):

        self.boton_contraste.setEnabled(True)
        self.boton_suavizada.setEnabled(True)
        self.boton_bordes.setEnabled(True)
        self.boton_original.setEnabled(False)

        y = self.__controlador.obtenerImagenOriginal()

        self.graf.graficarImagen(y)