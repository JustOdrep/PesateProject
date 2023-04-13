from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import json
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, SelectField, IntegerField, validators
from wtforms.validators import DataRequired



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

lista_productos = ['Harina 0000', 'Azucar', 'Leche', 'Manteca', 'Yema', 'Huevo']

#TODO: holaa

@app.route("/")
@app.route("/home")
def home():
    title='Home'
    return render_template('home.html', title=title)

'''
FORM PARA AGREGAR RECETAS
'''

class RecetasForm(FlaskForm):
    receta = StringField('Receta', validators=[DataRequired()])
    ingrediente=SelectField('Ingrediente:', choices=[])
    peso = IntegerField('Peso:')
    submit = SubmitField('Guardar Receta')

   

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
    return render_template('recetas.html', title=title, lista_productos=lista_productos, form=form)



if __name__ == '__main__':
    app.run(debug=True)

