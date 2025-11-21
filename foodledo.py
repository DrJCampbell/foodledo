import streamlit as st
import pandas as pd
import os
import random
from time import gmtime, strftime

recipes_dir = './recipes'

# recipe data structure
# pandas dataframes read from csv files in a folder
# folder name is recipe
# - text file for method
# - csv file for ingredients (ingredient,amount,unit)


# page to show current menu
def show_menu():
    pass

# page to show shopping list
def show_shopping():
    # look at the menu
    # read each set of ingredients
    # aggregate (sum) ingredients with the same unit
    pass

# page to create new menu (link from current menu)
def new_menu(recipes_dir = './recipes', n_recipes = 3):
    # list directories in the recipes directory
    # allow to select a subset of recipes
    # store that selection in a file (somewhere)
    print('hello')
    st.write('*** Hello, world!***')
    # get the available recipes
    recipes = os.listdir(recipes_dir)
    # remove non-recipe files starting with a dot
    recipes = [r for r in recipes if not r.startswith('.')]
    # random index to sample recipes
    rnd_index = random.sample(range(len(recipes)), k = n_recipes)
    # create a dict to store the recipes and ingredients
    menu_data = {'recipes': [], 'ingr_unit': {}}
    for i in rnd_index:
        st.write(recipes[i])
        menu_data['recipes'].append(recipes[i])
        ingredients = pd.read_csv(f"{recipes_dir}/{recipes[i]}/ingredients.txt")
        for row in range(ingredients.shape[0]):
            #st.write(row)
            iu_key = f"{ingredients.iloc[row]['ingredient']}_{ingredients.iloc[row,]['unit']}"
            if iu_key in menu_data['ingr_unit']:
                menu_data['ingr_unit'][iu_key] += ingredients.iloc[row]['amount']
            else:
                menu_data['ingr_unit'][iu_key] = ingredients.iloc[row]['amount']    

    # write a menu with a date-stamp and a shopping list
    time_stamp = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
    menu = pd.DataFrame(menu_data['recipes'])
    menu.to_csv(f"menus/menu_{time_stamp}.txt", index=False, header=False)
    shopping_list = pd.Series(menu_data['ingr_unit']).reset_index()
    shopping_list.to_csv(f"shopping/shopping_{time_stamp}.txt", index=False, header=False)
    st.write(time_stamp)
    



# page to add recipe (link from current menu)
def new_recipe():
    pass

def main_page():
    st.write("Welcome to FoodleDo")
    pass

if __name__ == '__main__':
    main_page()




