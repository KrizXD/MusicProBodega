import requests

def obtener_saludo():
    url = 'https://musicpro.bemtorres.win/api/v1/test/saludo'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Genera una excepción si la respuesta tiene un código de estado no exitoso
        data = response.json()
        saludo = data.get('message')
        if saludo:
            return saludo
    except requests.exceptions.RequestException:
        pass

    return 'Error al obtener el saludo';




def obtener_productos():
    url = 'https://musicpro.bemtorres.win/api/v1/bodega/producto'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Genera una excepción si la respuesta tiene un código de estado no exitoso
        data = response.json()
        productos = data.get('productos')
        if productos:
            return productos
    except requests.exceptions.RequestException:
        pass

    return 'Error al obtener los productos';
