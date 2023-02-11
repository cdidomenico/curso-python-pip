import csv
#leer un archivo csv y entregar un diccionario
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #Se lee primera fila que será el encabezado
    #porque reader es iterable
    header = next(reader)
    #print('header ',header)
    #['rank','cca3','Country/Territory', .....] es una lista de valores
    data = []
    #se inicializa la lista data[]
    for row in reader:
      #row es una lista ['74','zwe','zimbaue', ......]
      #se combina el header con las siguientes filas para 
      #hacer diccionarios
      iterable = zip(header, row)
      #iterable es un objeto iterable, se debe transformar antes de imprimir
      #con los valores de iterable se crean diccionarios 
      country_dict = {key: value for key, value in iterable}
      #print('country_dict', country_dict)
      #country_dict= {'rank': '36', 'cca3': 'zwe','country/territory': 'Zimbaue', .....}
      #se agregan los diccionarios a la lista
      data.append(country_dict)
      #al final se tiene una lista con los datos de cada pais en forma de diccionario
      #print('********' *5)
      #print(row)
      #data es una lista de diccionarios
    return data

if __name__ == '__main__':
  data = read_csv('./pop/data.csv')
  #se imprime primer elemento de la lista,el primer diccionario
  print(data[0])