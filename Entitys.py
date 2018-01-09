

class File:
   name=""
   date_update=01/01/11
   path=""
   date_name=01/01/11
   tipo=""
   def __init__(self, Name, DateUpdate,Path,DateName,Tipo):
      self.name = Name
      self.date_name = DateUpdate
      self.path=Path
      self.date_namee=DateName
      self.tipo=Tipo


class TiposFiles:
   tipos_ficheros = ('demanda', 'generacion', 'intercambio', 'aro_balance');

