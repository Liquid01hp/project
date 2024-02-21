import streamlit as st
import pandas as pd
import plotly.express as px

csv_file_path = 'vehicles_us.csv'

# Read the dataset
df = pd.read_csv(csv_file_path)

#Prints out the number of duplicates
(df.duplicated().sum())
df = df.drop_duplicates()

# At least one st.header with text
st.header("Vehicles Information")
st.subheader("The following information will give you a better understanding about the cars,"
"from Gas to Electric, how the lower the odometer often means cheapers price and how some cars"
"will still be high price due to them being classes or hidden gems.")

# At least one Plotly Express histogram
hist_column = st.selectbox("fuel", df.columns)
fig_hist = px.histogram(df, x=hist_column, title=f'Histogram of {hist_column}')
st.plotly_chart(fig_hist)

#Default values for x and y axes in scatter plot
default_x = 'odometer'
default_y = 'price'

# At least one Plotly Express scatter plot
scatter_x = st.selectbox("odometer", df.columns)
scatter_y = st.selectbox("price", df.columns)
fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, title='Odometer and Price correlation')
st.plotly_chart(fig_scatter)

# At least one checkbox to change the behavior
show_details = st.checkbox("Show details")
if show_details:
    st.write("Not all expensive cars have to be new")
