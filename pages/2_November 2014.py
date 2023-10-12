import streamlit as st
import plotly.express as px
from utils import load_clean_data

carbone = load_clean_data()

"""
### What happened in in November 2014 !? 🤔
"""

# drop_x = st.selectbox("X-axis", ['Code de la catégorie', 'Nom attribut français', 'Nom base français', 'Sous-localisation géographique français'], key=3)

# # Generate the histogram plot
# with st.echo(code_location='top'):
#     nov2014 = carbone[carbone['Date de modification'] == 'Novembre 2014']

#     fig = px.pie(nov2014, values='Total poste non décomposé', names=drop_x, title='Focus on November 2014')
#     fig.update_traces(textposition='inside', textinfo='none')
#     fig.update_layout(showlegend=False) 

#     st.plotly_chart(fig)
