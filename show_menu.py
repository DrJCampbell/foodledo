import streamlit as st
import pandas as pd

st.image('./logo.png', width=300)
st.write("Current menu:")

menu = pd.read_csv('menus/menu_latest.txt', header=None)
# parse menu row by row.
# show one recipe at a time with a button to view method

for i in menu.index:
    this_recipe = ''
    with open(f"./recipes/{menu.iloc[i][0]}/method.txt") as f:
        for l in f:
            this_recipe = this_recipe + l
    recipe_expand = st.expander(menu.iloc[i][0])
    recipe_expand.write(this_recipe)