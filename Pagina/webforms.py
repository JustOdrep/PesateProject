from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, SelectField, IntegerField, validators
from wtforms.validators import DataRequired, NumberRange
import json
from mercadopago import nuevo



'''
FORM PARA CALCULAR RECETAS
'''

#Abre el recetario.json para ver las recetas guardadas asi las pone en choice
def actualizador_recetas():
    global choice
    choice = ['No hay recetas guardadas']
    try:
        with open("recetario.json", "r") as f:
            dict_recetas = json.load(f)

    # Si el archivo no existe, crear un diccionario vacío
    except FileNotFoundError:
        choice= ['No hay recetas guardadas']

    choice = list(dict_recetas.keys())
    return choice

actualizador_recetas()
class CalcularForm(FlaskForm):
    recetas = SelectField('Receta', choices= choice, default='' )
    unidades = IntegerField('Unidades', validators=[NumberRange(min=1)], default=1 )


    #Init sirve para que se actualice tood el timepo la lista de recetas
    def __init__(self, *args, **kwargs):
            super(CalcularForm, self).__init__(*args, **kwargs)
            self.recetas.choices = choice

    



'''
FORM PARA GUARDAR RECETAS
'''


ingredientes_reposteria = sorted(nuevo)
class RecetasForm(FlaskForm):
    receta = StringField('Receta', validators=[DataRequired()])
    ingrediente=SelectField('Ingrediente:', choices=ingredientes_reposteria)
    peso = IntegerField('Peso:', validators=[NumberRange(min=0)])
    submit = SubmitField('Guardar Receta')


class BorrarRecetasForm(FlaskForm):
    actualizador_recetas()
    
    receta=SelectField('Receta', choices=choice)

    #Init sirve para que se actualice tood el timepo la lista de recetas
    def __init__(self, *args, **kwargs):
            super(BorrarRecetasForm, self).__init__(*args, **kwargs)
            self.receta.choices = choice
    submit = SubmitField('Borrar Receta')


class ActualizarPrecios(FlaskForm):
    submit = SubmitField('Actualizar Precios')




