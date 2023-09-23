#!/usr/bin/env python3
import random
from random import randint, choice as rc

from faker import Faker
from faker_food import FoodProvider

from api import app
from api.models import db, Restaurant,Pizza,RestaurantPizza

fake = Faker()
fake.add_provider(FoodProvider)


with app.app_context():
    ''' ----------------R E S T A U R A N T-------------- '''
    Restaurant.query.delete()    
    # using list comprehension to populate
    foods = ['foods','peverages','bites','specials','dessert','breakfast','Pizzas','Burgers','appetizers',]
    restaurant_list = [Restaurant(
        name = fake.unique.company() + f" {random.choice(foods)}"  )
    for i in range(15)
    ]
    db.session.add_all(restaurant_list)
    db.session.commit()


    '''---------------- P I Z Z A --------------------------'''
    Pizza.query.delete()
    # pizzas and their ingredients
    pizza_data = {
    "Pizza Margherita": ["Tomato Sauce", "Mozzarella Cheese", "Fresh Basil", "Olive Oil"],
    "Pepperoni Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni Slices"],
    "Hawaiian Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Ham", "Pineapple"],
    "Vegetarian Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Bell Peppers", "Mushrooms", "Onions", "Olives"],
    "BBQ Chicken Pizza": ["BBQ Sauce", "Mozzarella Cheese", "Grilled Chicken", "Red Onions", "Cilantro"],
    "Meat Lover's Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Sausage", "Bacon", "Ground Beef"],
    "Supreme Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Sausage", "Bell Peppers", "Onions", "Olives"],
    "White Pizza": ["Olive Oil", "Garlic", "Mozzarella Cheese", "Ricotta Cheese", "Parmesan Cheese"],
    "Buffalo Chicken Pizza": ["Buffalo Sauce", "Mozzarella Cheese", "Grilled Chicken", "Red Onions", "Blue Cheese Dressing"],
    "Pesto Pizza": ["Pesto Sauce", "Mozzarella Cheese", "Cherry Tomatoes", "Fresh Basil"],
    "Mushroom Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Mushrooms", "Garlic", "Thyme"],
    "Four Cheese Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Fontina Cheese", "Parmesan Cheese", "Gorgonzola Cheese"],
    "Bacon and Egg Pizza": ["Olive Oil", "Mozzarella Cheese", "Bacon", "Eggs", "Chives"],
    "Spinach and Feta Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Spinach", "Feta Cheese", "Garlic"],
    "Barbecue Bacon Pizza": ["BBQ Sauce", "Mozzarella Cheese", "Bacon", "Red Onions", "Cilantro"]
    }
    
    pizza_name = []
    pizza_ingredient= []
    for pizza in (pizza_data.items()):
        pizza_name.append(pizza[0])
        pizza_ingredient.append(",".join(pizza[1]))
   
    pizza_list = [Pizza(
        name =pizza_name[i],
        ingredients=pizza_ingredient[i])
        
        for i in range(15)
    ]

    db.session.add_all(pizza_list)
    db.session.commit()

