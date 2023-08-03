import streamlit as st
import pandas as pd
from bokeh.plotting import figure
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write ('Hello Word')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
y_axis = st.selectbox('select element 2', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])

x = df['Mg']
y = df['Si']

p = figure(
    title='simple line example',
    x_axis_label= 'x',
    y_axis_label= 'y')

p.plot(x, y)

st.bokeh_chart(p, use_container_width=True)

