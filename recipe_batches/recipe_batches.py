#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_whole_batches = None

    for ingredient in recipe.keys():
        try:
            if recipe[ingredient] > ingredients[ingredient]:
                return 0
            
            if max_whole_batches == None or ingredients[ingredient] // recipe[ingredient] < max_whole_batches:
                max_whole_batches = ingredients[ingredient] // recipe[ingredient]
        except KeyError:
            return 0

    return max_whole_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))