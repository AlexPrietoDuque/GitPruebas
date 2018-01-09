import Entitys as entity

import sys, os
import sys
import re
from datetime import datetime as dt


def ObtenerFicheros(path,formato):

   ficheros = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
   list = []

   try:

      for fichero in ficheros:
         try:
            Nombre = fichero
            FechaActua = dt.fromtimestamp(os.stat(path + "\\" + Nombre).st_ctime)
            Path = path + "\\" + Nombre
            match = re.search('\\d{12}', Nombre)
            if match != "None":
               try:
                  fecha_nombre = match.group()
               except Exception as ex:
                  raise Exception("Error al convertir a fomrato fecha la fecha obtnida del nombre")
            else:
               raise Exception("Error al obtener la fecha del nombre del fichero")
            Tipo= ExtaerTipoArchivo(Nombre)


            fileinfo = entity.File(Nombre, FechaActua, Path, fecha_nombre, Tipo)
            list.append(fileinfo)

         except Exception as e:
            print "Unexpected error: {}, {}".format(e, e.__class__)

   except Exception as e:
      print "Unexpected error: {}, {}".format(e,e.__class__)



   return list

def ExtaerTipoArchivo(nombre):

   tipo=str

   for tip in entity.TiposFiles.tipos_ficheros:
      if tip.lower() in str.lower(nombre):
         tipo=tip
         break

   return  tipo

def main():
   files = ObtenerFicheros("C:\Generador_Escenarios\GE_PSSE\Fich_Entrada\\eSIOS\Demanda","txt")
   files_filtered = [f for f in files if 'aro_balance_' in f.Name]
   pass

if __name__ == '__main__':
   main()


