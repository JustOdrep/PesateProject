import requests

def dolar_hoy():
    """
    Usando la api de DolarSi, returnea el valor de compra del dolar
    NO SE SI SE ACTUALIZA CON LOS DIAS
    """
    response = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    data = response.json()

    #Next convierte un iterable en el primer item. Si es calleada en el 1er item, lo conviertee en el 2do item y asi blabla

    dolar_blue = next(item for item in data if item['casa']['nombre'] == 'Dolar Blue')
    """   
     La estructura del dolar_blue es:
       {
        "casa": {
            "nombre": "Dolar Blue",
            "compra": "169.00",
            "venta": "179.00"
        }
    """
    venta = dolar_blue['casa']['venta']
    venta = float(venta.replace(',', '.'))

    return venta

