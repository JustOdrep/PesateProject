import requests
from bs4 import BeautifulSoup


#Da el precio por k o por unidad. Ej: Harin en kg, Leche en 1lt, 
def producto_precio(producto, url):
    """
    Da el precio por k o por unidad. Ej: Harin en kg, Leche en 1lt, 

    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #El cacao amargo no lo venden en dia asi que tiene un scrapping aparte
    if producto == 'Cacao en polvo':
        price_element = soup.find('p', {'class': 'product-detail-price'})
        if price_element:
            price = price_element.text.strip()
            #El strip de arriba te devuelve un string : $ 4,320
            price = int(price.replace("$", "").replace(",", "")) #Arregla el string
            return {producto : price}
    else:
        price_element = soup.find('span', {'class': 'vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last'})

    if price_element:
        price = price_element.text.strip()
        return {producto : price}
    else:
        print(f"No se pudo encontrar el precio de {producto}")
    




#DICCIONARIO PRODUCTOS CON SU LINK:

#Productos para agregar
"""
Gelatina sin sabor
Harina Leudante
Azucar mascabo
Azucar rubia
Coco rallado
"""
#Por ahora no estan caidos :D
nuevo ={
'Harina 0000': 'https://diaonline.supermercadosdia.com.ar/harina-0000-morixe-1-kg-258543/p',
'Harina 000': 'https://diaonline.supermercadosdia.com.ar/harina-000-caserita-1-kg-54869/p',
'Azúcar': 'https://diaonline.supermercadosdia.com.ar/azucar-ledesma-refinado-superior-1-kg-129208/p',
'Huevos': 'https://diaonline.supermercadosdia.com.ar/huevo-blanco-grande-6-un-31924/p',
'Manteca': 'https://diaonline.supermercadosdia.com.ar/manteca-tonadita-extra-calidad-200-gr-236478/p',
'Levadura en cubo': 'https://diaonline.supermercadosdia.com.ar/levadura-calsa-50-gr-13821/p',
'Levadura en sobre': 'https://diaonline.supermercadosdia.com.ar/levadura-seca-levex-20-gr-47618/p',
'Bicarbonato de sodio': 'https://diaonline.supermercadosdia.com.ar/bicarbonato-de-sodio-la-parmesana-50-gr-268136/p',
'Polvo para hornear': 'https://diaonline.supermercadosdia.com.ar/polvo-para-hornear-la-parmesana-50-gr-268137/p',
'Sal': 'https://diaonline.supermercadosdia.com.ar/sal-fina-dia-500-gr-55538/p',
'Leche': 'https://diaonline.supermercadosdia.com.ar/leche-parcialmente-descremada-liviana-la-serenisima-sachet-1-lt-20499/p',
'Vainillas': 'https://diaonline.supermercadosdia.com.ar/galletitas-vainillas-dia-148-gr-272350/p',
'Nueces': 'https://diaonline.supermercadosdia.com.ar/nuez-pelada-sueno-verde-300-gr-292331/p',
'Chocolate': 'https://diaonline.supermercadosdia.com.ar/chocolate-para-taza-dia-100-gr-60287/p',
'Crema de leche': 'https://diaonline.supermercadosdia.com.ar/crema-de-leche-la-serenisima-para-cocinar-330-gr-274209/p',
'Queso crema': 'https://diaonline.supermercadosdia.com.ar/queso-casancrem-entero-480-gr-172938/p',
'Azúcar impalpable': 'https://diaonline.supermercadosdia.com.ar/azucar-impalpable-dia-250-gr-60282/p',
'Miel': 'https://diaonline.supermercadosdia.com.ar/miel-de-abejas-dia-210-gr-24050/p',
'Maizena': 'https://diaonline.supermercadosdia.com.ar/almidon-de-maiz-maizena-sin-tacc-550-gr-279845/p',
'Aceite': 'https://diaonline.supermercadosdia.com.ar/aceite-de-girasol-natura-15-lts-78856/p',
'Azucar Rubia':'https://diaonline.supermercadosdia.com.ar/azucar-rubia-mascabo-ledesma-800-gr-263408/p',
'Harina Leudante':'https://diaonline.supermercadosdia.com.ar/harina-leudante-morixe-1-kg-258551/p',
'Dulce de Leche Repostero': 'https://diaonline.supermercadosdia.com.ar/dulce-de-leche-repostero-la-serenisima-400-gr-227719/p',
'Maiz Pisingallo': 'https://diaonline.supermercadosdia.com.ar/maiz-pisingallo-granero-400-gr-274326/p',
'Cacao en polvo': 'https://www.boticadelpastelero.com.ar/producto/cacao-amargo-en-polvo-n56-x-1-kg-fenix/2494',
'Avena': f'https://diaonline.supermercadosdia.com.ar/avena-instantanea-quaker-500-gr-292386/p'

}






#Estos links estan todos caidos
dict_producto_link = {
'Harina 0000': 'https://diaonline.supermercadosdia.com.ar/harina-0000-morixe-1-kg-258543/p',
'Harina 000': 'https://diaonline.supermercadosdia.com.ar/harina-000-caserita-1-kg-54869/p',
'Azúcar': 'https://diaonline.supermercadosdia.com.ar/azucar-light-puria-1-kg-46940/p',
'Huevos': 'https://diaonline.supermercadosdia.com.ar/huevo-blanco-granja-loma-verde-6-unidades-51484/p',
'Manteca': 'https://diaonline.supermercadosdia.com.ar/manteca-pakal-200-g-48107/p',
'Levadura': 'https://diaonline.supermercadosdia.com.ar/levadura-fleischmann-seca-8-g-217732/p',
'Bicarbonato de sodio': 'https://diaonline.supermercadosdia.com.ar/bicarbonato-de-sodio-efic-80-g-54474/p',
'Polvo para hornear': 'https://diaonline.supermercadosdia.com.ar/polvo-royal-para-hornear-85-g-14874/p',
'Sal': 'https://diaonline.supermercadosdia.com.ar/sal-finapureza-bolsa-500-g-31195/p',
'Leche': 'https://diaonline.supermercadosdia.com.ar/leche-entera-la-serenisima-botella-1-l-13949/p',
'Cacao en polvo': 'https://diaonline.supermercadosdia.com.ar/cacao-amargo-morixe-250-g-48710/p',
'Vainilla': 'https://diaonline.supermercadosdia.com.ar/vainilla-liquida-nielsen-200-cc-41039/p',
'Nueces': 'https://diaonline.supermercadosdia.com.ar/nueces-grande-chicas-la-morena-100-g-16760/p',
'Chocolate': 'https://diaonline.supermercadosdia.com.ar/chocolate-semiamargo-arcor-tableta-100-g-450/p',
'Crema de leche': 'https://diaonline.supermercadosdia.com.ar/crema-de-leche-ser-200-cc-24292/p',
'Queso crema': 'https://diaonline.supermercadosdia.com.ar/queso-crema-la-serenisima-290-g-13952/p',
'Azúcar impalpable': 'https://diaonline.supermercadosdia.com.ar/azucar-impalpable-bolsa-1-kg-57317/p',
'Miel': 'https://diaonline.supermercadosdia.com.ar/miel-lata-500-g-15257/p',
'Maizena': 'https://diaonline.supermercadosdia.com.ar/maizena-efic-120-g-56396/p',
'Melaza': f'https://diaonline.supermercadosdia.com.ar/melaza-sofia-bolsa-500-g-16540/p',
'Aceite': f'https://diaonline.supermercadosdia.com.ar/aceite-de-girasol-cocinero-1-l-13752/p',
'Avena': f'https://diaonline.supermercadosdia.com.ar/avena-en-hojuelas-efic-500-g-56378/p'
}