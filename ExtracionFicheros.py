import Entitys as entity

import sys, os
import sys
import re
from datetime import datetime as dt


def ObtenerFicheros(path):

   out=[]

   ficheros = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

   try:
      list = []
      for fichero in ficheros:
         Nombre = fichero
         FechaActua = dt.fromtimestamp(os.stat(path + "\\" + Nombre).st_ctime)
         Path = path + "\\" + Nombre
         m=re.match(Nombre,"[0-9]{11}")


         fileinfo=entity.File(Nombre,FechaActua,Path,"","Prueba") # lechu aprende a gitearr
         #asdsadasdsad

         list.append(fileinfo)

      return list

   except Exception as e:
      print "Unexpected error: {}, {}".format(e,e.__class__)



def main():
   files = ObtenerFicheros("C:\Generador_Escenarios\GE_PSSE\Fich_Entrada\\eSIOS\Demanda")
   files_filtered = [f for f in files if 'aro_balance_' in f.Name]




   pass

#sdfsdfsdfsdfsdfsdfsdfdsfds

if __name__ == '__main__':
   main()







