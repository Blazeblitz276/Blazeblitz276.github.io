import streamlit as st
import streamlit.components.v1 as components
from constant import *

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Portofolio", page_icon="🎨", layout="wide")
st.header("🎨 Portfolio", divider='rainbow')

# page functions ----------------------------------------------------------------
def Portfolio_component(header, content):
   st.subheader(header, divider='grey')
   st.write(content)

# Hurricane Intensity Prediction ----------------------------------------------------------------
Portfolio_component(Portfolio[1][0], Portfolio[1][1])

tab1, tab2 = st.tabs(["Details", "View Project"])
with tab1:
   st.write(Portfolio[1][1])
with tab2:
   st.link_button("Go to Project", "https://github.com/Blazeblitz276/Hurricane-Intensity-Estimation-using-Radiant-ML-Hub-Hurricane-Dataset")

# Stellar Data Classification in PySpark --------------------------------------------------------------
Portfolio_component(Portfolio[2][0], Portfolio[2][1])

st.link_button("Go to Github", "https://github.com/Blazeblitz276/Stellar_Data_EDA_and_classification")

# LLM Desktop ChatApp -------------------------------------------------------------- 
Portfolio_component(Portfolio[3][0], Portfolio[3][1])

st.link_button("Go to :blue[Source Code]", "https://github.com/Blazeblitz276/RAG-With-AWS")

# Japanese Restaurant Visitor Forecasting -----------------------------------------------------------
Portfolio_component(Portfolio[4][0], Portfolio[4][1])

components.iframe(StoryMap_iframe, width=1000, height=700, scrolling=True)
