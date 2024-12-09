from skimage import filters
from scipy.ndimage import gaussian_filter
from numpy.fft import fft2, fftshift
import numpy as np
import mysql.connector
import os

import pydicom as dc

class Sistema:

    def __init__(self, data=None):

        # Crea la conexión a MySQL

        self.__cnx = mysql.connector.connect(user='root' , passwd='password', host='localhost', database='info2')
        self.__cursor = self.__cnx.cursor()

        # Datos para los archivos .mat

        self.__data = []
        self.__sensores = 0
        self.__etapas = 0
        self.__pruebas = 0

        # Datos para los archivos .dcm

        self.__dicom = None
        self.__dicom_array = None
        self.__datos_paciente = None

        self.__nombre_usuario = None

        if data is not None:
            self.asignarDatos(self, data)
 # USUARIO

    def verificarUsuario(self, nombre_usuario, contrasena):

        busca_usuario = f"SELECT * FROM usuarios WHERE nombre_usuario='{nombre_usuario}'"

        self.__cursor.execute(busca_usuario)

        resultados = self.__cursor.fetchall()

        if len(resultados) == 0:

            return("Usuario no encontrado")

        else:

            busca_contrasena = f"SELECT nombre FROM usuarios WHERE nombre_usuario='{nombre_usuario}' AND contrasena='{contrasena}'"

            self.__cursor.execute(busca_contrasena)

            resultados = self.__cursor.fetchall()

            if len(resultados) == 0:

                return ("Contraseña errónea")

            else:

                self.__nombre_usuario = resultados[0][0].split()[0]
            
                return None
            
    def obtenerNombre(self):

        return self.__nombre_usuario
            
    def crearUsuario(self, nombre_usuario, contrasena, nombre):

        busca_usuario = f"SELECT * FROM usuarios WHERE nombre_usuario='{nombre_usuario}'"

        self.__cursor.execute(busca_usuario)

        resultados = self.__cursor.fetchall()

        if len(resultados) != 0:

            return("Usuario ya existente")

        else:

            crear_usuario = f"""
            INSERT INTO usuarios (nombre_usuario, contrasena, nombre) VALUES
            ('{nombre_usuario}', '{contrasena}', '{nombre}')"""

            self.__cursor.execute(crear_usuario)

            # Para que se confirmen los datos
            
            self.__cnx.commit()

            return("Usuario creado exitosamente")
            
    def asignarDatos(self, data):

        self.__data = data
        self.__sensores = data.shape[0]
        self.__etapas = data.shape[1]
        self.__pruebas = data.shape[2]

    def mostrarOriginal(self):

        return self.__data[:,:,0]
        
    def mostrarPromedio(self):

        x = np.mean(self.__data, 0)

        return np.transpose(x)
    
    def mostrarProyeccion2D(self):

        return np.reshape(self.__data, (self.__sensores, self.__etapas * self.__pruebas), order='F')

    

    
    
    
