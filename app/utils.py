def get_population():
  keys = ['col', 'bol'] #lista
  values = [300,400] #lista
  return keys, values

def population_by_country(data, country):
  #Se chequea si el dato country está dentro de la lista data
  result = list(filter(lambda item: item['Country'] == country , data))
  return result




  
