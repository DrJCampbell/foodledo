import streamlit as st
import pandas as pd

st.image('./logo.png', width=300)
st.write("Shopping list:")

diners = st.slider(
    "Number of diners",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
    label_visibility="visible",
    width="stretch"
    )

shopping_list = pd.read_csv('shopping/shopping_latest.txt', header=None)
shopping_list.sort_values(by=0, inplace=True)
for i in range(shopping_list.shape[0]):
    quantity = shopping_list[1].iloc[i] * diners
    ingredient_unit = str(shopping_list[0].iloc[i])
    ingredient_unit = ingredient_unit.split("_")
    st.write(f"{ingredient_unit[0]} :::    {str(round(quantity, 2))} {ingredient_unit[1]}")
#shopping_list = list(shopping_list)
#edited_shopping_list = st.data_editor(shopping_list)
#st.write(shopping_list)