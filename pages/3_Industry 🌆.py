import streamlit as st
import plotly.express as px
from utils import load_clean_data

carbone = load_clean_data()

"""
# Industry Analysis: Decoding CO2 Emissions 🏭🌎

Welcome to the Industry Analysis section, where we shine a spotlight on the critical role industries play in carbon emissions. 📊🔍

## Unmasking High Emission Sectors 🕵️‍♂️

In this segment of our journey, we'll unravel the complex web of industries and their contributions to carbon dioxide (CO2) emissions. 🏭🌫️

### Revealing the Heavy Hitters:

Our primary objective is to:

- **Identify Key Contributors**: Explore which industries are the leading producers of CO2 emissions. 📈🏢
- **Quantify Impact**: Analyze the extent of their influence on the environment and global emissions. 🌍📉

### Corporate Social Responsibility (CSR) in the Spotlight:

As we navigate through the industrial landscape, it's vital to emphasize the importance of Corporate Social Responsibility (CSR). Companies play a crucial role in minimizing their environmental footprint, and CSR is a powerful instrument for achieving that.

**CSR Matters** 🌱🏢:

Corporate Social Responsibility is the ethical compass that guides companies towards:

- **Sustainability**: Adopting eco-friendly practices that reduce their environmental impact. 🌿🌏
- **Transparency**: Communicating openly about their environmental efforts and impact. 🗣️📈
- **Global Stewardship**: Taking responsibility for the planet's well-being, and contributing to a sustainable future. 🌎✨

As we explore the industries contributing to CO2 emissions, we'll also highlight examples of CSR initiatives that are making a positive difference in the world.

Let's dive into the data, dissect industrial emissions, and discover how CSR can be a force for positive change. 🌟🏭🔗

### Biggest polluters in the industry:

"""
histfunc = st.radio("Select a histogram function", ('count', 'sum', 'avg', 'min', 'max'))
log = st.checkbox("Logarithmic scale")

with st.echo(code_location='top'):
    fig = px.histogram(carbone, x='Code de la catégorie', y='Total poste non décomposé', title='Biggest polluters in the industry', histfunc=histfunc)
    fig.update_layout(showlegend=False)
    fig.update_xaxes(categoryorder='total descending')
    if log:
        fig.update_layout(yaxis_type="log")
    st.plotly_chart(fig)

"""
Here we can see Deforastation is a major polluter, followed closely by the maritime transportation. 🚢

Another interesting point is on the right of this histogram where reforesation has a negative impact on the CO2 emissions. 🌳
### 
"""

fig = px.histogram(carbone[carbone['Total poste non décomposé'] > 100], x='Nom attribut français', y='Total poste non décomposé', title='Biggest polluters (Company name) in the industry', histfunc=histfunc)
fig.update_layout(showlegend=False)
fig.update_xaxes(categoryorder='total descending')
if log:
    fig.update_layout(yaxis_type="log")
st.plotly_chart(fig)

fig = px.histogram(carbone[carbone['Total poste non décomposé'] > 100], x='Nom base français', y='Total poste non décomposé', title='Biggest polluters (Object name) in the industry', histfunc=histfunc)
fig.update_layout(showlegend=False)
fig.update_xaxes(categoryorder='total descending')
if log:
    fig.update_layout(yaxis_type="log")
st.plotly_chart(fig)

"""
In those plots we remark a really interesing term appearing many times in the high polluters: **"Changement d'affectation des sols"**. ⛱︎

What is it? 🤔
# Land Transformation to Impermeability and its CO2 Emissions 🏞️➡️🏙️

Welcome to the realm where land undergoes a transformative journey, changing from its natural state to impermeable urban landscapes. 🚧🌱

## Unveiling the Impact on CO2 Emissions 🌍📉

The process of transitioning land to impermeability involves the construction of cities, roads, and structures that hinder natural soil permeability. But what's its connection to carbon dioxide (CO2) emissions? Let's dive in! 🚀🔍

### 1. Direct CO2 Emissions 🏗️🏢

The construction of infrastructure, material extraction, transportation, and energy demands during construction can lead to direct CO2 emissions. 🏭🔥

### 2. Altering the Water Cycle 🌧️💧

Impermeable surfaces disrupt the natural water cycle, reducing water infiltration into the soil. This can result in increased flooding, reduced groundwater recharge, and a shortage of freshwater resources. 💦🌊

### 3. Impact on Vegetation 🌿🌳

The transformation process often involves the removal of existing vegetation, reducing the Earth's ability to absorb CO2 through photosynthesis. 🍃🌎

### 4. Urban Heat Island Effect 🏙️🌡️

Impermeable surfaces, like concrete and asphalt, absorb and radiate heat, contributing to the urban heat island effect. This can lead to greater energy consumption for cooling, resulting in additional CO2 emissions. 🔥🏘️❄️

In summary, the transition of land to impermeability is a multifaceted challenge, impacting the environment and climate. Sustainable urban planning and development are crucial to mitigating these effects and reducing associated CO2 emissions. 🌿🏙️🌍

Stay tuned for more insights on the dynamic relationship between human activities and our planet's changing landscape. 📊🔍

![](https://www.millenaire3.com/var/m3/storage/images/8/5/8/1/491858-1-fre-FR/Limites%20planétaires%20Infographie%208.PNG)
"""