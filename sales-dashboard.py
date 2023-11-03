import streamlit as st
import pandas as pd
import plotly.express as px

# Dataset
df = pd.read_csv('ecom-data.csv')

# Add a heading to the sidebar
st.sidebar.markdown("# Sales Dashboard")
st.sidebar.markdown("\n")

# Create a radio button on the sidebar to select the chart
selected_chart = st.sidebar.selectbox("Select Chart", ["Monthly Sales Trends", "Sales Leaders", "Product Category Sales by Gender"])

# Define functions to create individual charts

# Monthly Sales Trends
def create_monthly_sales_trends_chart():
    st.markdown("### Sales Trend over the year using a Histogram")
    st.write("Companies Sales over the year showing variation.")

    monthly_sales_fig = px.bar(df, x='Order_Date', y='Sales', title='Monthly Sales Trends', labels={'Order_Date': 'Month', 'Sales': 'Total Sales'})
    st.plotly_chart(monthly_sales_fig)

    st.markdown("#### Business Insight :")
    st.write("Sales Monthly Trend shows product sold per month of 2018 with Summer Time (May June July) and Winter Time (October November December) showing good sales. The sales over the first quarter are less as compared to any quarter around year.")

def create_sales_leaders_chart():
    best_selling_products = df.groupby(['Product', 'Gender'])['Sales'].sum().nlargest(10).reset_index()
    st.markdown("### Top Selling Products in the Company")
    st.write("Sales Leaders - Best Selling Products in the Company")

    fig = px.bar(
        best_selling_products,
        x='Product',
        y='Sales',
        color='Gender',
        labels={'Product': 'Product', 'Sales': 'Total Sales'},
        barmode='stack',  # Stacked bar chart mode
    )
    st.plotly_chart(fig)
    st.markdown("#### Business Insight :")
    st.write("The 'Top Selling Products by Gender' chart displays the top 10 selling products with a breakdown by gender. It helps identify the most popular products in terms of sales, segmented by gender, which is valuable for understanding sales patterns across different genders.")

# Function to create a stacked bar chart for product category sales by gender
def plot_stacked_bar_product_category_sales():
    category_gender_sales = df.groupby(['Product_Category', 'Gender'])['Sales'].sum().reset_index()
    
    st.markdown("### Total Sales by Category divided by Gender")
    st.write("Sales by Category showing customer's gender")

    stacked_bar_fig = px.bar(
        category_gender_sales,
        x='Product_Category',
        y='Sales',
        color='Gender',
        labels={'Product_Category': 'Product Category', 'Sales': 'Total Sales'},
        barmode='relative',
    )
    st.plotly_chart(stacked_bar_fig)

    st.markdown("#### Business Insight :")
    st.write("Fashion is the most selling product category. Home and Furniture and Electronics have more female buyers whereas Auto and Accessories and Fashion have more male buyers. Followed by Fashion most selling category is ")

# Display the selected chart
if selected_chart == "Monthly Sales Trends":
    create_monthly_sales_trends_chart()
elif selected_chart == "Sales Leaders":
    create_sales_leaders_chart()
elif selected_chart == "Product Category Sales by Gender":
    plot_stacked_bar_product_category_sales()
