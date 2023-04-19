
# Pesate  ![hola](Pagina/static/Logo-png3.png)
### Pesate documents recipes and displays the cost of their ingredients in both Argentine pesos and US dollars.

The idea for the project came from a daily reality that I was experiencing. I run a pastry business where I sell products such as cookies, brownies, cinnamon rolls, and other baked goods. Every time I sold a product, I had to check how much I spent on the supermarket and charge accordingly. Due to my need and passion for technology, I decided to create a webpage that allows users to store recipes and calculates the cost of their ingredients. 

Additionally, I wanted it to allow you to select how many times you want to make that recipe. For example, when I make cookies, I like to make the same recipe three times at once so I can freeze some for later.

Due to the unstable currency in my country, I also decided to calculate the price in dollars to have a better record of my expenses.

The project  took me approximately 20 days and I had to learn the following technologies:

* *SQLAlchemy* to store ingredients. I used a relational table because I wanted all ingredients to have a name, price, and purchase link.
* *WTForm* to simplify the forms.
* I had to refresh my knowledge of *JavaScript* in order to create functions that enable the addition or removal of ingredients from a recipe
* *JSON* to store recipes. Due to the variability of recipes, I felt that a non-relational database was the best way to store them.
* *Flask,  Jinja and Bootstrap* to develop the web-page 
## Table of Contents

- [About](#about)
- [Demo](#demo) 
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Files](#files)

## About
The purpose of this application is to document recipes and display the cost of their ingredients in both Argentine pesos and US dollars.


My goal is to help people who sell pastry recipes generate extra income by using a tool that will help them manage their budget.



## Demo

See my demo in youtube with this [link](https://youtu.be/9vpQ5jjcg7Q).

## Getting Started
1. Clone it from github
2. In the command line:
        pip install -r requirements.txt 
3. In the command line :
    cd Pagina
    py -m flask run 

## Usage
There are 4 different pages in the app, as you can see in the navigation bar:
    ![Navbar](Pagina/static/NavBar.png)


 ### Calculadora
 * **English:** Calculator.
 * Calculates the cost of ingredients for a selected recipe.
 * Allows the user to input the quantity of times they want to cook the recipe, and calculates the total cost accordingly.




### Agregar recetas
* **English:** Add recipe.
* Adds a new recipe to the database.
* Offers a list of 30 ingredients to choose from.






### Borrar recetas
 * **English:** Delete recipe.
* Removes a recipe from the database.


### Precios
* **English:** Prices
*Shows a table with the following columns:
    *Name: Ingredient name.
    *Price: Price per kg/liter or unit (for eggs).
    *Link: Link to the supermarket page.


## Files

### Py files
#### Database
* Created with SQLAlchemy. 
* agregar_ingrediente: Adds an ingredient to the table
* producto_precio:  Web-scrapes the price of a product given its name and URL. Returns a dictionary with the product as the key and the price as the value.
* updatear_precio: Calls all the above functions by first calling producto_precio for web-scraping, then adding the price to the table with agregar_ingrediente.
buscar_ingrediente: Returns the price per kg/lt/unit. This function is used on the home tab when you select an ingredient
#### Dblue
*Uses the DolarSi API to get the selling value for the Dollar Blue.

#### MercadoPago
* Shows the ingredient list in a dictionary with the keys being the product and the values the URL to webscrap
* The list of ingredients is pre-defined, covering most pastry recipe ingredients.
* There is a limitation to which products are on the Dia Page, for example the cocoa powder had to be web-scrapped from another market



#### Webforms
In all webforms i had the problem of having to update the choices of recipes. I had a rare "bug", the recipes only updated when i saved the .py file, i spent days trying to figure out how to make the user to save a file
The solution was actually very simple, with an __init__ function the choices update automatically

### HTML Templates

#### Recetas
* I decided to use a select form for the ingredients for my limitation of not knowing how to have a list of user-inputs 

### Precios
* Two tables are used in the "Prices" feature to minimize scrolling for the 30 ingredients.


Thanks for reading!




