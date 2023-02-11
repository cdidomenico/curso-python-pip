#solucion propuesta grafico torta de población sudamerica
#todos los print los he usado para probar la ejecucion 
#de los diferentes coponentes del programa
import csv
import grafico

def read_csv (path):
  with open (path,  'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    #print('reader ', reader)
    header = next(reader)
    print(header)
    #se inicializan las listas de datos para el grafico
    pais = []
    porcentaje = []
    for row in reader :
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      #es un diccionario hecho por una fila del file csv
      if country_dict['Continent'] == 'South America':
        #se grafican datos solo de sudamerica
        pais.append(country_dict['Country/Territory'])
        porcentaje.append(country_dict['World Population Percentage'])
        #se escriben las listas para el grafico
    #print('country_dict', country_dict)
    #print('pais ', pais)
    #print('porcentaje', porcentaje)
    #grafico.py es una copia del charts.py original
    grafico.generate_pie_chart(pais, porcentaje)  
    
if __name__== '__main__':
  data = read_csv('app/data.csv')
