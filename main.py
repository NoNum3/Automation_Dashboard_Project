import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import os
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Superstore Dashboard", page_icon=":bar_chart:", layout="wide"
)

st.title(":bar_chart: Superstore Dashboard")
st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

