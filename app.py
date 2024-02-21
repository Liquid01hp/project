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

# Description of histogram
st.text = ("Most vehicles are gas with around 47,000 and counting making that 91% of the overal number of vehicles,"
"followed by Diesel with about 3,700 that being 7.1%, leaving electric as the lowest % out of all the cars being 0.01"
"due to electric cars only being 6 of them in total.")

#Default values for x and y axes in scatter plot
default_x = 'odometer'
default_y = 'price'

# At least one Plotly Express scatter plot
scatter_x = st.selectbox("odometer", df.columns)
scatter_y = st.selectbox("price", df.columns)
fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, title='Odometer and Price correlation')
fig_scatter.update_layout(xaxis_title_text='Paint Color')
fig_scatter.update_layout(xaxis_title_text='Model Year')
st.plotly_chart(fig_scatter)

#Description of scatterplot
st.text =("The expected trend of odometer and price seems to be accurate,"
"the price of the vehicle declines as the odometer level increases, for exception of some cars"
"which could be classic cars or electric cars that often aren't affect by the amount of miles.")

# At least one checkbox to change the behavior
show_details = st.checkbox("Show details")
if show_details:
    st.write("Not all expensive cars have to be new")
