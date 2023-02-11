import matplotlib.pyplot as plt
#matplotlib se debe instalar para poder usarlo


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()
  

if __name__ =='__main__':
  labels = []
  values = []
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
