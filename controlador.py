from vista import VentanaPrincipal
import sys
from PyQt5.QtWidgets import QApplication
from modelo import Sistema

class Coordinador(object):

    def __init__(self, vista, sistema):

        self.__mi_vista = vista
        self.__mi_sistema = sistema

    def verificarUsuario(self, usuario, contrasena):

        return self.__mi_sistema.verificarUsuario(usuario, contrasena)
    
    def crearUsuario(self, usuario, contrasena, nombre):

        return self.__mi_sistema.crearUsuario(usuario, contrasena, nombre)
    
    def obtenerNombre(self):

        return self.__mi_sistema.obtenerNombre()
    
    def cargarArchivoMat(self, data):

        self.__mi_sistema.asignarDatos(data)

    def mostrarOriginal(self):

        return self.__mi_sistema.mostrarOriginal()

    def mostrarPromedio(self):

        return self.__mi_sistema.mostrarPromedio()
    
    def mostrarProyeccion2D(self):

        return self.__mi_sistema.mostrarProyeccion2D()
    
    def mostrarSiguiente(self, j):

        return self.__mi_sistema.mostrarSiguiente(j)
    
    def mostrarAnterior(self, j):

        return self.__mi_sistema.mostrarAnterior(j)
    
    def obtenerLista(self):

        return self.__mi_sistema.obtenerLista()
    
    def cargarImagen(self, archivo):

        return self.__mi_sistema.cargarDicom(archivo)
    
    def obtenerDatosPaciente(self):

        return self.__mi_sistema.obtenerDatosPaciente()
    
    def obtenerImagenContrastada(self):

        return self.__mi_sistema.obtenerImagenContrastada()

    def obtenerImagenSuavizada(self):

        return self.__mi_sistema.obtenerImagenSuavizada()

    def obtenerImagenBordes(self):

        return self.__mi_sistema.obtenerImagenBordes()

    def obtenerImagenOriginal(self):

        return self.__mi_sistema.obtenerImagenOriginal()
    
class Main():
    
    def __init__(self):
        
        self.__app = QApplication(sys.argv)
        self.__mi_vista = VentanaPrincipal()
        self.__mi_sistema = Sistema()  
        #hacemos enlaces entre las partes
        self.__mi_controlador = Coordinador(self.__mi_vista, self.__mi_sistema)
        self.__mi_vista.asignarControlador(self.__mi_controlador)
           
    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())

p = Main()
p.main() 