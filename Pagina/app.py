from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_session import Session
import json
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, SelectField, IntegerField, validators
from wtforms.validators import DataRequired
from webforms import RecetasForm, CalcularForm, BorrarRecetasForm, actualizador_recetas
from dblue import dolar_hoy
from database import Base, Ingredientes, agregar_ingrediente, updatear_precios, buscar_ingrediente
import time




app = Flask(__name__)
app.secret_key =b'_5#y2L"F4Q8z\n\xec]/'






#TODO: holaa
@app.route("/")
@app.route("/home" , methods=['GET','POST'])
def home():
    title='Home'
    actualizador_recetas()
    #updatear_precios() #Activar y desactivar si agregas un ingrediente nuevo.
    form = CalcularForm()
    ingredientes=None
    ingredientes_calculados = {}
    total_pesos = 0
    total_usd =0



    if request.method == "POST":
        inicio = time.time()
        receta = request.form.get('recetas')
        #Loadea el diccionario con todas las recetas si existe, y lo crea si no 
        try:
            with open("recetario.json", "r") as f:
                dict_recetas = json.load(f)
        # Si el archivo no existe, crear un diccionario vacío
        except FileNotFoundError:
            dict_recetas = {}
        #Este dict tiene los ingredientes de una receta en particular
        ingredientes = dict_recetas[receta]
        dolar = dolar_hoy()
        for key, values in ingredientes.items():
            #La fx buscar_ingrediente returnea el precio del producto
            precio_scrap = buscar_ingrediente(key)
            if key == 'Huevos': #Los huevos son los unicos que estan scrapeados por unidad
                precio_pesos = int(precio_scrap) * int(values)
            else: #Los ingredientes que no son huevos estan scrapeados en 1000g o 1000ml
                precio_pesos = int(precio_scrap) * int(values) / 1000
                precio_usd = precio_pesos / dolar
            ingredientes_calculados[key] = {
                'peso':values,
                'precio_pesos':precio_pesos,
                'precio_usd': precio_usd
            }
        #Por cada value en ing_calc.values. Buscar con su key 'precio_moneda', ponerlo en una lista y dps sumarlo
        total_pesos = sum([v['precio_pesos'] for v in ingredientes_calculados.values()])
        total_usd = sum([v['precio_usd'] for v in ingredientes_calculados.values()])
        fin = time.time()
        tiempo = fin- inicio

        

        

            
        #La key de ingrediente es harina y el value son 250gramos
        return render_template('home.html', title=title, form = form, ingredientes_calculados=ingredientes_calculados, total_pesos= total_pesos, total_usd=total_usd, tiempo = tiempo)
    return render_template('home.html', title=title, form = form ,ingredientes_calculados=ingredientes_calculados)





   

@app.route("/recetas", methods=['GET','POST'])
def recetas():
    title = 'Recetas'
    form=RecetasForm()
    if request.method == "POST":
        
        #Guarda el nombre de la receta y la flashea
        receta= request.form.get('receta')
        flash(f'Receta de {receta} agregada con exito!', 'success' )
        
        #Guarda las respuestas de los ingredientes y del peso, para despues zipearlos en un dict
        lista_ingredientes = request.form.getlist('ingrediente')
        lista_peso = request.form.getlist('peso')
        dict_receta = dict(zip(lista_ingredientes, lista_peso))

        #Loadea el diccionario con todas las recetas si existe, y lo crea si no 
        try:
            with open("recetario.json", "r") as f:
                dict_recetas = json.load(f)
        # Si el archivo no existe, crear un diccionario vacío
        except FileNotFoundError:
            dict_recetas = {}
        
        #Agrega la nueva receta al dict de recetas
        dict_recetas[receta] = dict_receta

        # Escribe el diccionario actualizado en el archivo "recetario.json"
        with open("recetario.json", "w") as f:
            json.dump(dict_recetas, f)

        #Redirectea
        return redirect(url_for('recetas'))
    return render_template('recetas.html', title=title, form=form)



if __name__ == '__main__':
    app.run(debug=True)

@app.route("/borrar", methods=['GET','POST'])
def borrar():
    title = 'Borrar'
    actualizador_recetas()
    form= BorrarRecetasForm()

    if request.method == "POST":
        receta = request.form.get('receta')
        flash(f'Receta: {receta} quitada con exito!', 'danger' )
        # Abre el  JSON y carga su contenido en una variable de Python
        with open("recetario.json", "r") as f:
            data = json.load(f)

        # Elimina la entrada "email" del diccionario
        try:
            del data[receta]
        except KeyError:
            pass
        # Guarda el diccionario actualizado en el archivo JSON
        with open("recetario.json", "w") as f:
            json.dump(data, f)
        
        return redirect(url_for('borrar'))

    return render_template('borrar.html', title=title, form=form)


@app.route("/about")
def about():
    title='Acerca '
    return render_template('about.html', title=title)


#Variables para jinja
def usd(value):
    """Format value as USD."""
    return f"U$D {value:,.2f}"

def pesos(value):
    """Format value as Pesos."""
    if value <1:
        value = 1
    return f"$ {value:,.0f}"

# Custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.filters["pesos"] = pesos