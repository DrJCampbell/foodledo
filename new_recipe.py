import streamlit as st
import os

st.image('./logo.png', width=300)
st.write("Add a new recipe:")

recipe = st.text_input(
    "Enter a title",
    value="",
    max_chars=100,
    label_visibility="visible",
    width="stretch"
    )

ingredients = st.text_area(
    "Enter a comma-separated list of ingredients (ingredient,amount,unit)",
    value="ingredient,amount,unit",
    height=None,
    label_visibility="visible",
    width="stretch"
    )

method = st.text_area(
    "How do you make this?",
    value="",
    height=None,
    label_visibility="visible",
    width="stretch"
    )

if st.button("Save recipe"):
    # Check if directory exists
    if not os.path.exists(f"./recipes/{recipe}"):
        # Create the directory
        os.makedirs(f"./recipes/{recipe}")
        st.write(f"Directory '{recipe}' created.")
        with open(f"./recipes/{recipe}/ingredients.txt", "w") as f:
            f.write(ingredients)
        with open(f"./recipes/{recipe}/method.txt", "w") as f:
            f.write(method)
    else:
        st.write(f"Directory '{recipe}' already exists. Please choose another name")