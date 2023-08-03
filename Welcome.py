import streamlit as st
import pandas as pd
from bokeh.plotting import figure
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write ('Hello Word')

st.multiselect('select location', file_name_list, file_name_list[0])

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
y_axis = st.selectbox('select element 2', el_list)

x = df['Mg']/10000
y = df['Si']/10000

p = figure(
    title='Element Plot',
    x_axis_label= 'Mg' + ' wt%',
    y_axis_label= 'Si' + ' wt%')

p.circle(x, y, size =10)

st.bokeh_chart(p, use_container_width=True)

