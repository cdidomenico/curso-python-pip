import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    # r.text es de tipo string, que parece una lista de diccionarios
    #r.json() transforma r.text en una lista que python puede manipular
    categories = r.json()
    for category in categories:
        print(category['name'])