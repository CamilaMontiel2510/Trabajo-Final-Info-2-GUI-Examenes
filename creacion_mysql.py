import mysql.connector
import os
cnx = mysql.connector.connect(user='root' , passwd='password', host='localhost')
cursor = cnx.cursor()

# cursor.execute("CREATE DATABASE info2")
cursor.execute("USE info2")

cursor.execute("DROP TABLE IF EXISTS usuarios")
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  nombre_usuario VARCHAR(40) UNIQUE NOT NULL,
  nombre VARCHAR(40) NOT NULL,
  contrasena VARCHAR(40) NOT NULL
  )
""")

cursor.execute("""
INSERT INTO usuarios VALUES
(1, 'camila', 'Camila ... ... ...', '123456'),
(2, 'aleja', 'Aleja ... ... ...', '654321')
""")

# cursor.execute("SELECT * FROM usuarios")

# print(cursor.fetchall())

cnx.commit()
cnx.close()
