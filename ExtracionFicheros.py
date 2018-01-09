import Entitys as entity

import sys, os

def ObtenerFicheros(path):

   out=list()

   ficheros = os.listdir(path)

   for fichero in ficheros:
      Nombre=fichero
      FechaActua=os.stat(path+"\\"+Nombre).st_ctime.strftime("%d/%m/%Y /%H/%M/%S")
      Path=path+"\\"+Nombre

      print  Nombre,FechaActua,Path



def main():
   ObtenerFicheros("C:\Generador_Escenarios\GE_PSSE\Fich_Entrada\eSIOS\Demanda")




if __name__ == '__main__':
   main()







