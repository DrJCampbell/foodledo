import streamlit as st
import pandas as pd

pages = {
    "Options": [
        st.Page("show_menu.py", title="View menu", default=True),
        st.Page("pick_menu.py", title="Pick_menu"),
        #st.Page("random_menu.py", title="Random menu"),
        st.Page("show_shopping.py", title="Show shopping"),
        st.Page("new_recipe.py", title="New recipe"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()


