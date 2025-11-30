
import streamlit as st
import pandas as pd
import os
from time import gmtime, strftime

st.image('./logo.png', width=300)
st.write("Create a menu:")

recipes_dir = './recipes'

recipes = os.listdir(recipes_dir)
recipes = [r for r in recipes if not r.startswith('.')]
recipes.sort()

selected_recipes = st.multiselect(
    "Choose recipes:", list(recipes)
    )


if st.button("Save menu"):
    menu_data = {'recipes': [], 'ingr_unit': {}}
    for i in range(len(selected_recipes)):
        menu_data['recipes'].append(selected_recipes[i])
        ingredients = pd.read_csv(f"{recipes_dir}/{selected_recipes[i]}/ingredients.txt")
        for row in range(ingredients.shape[0]):
            iu_key = f"{ingredients.iloc[row]['ingredient']}_{ingredients.iloc[row,]['unit']}"
            if iu_key in menu_data['ingr_unit']:
                menu_data['ingr_unit'][iu_key] += ingredients.iloc[row]['amount']
            else:
                menu_data['ingr_unit'][iu_key] = ingredients.iloc[row]['amount']
    #with open("menus/menu_latest.txt", "w") as f:
    #    for name in selected_recipes:
    #        f.write(name + "\n")
    time_stamp = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
    menu = pd.DataFrame(menu_data['recipes'])
    menu.to_csv(f"menus/menu_{time_stamp}.txt", index=False, header=False)
    menu.to_csv(f"menus/menu_latest.txt", index=False, header=False)
    shopping_list = pd.Series(menu_data['ingr_unit']).reset_index()
    shopping_list.to_csv(f"shopping/shopping_{time_stamp}.txt", index=False, header=False)
    shopping_list.to_csv(f"shopping/shopping_latest.txt", index=False, header=False)
    st.success("Recipes saved to menu_latest.txt")

    