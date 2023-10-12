from utils import load_clean_data
import streamlit as st
import plotly.express as px

carbone = load_clean_data()
"""
# Exploring CO2 Emissions 🌍📈

Welcome to the heart of our data analysis journey, where we delve into the world of CO2 emissions. 🌫️📊

## Unveiling the Carbon Footprint 🕵️‍♂️

In this section, we'll embark on a comprehensive exploration of carbon dioxide (CO2) emissions, dissecting the data to gain profound insights. 📉🔍

### Comparing Multiple Dimensions:

Our analysis is multidimensional, comparing CO2 emissions across various key factors:

- **Industry Categories**: We'll examine how different industries contribute to carbon emissions. 🏭🏢
- **Geographical Locations**: Mapping out emissions geographically to understand regional disparities. 🗺️🌎
- **Time Trends**: Exploring how emissions have evolved over time, uncovering historical patterns. 📆⌛
- And More: We'll leave no stone unturned as we explore additional factors that influence emissions.

Our aim is to paint a comprehensive picture of carbon emissions and their implications, enabling us to make informed decisions and take meaningful actions. 🌱🌏

Let's start this enlightening journey into the realm of CO2 emissions, where data transforms into actionable insights. 🚀📈

### C02 Emissions by Country:
"""

aggregate_type = st.selectbox("Aggregate Type", ["Sum", "Average"], key=1)

# Calculate the aggregation based on the user's selection
if aggregate_type == "Sum":
    histfunc = 'sum'
    title = 'Sum CO2 emitting by country'
else:
    histfunc = 'avg'
    title = 'Average CO2 emitting by country'

# Generate the histogram plot
with st.echo(code_location='top'):
    fig = px.histogram(carbone, x='Localisation géographique', y='Total poste non décomposé', histfunc=histfunc, title=title)
    st.plotly_chart(fig)

"""
What do you notice? 🤔

We can see something really disappointing, the data is not consistent. Obviously rest of the 
world produce way more C02 in therm of average. But if we take the sum France is way much higher !
This is dur to the fact that the dataset is mainly composed of French companies. And in addition, other countries are only called other cournties.

So we can't really compare the data.
What we can do tho, is make a preformant analysis on France only, for this we just need to keep only France's data
"""
log_scale = st.checkbox("Log Scale")

# Generate the histogram plot
with st.echo(code_location='top'):
    fig = px.histogram(carbone, x='Sous-localisation géographique français', y='Total poste non décomposé', histfunc='avg', title='Sum CO2 emitting by country')
    
    # Set the y-axis scale based on the user's selection
    if log_scale:
        fig.update_layout(yaxis_type="log")
    
    st.plotly_chart(fig)

"""
A problem here is that the data is consistent again, many departments didn't provide enough data.
The aftermath is this plot with a lot of blanks. We can't really do anything about it, so we'll just keep de departments providing data.
"""

with st.echo(code_location='bottom'):
    carbone.drop(carbone[carbone['Total poste non décomposé'] < 10].index, inplace=True)
    fig = px.histogram(carbone, x='Sous-localisation géographique français', y='Total poste non décomposé', histfunc='avg', title='Avg CO2 emitting by departement')
    if log_scale:
        fig.update_layout(yaxis_type="log")
    st.plotly_chart(fig)

"""
Madagascar is a high outlier.

Problem, we now have only 1500 rows our dataset is now significantly smaller. But the data is consistent and usable.

We can actually say that this is the data we had at the start. All the rows and columns deleted were just noise.
### CO2 Emissions by Time:

"""

aggregate_type2 = st.selectbox("Aggregate Type", ["Sum", "Average"], key=2)
color = st.checkbox("Color")
log_scale2 = st.checkbox("Log")

# Calculate the aggregation based on the user's selection
if aggregate_type2 == "Sum":
    histfunc2 = 'sum'
    title = 'Sum CO2 emitting by time'
else:
    histfunc2 = 'avg'
    title = 'Average CO2 emitting by time'

# Generate the histogram plot
with st.echo(code_location='top'):
    if color:
        fig = px.histogram(carbone, x='Date de modification', y='Total poste non décomposé', histfunc=histfunc2, title=title, color='Incertitude')
    else:
        fig = px.histogram(carbone, x='Date de modification', y='Total poste non décomposé', histfunc=histfunc2, title=title)
    if log_scale2:
        fig.update_layout(yaxis_type="log")

    st.plotly_chart(fig)

"""
We can see a huge spike in November 2014. We'll see what happened in this period more strictly later. 🤔
### CO2 Emissions by Sources:
"""
with st.echo(code_location='top'):
    fig = px.histogram(carbone, x='Contributeur', y='Total poste non décomposé', histfunc='sum', title='`Sum CO2 emitted by sources', color='Incertitude')
    st.plotly_chart(fig)

"""
What we can see here is that there is one main source of data. 
This shows once again the bad quality of the data. 

We can really observe that the data about C02 emissions is not that accurate. 
Which is quite comprehensible, it's not easy to measure the C02 emissions of a company.
Moreover, the need of this data is quite recent, so it's normal that the data is not that accurate.

The data from the weather has been existing since a while so we can really analyse how C02 emissions impacted our planet.
But data from companies is quite new, this is a new way to visualize the movement of C02 emissions.

And this new way of visualizing needs new datasets that are build today for tomorrow.

This is the responsability of us, future engineers or entrepreneurs to build the datasets of tomorrow.


![photo](/Users/jeandtx/Documents/CODE/M1/DATA VIZ/project 2/pages/asset.png)
"""