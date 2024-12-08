from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QFileDialog, QVBoxLayout, QWidget
import scipy.io as sio
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class VentanaPrincipal(QMainWindow):

    def __init__(self, ppal=None):

        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('Vistas/vista_login.ui', self)
        self.setup()

    def setup(self):

        self.boton_ingresar.clicked.connect(self.iniciarSesion)
        self.boton_ingresar.setAutoDefault(True)
        
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


