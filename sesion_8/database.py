import mysql.connector
import os

class MySQLDB:
    def __init__(self, host, user, password, database):
      self.host = host
      self.user = user
      self.password = password
      self.database = database
      self.connection = None
      
    def connect(self):
      try:
        if self.connection is None:  
          self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
          )   
          print("Conexión exitosa")   
      except mysql.connector.Error as e:
        print(f"Error mientras se estaba conectando a MySQL {e}")
        
    def disconnect(self):
      if self.connection:
          try:
              self.connection.close()  # Asegúrate de que esta línea se ejecuta correctamente
              self.connection = None
              print("Desconexión exitosa")
          except mysql.connector.Error as e:
              print(f"Error mientras se estaba desconectando de MySQL {e}")
        
    def execute_query(self, query, params=None):
      cursor = self.connection.cursor()
      try:
        if params:
          cursor.execute(query, params)
        else:
          cursor.execute(query)
        self.connection.commit()
        return cursor
      except mysql.connector.Error as e:
        print(f"Error mientras se estaba ejecutando la consulta {e}")
        return None

        

db = MySQLDB(
  "127.0.0.1",
  "root",
  "",
  "testlp"
)

#db.connect()
# categorias = db.execute_query("SELECT * FROM categorias")
# db.disconnect()
