import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Dataset
df = pd.read_csv('ecom-data.csv')

# Add a heading to the sidebar
st.sidebar.markdown("# Operational Dashboard")
st.sidebar.markdown("\n")

# Create a radio button on the sidebar to select the chart
selected_plot = st.sidebar.selectbox("Select Chart", ["Order Priority Analysis", "Shipping Costs Analysis", "Payment Preference"])

# Insights

# Order Priority Analysis - Bar Chart with Numbers on Top
def order_priority():
    st.markdown("### Order Priority Analysis")
    st.write("Value Count of Order Priority of all product buys. ") 

    order_priority_counts = df['Order_Priority'].value_counts().reset_index()
    order_priority_counts.columns = ['Order_Priority', 'Count']

    fig_order_priority = go.Figure(data=[go.Bar(
        x=order_priority_counts['Order_Priority'],
        y=order_priority_counts['Count'],
        text=order_priority_counts['Count'],
        textposition='auto',
    )])

    fig_order_priority.update_layout(
        title='Order Priority Analysis',
        xaxis_title='Order Priority',
        yaxis_title='Count'
    )

    st.plotly_chart(fig_order_priority)

    st.markdown("#### Business Insight :")
    st.write("Medium Priority is the most common when customers are buying products. Followed by high and critical and low priority have fewer orders. Company services should focus more on Medium priority and High Priority order delivery.")

# Shipping Costs Breakdown - Box Plot
def shipping_cost():
    st.markdown("### Shipping Cost Analysis ")
    st.write("Shipping Cost shown by Order Priority.")

    fig_shipping_costs = px.box(df, x='Order_Priority', y='Shipping_Cost', title='')
    st.plotly_chart(fig_shipping_costs)

    st.markdown("#### Business Insight :")
    st.write("Shipping Cost remains uniform over different Order Priority.")

# Payment Method Preferences - Pie Chart
def payment_prefer():
    st.markdown("### Payment Method Preference ")
    st.write("Which mode of payment is most used, which is used less.") 
    
    payment_method_counts = df['Payment_method'].value_counts().reset_index()
    payment_method_counts.columns = ['Payment_method', 'Count']

    fig_payment_method = go.Figure(data=[go.Pie(
        labels=payment_method_counts['Payment_method'],
        values=payment_method_counts['Count'],
    )])

    fig_payment_method.update_layout(
        title='Payment Method Preferences',
    )

    st.plotly_chart(fig_payment_method)
    
    st.markdown("#### Business Insight :")
    st.write("Customers prefer Credit card payment majorly. Other methods account for much less of the payments. Company should focus on driving customers through credit card payments by offering incentives discounts etc.")


# Display the selected plot
if selected_plot == "Order Priority Analysis":
    order_priority()
elif selected_plot == "Shipping Costs Analysis":
    shipping_cost()
elif selected_plot == "Payment Preference":
    payment_prefer()