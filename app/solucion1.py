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
      if country_dict['Country/Territory'] == pais:
        #
        #se inizializa el dict country, por ahora vacio
        country = {}
        for x in country_dict:
          if 'Population' in x and 'Percentage' not in x:
            f = x[:4]
            g = int(f)
            print('f', f)
            #es para graficar datos por decenios
            if g % 10 == 0:
              print('ffff', g)
            
              #se va rellenando el dict country
              country.update({g: country_dict[x]})
            #se debe eliminar ultima entrada del dict country
            #country.popitem() ahora no es necesario por if g % 10 ==0:
            #ahora country contiene solo los datos de interes
        print('country ',country)
            
            #se recuperan las claves en una lista 
        claves = list(country.keys())
        claves.reverse()
        print('claves ', claves)
        #cla = []
        #a = len(claves)
        #for x in range(a):
          #z = claves[x]
          #print('claves', z)
          #i = z[:4]
          #y = int(i)
          #print('y ',y)
          #if y % 10 == 0:
          #cla.append(x)
        #print('cla', cla)
        #cla.reverse()

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
        ax.bar(claves, val)
        plt.show()

if __name__== '__main__':
  pais = input('ingrese un nombre de pais en ingles')
  data = read_csv('app/data.csv', pais)
