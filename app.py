import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
csv_file_path = 'vehicles_us.csv'

# Read the dataset
df = pd.read_csv(csv_file_path)

# Empty spaces
df = df.dropna()

# Header
st.header("Vehicles Information")

# Introduction
st.markdown("Many different models of cars are released every year, they are all different to fulfill the accomodations of everyone, from price, space, economic, paint color and 4 wheel drive. Even with so many different types of customization there certain aspects of a car that are common.")

# Delete _ for the column names 
df.columns = df.columns.str.replace('_', ' ')
df.columns = df.columns.str.replace('is4wd', '4 wd')

# At least one Plotly Express histogram
hist_column = st.selectbox("X Section", df.columns, index = 4)

# Find create a groupby
model_year = df.groupby('model year').cylinders.median()

# Finds all the medians per every year and adds the to a list
median_list = model_year.values.tolist()

# Finds the number of unique values
median_count = Counter(median_list)
unique_median = list(median_count.keys())
frequencies = list(median_count.values())
print (unique_median)
print (frequencies)

# Create a histogram
fig_hist = px.bar(df, x= unique_median, y = frequencies, title = 'Histogram of Cylinders') 
fig_hist.update_xaxes(title_text='Common # of cylinders for all years')
# fig_hist.update_xaxes(title_text='Sum of Common Cylinders per Year')
fig_hist.update_yaxes(title_text='Number of years')
st.plotly_chart(fig_hist)
fig_hist.show()

# Description of histogram
st.markdown("Depending on the reasons to purchase a new car, from economic cars to family size or working trucks, it seems like people prefer the 6 cylinders and 8 more than anything else released throughout the year.")

# Default values for x and y axes in scatter plot
default_x = 'X Section'
default_y = 'Y Section'

# At least one Plotly Express scatter plot
scatter_x = st.selectbox("X Section", df.columns, index = 6)
scatter_y = st.selectbox("Y Section", df.columns, index = 0)
fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, title='Odometer and Price correlation')
# At least one checkbox to change the behavior
show_details = st.checkbox("Press to view details")
if show_details:
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df['odometer'] < 300000) & (df['price'] < 60000)]

    # Create the scatterplot with the filtered data
    fig_scatter_filtered = px.scatter(filtered_df, x=scatter_x, y=scatter_y, title='Filtered Odometer and Price correlation')
    st.plotly_chart(fig_scatter_filtered)
    st.write("After removing the classic cars and hidden gems, we can see more clearly what the average price and number of miles on each car")
else:
    fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, title='Odometer and Price correlation')
    st.plotly_chart(fig_scatter)
    
# Description of scatterplot
st.markdown("The expected trend of odometer and price seems to be accurate, the price of the vehicle declines as the odometer level increases, for exception of some cars which could be classic cars or electric cars that often aren't affect by the amount of miles.")

# Conclusion
st.markdown("Some cars are expensive due to time, others due to miles but the average car seems to be at a fair price. After looking at the detail table, we were able to see how their price slowly declines at a decent rate.")