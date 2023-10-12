import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_industry

"""
# Bonus Fun Page: Exploring New Frontiers 🚀📊

Welcome to the Bonus Fun Page, where we take our data exploration to the next level! 🎉🌐

## Unveiling Additional Insights 🕵️‍♂️📈

This is where things get exciting! We're diving deeper into the realm of data by introducing a new dataset, thanks to our friends at [inforse.fr](https://www.inforse.fr/accueil). 📂🔍

### Gearing Up for GCO2 Analysis 🌿🏢

Our main mission here is to analyze and visualize the greenhouse gas emissions (gCO2) of sectors and companies. We'll create insightful plots that showcase the relationships and dynamics between these two crucial factors. 🌍📉

"""
industry = load_industry()
fig = px.histogram(industry, x='NAF_SECTION',
                   title='Number of companies by industry in this new dataset')
st.plotly_chart(fig)
fig = px.histogram(industry, x='NAF_SECTION', title='Tonnes of CO2 produced by industry in the dataset',
                   y='tonnes CO2 scopes 1 & 2', histfunc='sum')
fig.update_layout(yaxis_type="log")
st.plotly_chart(fig)


# Create your scatter plot with the trendline
fig = px.scatter(industry, x='g CO2 / € du secteur', y="g CO2 /  € de l'entreprise", color='Entité',
                 title='Tonnes of CO2 produced by industry in the dataset')
diagonal = go.Scatter(x=list(range(len(industry))), y=list(
    range(len(industry))), mode='lines', name='x = y')
fig.add_trace(diagonal)
# Update the y-axis to use a logarithmic scale
fig.update_traces(showlegend=False)
fig.update_layout(yaxis_type="log")
st.plotly_chart(fig)
"""
### The results are in! 📊📈
This plot is so interesting because it shows the relationship between the CO2 emissions of a company and the CO2 emissions of its industry. 🤯
Thus, by tracing the line x = y, we can see that a company's CO2 emissions are proportional to the CO2 emissions of its industry. 📈

In other words, is the company's CO2 emissions normal compared to the CO2 emissions of its industry? 🤔 
Is it a good or a bad company? 🤔

"""
