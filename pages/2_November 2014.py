import streamlit as st
import plotly.express as px
from utils import load_clean_data

carbone = load_clean_data()

"""
### What happened in in November 2014 !? 🤔
"""
with st.echo(code_location='top'):
    nov2014 = carbone[carbone['Date de modification'] == 'Novembre 2014']
histfunc = st.radio("Select a histogram function",
                    ('count', 'sum', 'avg', 'min', 'max'))
log = st.checkbox("Logarithmic scale")

with st.echo(code_location='top'):
    fig = px.histogram(nov2014, x='Code de la catégorie', y='Total poste non décomposé',
                       title='Biggest polluters in the industry', histfunc=histfunc)
    fig.update_layout(showlegend=False)
    fig.update_xaxes(categoryorder='total descending')
    if log:
        fig.update_layout(yaxis_type="log")
    st.plotly_chart(fig)


fig = px.histogram(nov2014[nov2014['Total poste non décomposé'] > 100], x='Nom attribut français',
                   y='Total poste non décomposé', title='Biggest polluters (Company name) in the industry', histfunc=histfunc)
fig.update_layout(showlegend=False)
fig.update_xaxes(categoryorder='total descending')
if log:
    fig.update_layout(yaxis_type="log")
st.plotly_chart(fig)

fig = px.histogram(nov2014[nov2014['Total poste non décomposé'] > 100], x='Nom base français',
                   y='Total poste non décomposé', title='Biggest polluters (Object name) in the industry', histfunc=histfunc)
fig.update_layout(showlegend=False)
fig.update_xaxes(categoryorder='total descending')
if log:
    fig.update_layout(yaxis_type="log")
st.plotly_chart(fig)
