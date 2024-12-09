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


