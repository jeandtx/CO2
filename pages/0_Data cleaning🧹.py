import streamlit as st
from utils import load_dataset

"""
# Data Cleaning: Preparing for Clarity 🧹📊

## Welcome to the Data Cleaning Phase! 🚿🧽

In the realm of data analysis, the road to meaningful insights begins with clean and well-structured data. 📈🔍

### 🧼 What is Data Cleaning?

Data cleaning is the essential first step in our journey to unveil the truth about CO2 emissions. It's the process of:

- **Identifying Imperfections**: Locating inconsistencies, inaccuracies, and anomalies within our data. 🕵️‍♂️🔎
- **Correcting Errors**: Taking necessary measures to rectify these inconsistencies and inaccuracies. 🛠️📏
- **Enhancing Quality**: Improving data quality for accurate analysis and visualization. 🌟📊

### 🔑 Why is Data Cleaning Crucial?

Clean data is the foundation upon which we'll build our understanding of carbon emissions. Without this crucial step, our analysis could be clouded by inaccuracies and misinformation. Through data cleaning, we ensure:

- **Reliability**: We can trust our data to provide accurate insights. 📈✅
- **Consistency**: Our datasets are uniform and consistent, making comparisons and analysis more straightforward. 📉📊
- **Reproducibility**: Others can replicate our analysis with confidence. 🔄📈

### 🛠️ The Data Cleaning Toolkit:

Our data cleaning toolkit is equipped with various techniques, tools, and best practices to ensure our data is pristine and ready for exploration. We'll address issues such as missing values, duplicates, outliers, and more.
The tools are mainly from the Pandas library, a powerful Python package for data analysis. 🐼🐍

"""
with st.echo(code_location='below'):
    import numpy as np
    import pandas as pd
    import plotly.express as px

"""
Then, we need to load our datasets. We'll be using the following datasets for our analysis:
The [La Base Carbone](https://www.data.gouv.fr/fr/datasets/base-carbone-complete-de-lademe-en-francais-v17-0/) is a public database managed by ADEME (French Agency for Ecological Transition) containing emission factors essential for conducting carbon accounting exercises. (An emission factor is a ratio used to determine greenhouse gas emissions associated with an object, material, or service.)
"""
with st.echo(code_location='below'):
    carbone = load_dataset()
"""
```
Index(['Type Ligne', 'Identifiant de l'élément', 'Structure',
       'Statut de l'élément', 'Nom base français', 'Nom attribut français',
       'Nom frontière français', 'Code de la catégorie', 'Tags français',
       'Unité français', 'Contributeur', 'Programme', 'Url du programme',
       'Source', 'Localisation géographique',
       'Sous-localisation géographique français', 'Date de création',
       'Date de modification', 'Période de validité', 'Incertitude',
       'Réglementations', 'Transparence', 'Qualité', 'Qualité TeR',
       'Qualité GR', 'Qualité TiR', 'Qualité C', 'Qualité P', 'Qualité M',
       'Commentaire français', 'Type poste', 'Nom poste français',
       'Total poste non décomposé', 'CO2f', 'CH4f', 'CH4b', 'N2O',
       'Code gaz supplémentaire 1', 'Valeur gaz supplémentaire 1',
       'Code gaz supplémentaire 2', 'Valeur gaz supplémentaire 2',
       'Code gaz supplémentaire 3', 'Valeur gaz supplémentaire 3',
       'Code gaz supplémentaire 4', 'Valeur gaz supplémentaire 4',
       'Code gaz supplémentaire 5', 'Valeur gaz supplémentaire 5',
       'Autres GES', 'CO2b'],
      dtype='object')```
"""
"""
We can see that we have MANY columns and we don't need all of them. Especially, we don't need empty colmuns 
After this, a simple scatter plot help us to visualize all the numeric features and how they are distributed around the dataset.
"""
with st.echo(code_location='top'):
    carbone.drop([
        "Statut de l'élément", 'Code gaz supplémentaire 2', 'Valeur gaz supplémentaire 2',
        'Code gaz supplémentaire 3', 'Valeur gaz supplémentaire 3',
        'Code gaz supplémentaire 4', 'Valeur gaz supplémentaire 4',
        'Code gaz supplémentaire 5', 'Valeur gaz supplémentaire 5'], axis=1, inplace=True)
    fig = px.scatter(carbone.select_dtypes([np.number]))
    st.plotly_chart(fig)

"""
Now that the data cleaning is complete and we've gained insights into how our features are distributed, it's time to dive into analysis and visualization. 📊🔍
"""
