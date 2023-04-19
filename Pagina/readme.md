
# Pesate  ![hola](static/Logo-png3.png)
Pesate documents recipes and displays the cost of their ingredients in both Argentine pesos and US dollars.

## Table of Contents

- [About](#about)
- [Demo](#demo) 
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](#contributing)

## About
The purpose of this application is to document recipes and display the cost of their ingredients in both Argentine pesos and US dollars.


My goal is to help people who sell pastry recipes generate extra income by using a tool that will help them manage their budget.



## Demo

As this started as a CS50 Final Proyect, here is a short video to present it:
link

## Getting Started
1. Clone it from github
2. In the command line:
    pip install -r requirements.txt
3. In the command line :
    cd Pagina
    py -m flask run 

## Usage
There are 4 different pages in the app, as you can see in the navigation bar:
    ![Navbar](static/NavBar.png)


 ### Calculadora
 * **English:** Calculator.
 * Upon selecting a recipe, shows the cost of the ingredientes.
 * You can select how many times you want to cook the recipe and see the cost of its ingredients.




### Agregar recetas
* **English:** Add recipe.
* Adds a recipe to the database.
* You can choose from a list of 30 ingredients for your recipe.





### Borrar recetas
 * **English:** Delete recipe.
* Deletes a recipe from the database.


### Precios
* **English:** Prices
* Shows a table with he columns:
    * Name: Name of the ingredient.
    * Price: Price per kg/lt or unit in the case of eggs.
    * Link: Link of the supermarket page.  

