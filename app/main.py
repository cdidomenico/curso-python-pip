import utils
#lista con diccionarios dentro
data = [
    {
      'Country': 'Colombia',
      'Population': 300
    },
    
    {
      'Country': 'Bolivia',
      'Population': 200
    }
  ]

# se mete todo el codigo dentro de una funcion
# luego solo se ejecuta si es invocada la funcion
def run():
  keys, values = utils.get_population()
  print(keys,values)
  
  
  
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  
  print(result)

# este if incica que si se invoca main desde la terminal se ejecuta run
# de esta manera se puede ejecutar main como un script:  main.py
if __name__ == '__main__':
  run()
  