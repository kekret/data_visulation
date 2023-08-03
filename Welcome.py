import streamlit as st
import pandas as pd

st.write ('Hello Word')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
