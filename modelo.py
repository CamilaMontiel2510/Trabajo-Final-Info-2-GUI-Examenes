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