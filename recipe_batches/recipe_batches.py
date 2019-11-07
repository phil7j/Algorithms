#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # If there's more required than there are in the ingredients, it won't be able to make any batches, so 0
    if len(recipe) > len(ingredients):
        return 0
    # loop thorugh recipe, match the values from both dicitonaries, and divide the ingredients by the recipe to find how many times it can go in.
    # add divided values into a variable called batches
    batches = []
    for key1, value1 in recipe.items():
        for key2, value2 in ingredients.items():
            if key1 == key2:
                diff = value2 // value1
                if diff > 0:
                    batches.append(diff)
    return min(batches)


print(recipe_batches({'milk': 2}, {'milk': 200}))


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
