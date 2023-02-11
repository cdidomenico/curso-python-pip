import matplotlib.pyplot as plt
import csv

def read_csv (path, pais):
  with open (path,  'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    #print('reader ', reader)
    header = next(reader)
     #print(header)
    #country= {}
    for row in reader :
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      #es un diccionario hecho por una fila del file csv
      #country = {}
      if country_dict['Continent'] == 'South America':
        #
        #se inizializa el dict country, por ahora vacio
        country = {}
        for x in country_dict:
          if 'Population' in x:
            #se va rellenando el dict country
            country.update({x: country_dict[x]})
            #se debe eliminar ultima entrada del dict country
        country.popitem()
            #ahora country contiene solo los datos de interes
        print('country ',country)
            
            #se recuperan las claves en una lista 
        claves = list(country.keys())
        print('claves ', claves)
        cla = []
        a = len(claves)
        for x in range(a):
          z = claves[x]
          print('claves', z)
          i = z[:4]
          y = int(i)
          print('y ',y)
          if y % 10 == 0:
            cla.append(i)
        print('cla', cla)
        cla.reverse()

          #se recuperan los valores en una lista
        
        valores = list(country.values())
        print('valores  ', valores)
        val = []
        for x in range(len(valores)):
          y = valores[x]
          z = int(y)
          val.append(z)

        print('val ', val)
        val.reverse()
        #print('lav', val)       
      
        #print('valores ', valores)

        fig, ax = plt.subplots()
        ax.bar(cla, val)
        plt.show()

if __name__== '__main__':
  pais = input('ingrese un nombre de pais en ingles')
  data = read_csv('app/data.csv', pais)
