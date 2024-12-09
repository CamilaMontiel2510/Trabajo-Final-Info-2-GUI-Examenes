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

%...







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
