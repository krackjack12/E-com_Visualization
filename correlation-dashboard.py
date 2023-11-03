import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Dataset
df = pd.read_csv('ecom-data.csv')

# Add a heading to the sidebar
st.sidebar.markdown("# Operational Dashboard")
st.sidebar.markdown("\n")

# Create a radio button on the sidebar to select the chart
selected_plot = st.sidebar.selectbox("Select Chart", ["Order Priority Analysis", "Shipping Costs Analysis", "Payment Preference"])

# Insights

# Dataset
df = pd.read_csv('ecom-data.csv')

# Create the Heatmap of Correlations
st.header("Heatmap of Correlations")
correlation_matrix = df_selected.corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
st.pyplot(fig)

# Create the Scatter Plot of Discounts vs. Sales
st.header("Scatter Plot of Discounts vs. Sales")
st.write("This scatter plot compares discounts to sales to identify any patterns.")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=df, x='Discount', y='Sales', hue='Product_Category')
st.pyplot(fig)


# Find the best-selling product in each category
best_selling_products = df.groupby('Product_Category')['Product'].agg(lambda x: x.mode().iloc[0]).reset_index()

# Create a bar chart using Plotly
fig = px.bar(
    best_selling_products,
    x='Product_Category',
    y='Product',
    text='Product',
    title='Best Selling Product per Category',
)

fig.update_traces(texttemplate='%{text}', textposition='inside')

# Display the Plotly bar chart in Streamlit
st.header("Best Selling Product per Category")
st.plotly_chart(fig)

# Display the selected plot
if selected_plot == "Order Priority Analysis":
    order_priority()
elif selected_plot == "Shipping Costs Analysis":
    shipping_cost()
elif selected_plot == "Payment Preference":
    payment_prefer()