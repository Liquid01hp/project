import streamlit as st
import pandas as pd
import plotly.express as px

csv_file_path = 'vehicles_us.csv'

# Read the dataset
df = pd.read_csv(csv_file_path)

# Header
st.header("Vehicles Information")

# Introduction
st.markdown("A lot is needed to be learn when it comes to cars, from model, model year, number of cylinders and so on. The following will showcase the average number of cylinders in our collection and how often the price of a car is affect by the odometer. ")

# Delete _ for the column names 
df.columns = df.columns.str.replace('_', ' ')
df.columns = df.columns.str.replace('is4wd', '4 wd')

# At least one Plotly Express histogram
hist_column = st.selectbox("X Section", df.columns, index = 4)

#Find the mediam for model_year
model_year = df.groupby('model year').cylinders.median()
model = df.groupby('model').cylinders.median()

# Create a histogram
fig_hist = px.histogram(df, y= model_year, )
fig_hist = px.histogram(df, x= model,)
fig_hist.update_xaxes(title_text='Average # of Cylinders Per Model Year')
fig_hist.update_yaxes(title_text='test_title')
#print (fig_hist)
#fig_hist.show()
fig_hist = px.histogram(df, x=hist_column, title=f'Histogram of {hist_column}')
st.plotly_chart(fig_hist)

# Description of histogram
st.markdown("Throughout the years, cars have update in many ways, one of them is the amount of cylinders a car has. They started with 3 and the highest until now its 12, althought majority of cars now a days have either 4, 6 or 8 making that the most common ones.")

# Default values for x and y axes in scatter plot
default_x = 'X Section'
default_y = 'Y Section'

# At least one Plotly Express scatter plot
scatter_x = st.selectbox("X Section", df.columns, index = 6)
scatter_y = st.selectbox("Y Section", df.columns, index = 0)
fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, title='Odometer and Price correlation')
# At least one checkbox to change the behavior
show_details = st.checkbox("Show details")
if show_details:
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df['odometer'] < 300000) & (df['price'] < 60000)]

    # Create the scatterplot with the filtered data
    fig_scatter_filtered = px.scatter(filtered_df, x=scatter_x, y=scatter_y, title='Filtered Odometer and Price correlation')
    st.plotly_chart(fig_scatter_filtered)
else:
    fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, title='Odometer and Price correlation')
    st.plotly_chart(fig_scatter)

#Description of scatterplot
st.markdown("The expected trend of odometer and price seems to be accurate, the price of the vehicle declines as the odometer level increases, for exception of some cars which could be classic cars or electric cars that often aren't affect by the amount of miles.")

# Conclusion
st.markdown("Some cars are expensive due to time, others due to miles but the average car seems to be at a fair price.")