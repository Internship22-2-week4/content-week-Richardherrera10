# Escribir una función llamada contrasenaValida que reciba un string y retorne true 
# si el string es igual a "2Fj(jjbFsuj" o "eoZiugBf&g9". De lo contrario debe retornar false.

def contrasenaValida(cadena):
  print('soy contraseña valida')
  print(cadena)
  if cadena == '2Fj(jjbFsuj' or cadena == 'eoZiugBf&g9':
    return print(True)
  else:
    return print(False)



# Escribir una función llamada calcularImpuestos que reciba dos argumentos numéricos: edad e ingresos. 
# Si edad es igual o mayor a 18 y los ingresos son iguales o mayores a 1000 debe retornar ingresos * 40%. 
# De lo contrario retornar 0.

def calcularImpuestos(edad, ingresos):
  if edad >= 18 and ingresos >= 1000:
    return print((ingresos*0.4))
  else:
    return print(0)


# Escribe una función llamada likes que reciba un número y retorne un string utilizando el formato 
# de K para miles y M para millones.

def likes(number):
  if (isinstance(number, int)):
    number = str(number)
  numberRev = number[::-1]
  length = len(numberRev)
  numberNew = ''
  allNums = ''
  for index, digit in enumerate(numberRev):
    if index < 3 and length <= 3:
      return print(f'{number}')
    if index >= 3 and length <= 6:
      numberNew = numberRev.replace(allNums, '')
      return print(f'{numberNew[::-1]}K')
    if (index) >= 6:
      numberNew = numberRev.replace(allNums, '')
      return print(f'{numberNew[::-1]}M')
    else:
      allNums += (digit)

def bmi(peso, altura):
  indiceBMI = round(peso / altura**2,1)
  if indiceBMI < 18.5:
    return print('Bajo de Peso')
  elif indiceBMI > 18.5 and indiceBMI < 24.9:
    return print('Normal')
  elif indiceBMI > 25 and indiceBMI < 29.9:
    return print('Sobrepeso')
  elif indiceBMI >= 30:
    return print('obeso')

class Obra:
  def __init__(self, idObra, tipo, autores, fecha, valor):
    self.idObra = idObra
    self.tipo = tipo
    self.autores = autores
    self.fecha = fecha
    self.valor = valor

class Portafolio:
  def __init__(self, idPortafolio, idObra, fotografias, videos):
    self.idPortafolio = idPortafolio
    self.idObra = idObra
    self.fotografias = fotografias
    self.videos = videos
  def mostrarFotosVideos(self):
    if (self.fotografias == True and self.videos == True):
      return print('Mostrando fotos y videos')
    elif (self.fotografias == True):
      return print('Mostrando fotografias')
    elif (self.videos == True):
      return print('Mostrando videos')


class Exhibicion:
  def __init__(self, idExhibicion, fecha, lugar, descripcion, idPortafolio):
    self.idExhibicion = idExhibicion
    self.fecha = fecha
    self.lugar = lugar
    self.descripcion = descripcion
    self.idPortafolio = idPortafolio
  def mostrarDatosExhibicion(self):
    print(f'Bienvenido a la exhibición de la fecha {self.fecha} en {self.lugar}')

if __name__ == '__main__':
  # contrasenaValida('')
  # calcularImpuestos(30, 500)
  # likes(999)
  # bmi(52, 1.75)
  obraNew = Obra('MR1', 'Escultura', 'Mario Rodrigues', '11/15/1998', 500)
  portafolioN = Portafolio('PORT1', 'MR1', False, True)
  exhibicionN = Exhibicion('EXH1', '7/12/2022', 'Guatemala', 'Exhibicion del escultor Mario Rodrigues', 'PORT1' )
  print(obraNew.__dict__)
  print(portafolioN.__dict__)
  portafolioN.mostrarFotosVideos()
  print(exhibicionN.__dict__)
  exhibicionN.mostrarDatosExhibicion()