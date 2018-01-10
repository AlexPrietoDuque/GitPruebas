import ConfigParser

class File:
   name=""
   date_update=01/01/11
   path=""
   date_name=01/01/11
   tipo=""
   def __init__(self, Name, DateUpdate,Path,DateName,Tipo):
      self.name = Name
      self.date_update = DateUpdate
      self.path=Path
      self.date_name=DateName
      self.tipo=Tipo

class TiposFiles:
   tipos_ficheros = ('demanda', 'generacion', 'intercambio', 'aro_balance');

class ParamControl:
   modo_ejecucion=str
   manual=bool
   tipo_escenario=str

   def __init__(self, modo_ejecucion, manual, tipo_escenario):
      self.modo_ejecucion = modo_ejecucion
      self.manual = manual
      self.tipo_escenario = tipo_escenario

def ExtracionParametros (seccion):
   param={}
   try:

      ruta_archivo="config.cfg"
      cfg = ConfigParser.ConfigParser()
      cfg.optionxform = str
      cfg.read([ruta_archivo])

      if not cfg.read([ruta_archivo]):
         print "No existe el archivo"
         raise  EnvironmentError ("No se ha encontrado el archivo de configuracion")
      else:

         secc=cfg.sections()
         secc=[elem for elem in secc if str.lower(elem) in str.lower(seccion)]

         if not cfg.has_section(seccion):
            raise SystemError("No se ha encontrado la seccion indicada {}".format(seccion))
         else:
            param=cfg.items(secc[0])

   except Exception as e:
      print "Unexpected error: Mensaje: {}, TipoError: {}".format(e.message, e.__class__)

   return param



















