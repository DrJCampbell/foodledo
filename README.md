# foodledo

FoodleDo - A streamlit app to manage recipe selection and shopping list creation.

- Run this app as a streamlit server on your network.
- Create new menus for the week
- Get a shopping list customised to your family size (portions per meal)

## Installation

### Step 1

Create a conda environment with Python 3.12, Pandas and Streamlit. If you first need to install conda, we recommend using [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions).

```bash
conda create --name foodledo python=3.12 --yes

conda activate foodledo

pip install pandas

pip install streamlit
```

### Step 2

Next, clone the GitHub repository to a sensible folder location on your computer. If you are using the Mac command line, you may need to first install X-code command line tools. If using Windows, either try the GitHub Desktop application or the miniconda prompt.

```
git clone https://github.com/DrJCampbell/foodledo.git

git clone git@github.com:DrJCampbell/foodledo.git # if using ssh
```

### Step 3

Start the development server

```bash
cd foodledo

streamlit run foodledo.py
```

### Step 4

Navigate to the URL on your local computer (eg http://localhost:<port number>)