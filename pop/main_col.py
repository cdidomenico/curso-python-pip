import utils
import read_csv
import charts
#clase 40 curso python nicolas molina
def run():
  data = read_csv.read_csv('./pop/data.csv')
  country = input('Type Country => ')
  #print('country ', country)
  
  result = utils.population_by_country(data,country)
  #print('result  ', result)
  if len(result) > 0:
    country = result[0]
    #print('country mmmmm', country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

if __name__== '__main__':
  run()