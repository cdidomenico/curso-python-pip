import csv
#leer un archivo csv y entregar un diccionario
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    #Se lees primera fila que será el encabezado
    header = next(reader)
    data = []
    for row in reader:
      #se combina el header con las siguientes filas para 
      #hacer diccionarios
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      #se agregan los diccionarios a la lista
      data.append(country_dict)
      #al final se tiene una lista con lod datos de cada pais en forma de doccionario
      return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  #se imprime primer elemento de la lista,el primer diccionario
  print(data[0])