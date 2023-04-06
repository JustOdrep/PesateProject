from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)


lista_productos = ['Harina 0000', 'Azucar', 'Leche', 'Manteca', 'Yema', 'Huevo']

#TODO: holaa

@app.route("/")
@app.route("/home")
def home():
    title='Home'
    return render_template('home.html', title=title)


@app.route("/recetas")
def recetas():
    title = 'Recetas'

    return render_template('recetas.html', title=title, lista_productos=lista_productos)



if __name__ == '__main__':
    app.run(debug=True)

