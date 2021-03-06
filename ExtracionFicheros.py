import Entitys as entity

import sys, os
import sys
import re
from datetime import datetime as dt

#11:26
#11:39
#Commint 11:27
def ObtenerFicheros(path,formato):

   ficheros = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
   list = []

   #try:

   for fichero in ficheros:
      try:
         Nombre = fichero
         FechaActua = dt.fromtimestamp(os.stat(path + "\\" + Nombre).st_ctime)
         Path = path + "\\" + Nombre
         match = re.search('\\d{8}', Nombre)
         if match != "None":
            try:

               #fecha_nombre = dt.strptime(match.group(), '%d%m%Y')
               fecha_nombre = match.group()
            except Exception as ex:
               fecha_nombre=""
         else:
            raise Exception("Error al obtener la fecha del nombre del fichero")
         Tipo= ExtaerTipoArchivo(Nombre)


         fileinfo = entity.File(Nombre, FechaActua, Path, fecha_nombre, Tipo)
         list.append(fileinfo)

      except Exception as e:
         print "Unexpected error: Mensaje: {}, TipoError: {}".format(e.message, e.__class__)

   #except Exception as e:
      #print "Unexpected error: {}, {}".format(e,e.__class__)


   return list

def ExtaerTipoArchivo(nombre):

   tipo=str

   for tip in entity.TiposFiles.tipos_ficheros:
      if tip.lower() in str.lower(nombre):
         tipo=tip
         break

   return  tipo

def main():
   files_demanda = ObtenerFicheros("C:\Generador_Escenarios\GE_PSSE\Fich_Entrada\\eSIOS\Demanda","txt")
   #Ordeno el listado por fecha la lista de ficheros de demanda
   files_demanda.sort(key=lambda x: x.date_update, reverse=True)

   RUTA_PY,_= os.path.split(__file__)
   RUTA_GE = os.path.normpath(os.path.join(RUTA_PY, r'..'))




   pass

if __name__ == '__main__':
   main()


