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
    shopping_list = pd.read_csv('shopping/shopping_latest.txt', header=None)
    shopping_list = list(shopping_list)
    edited_shopping_list = st.data_editor(shopping_list)
    st.write(shopping_list)


# page to create new menu (link from current menu)
def random_menu(recipes_dir = './recipes', n_recipes = 3):
    # list directories in the recipes directory
    # allow to select a subset of recipes
    # store that selection in a file (somewhere)
    # get the available recipes
    recipes = os.listdir(recipes_dir)
    # remove non-recipe files starting with a dot
    recipes = [r for r in recipes if not r.startswith('.')]
    # random index to sample recipes
    rnd_index = random.sample(range(len(recipes)), k = n_recipes)
    # create a dict to store the recipes and ingredients
    menu_data = {'recipes': [], 'ingr_unit': {}}
    for i in rnd_index:
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
    menu.to_csv(f"menus/menu_latest.txt", index=False, header=False)
    shopping_list = pd.Series(menu_data['ingr_unit']).reset_index()
    shopping_list.to_csv(f"shopping/shopping_{time_stamp}.txt", index=False, header=False)
    shopping_list.to_csv(f"shopping/shopping_latest.txt", index=False, header=False)
    
def pick_menu(recipes_dir = './recipes'):
    # list directories in the recipes directory
    # allow to select a subset of recipes
    recipes = os.listdir(recipes_dir)
    #for recipe in recipes:
    #    st.checkbox(recipe)
    selected_recipes = st.multiselect("Choose recipes:", list(recipes))
    if selected_recipes:
        st.write("### Selected recipes")
        st.write(selected_recipes)
    
    if st.button("Save menu"):
        with open("menus/menu_latest.txt", "w") as f:
            for name in selected_recipes:
                f.write(name + "\n")
        st.success("Recipes saved to menu_latest.txt")



# page to add recipe (link from current menu)
def new_recipe():
    # add a data editor with enough rows for ingredients
    # used a text area for method
    # save to recipes folder
    # create new folder in recipes - check name doesn't already exist
    pass

def main_page():
    st.image('./logo.png', width=300)
    st.write("Welcome to FoodleDo")
    menu = pd.read_csv('menus/menu_latest.txt', header=None)
    # parse menu row by row.
    # show one recipe at a time with a button to view method

    st.session_state.pick_menu = st.button("Select new menu")

    if st.session_state.pick_menu:
        pick_menu()
        #del st.session_state.pick_menu
    else:
        st.session_state.random_menu = st.button("Random menu")
        st.session_state.show_shopping = st.button("View shopping list")
        for i in menu.index:
            this_recipe = ''
            with open(f"./recipes/{menu.iloc[i][0]}/method.txt") as f:
                for l in f:
                    this_recipe = this_recipe + l
            recipe_expand = st.expander(menu.iloc[i][0])
            recipe_expand.write(this_recipe)




    

    if st.session_state.random_menu:
        random_menu()
        del st.session_state.random_menu   
    
    if st.session_state.show_shopping:
        show_shopping()
        del st.session_state.show_shopping

if __name__ == '__main__':
    main_page()




