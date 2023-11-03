import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Dataset
df = pd.read_csv('ecom-data.csv')

# Function to create a bar chart with numbers on top
def create_bar_chart_with_numbers(data, x, y, title):
    fig = px.bar(data, x=x, y=y, title=title)

    # Add text labels for each bar
    for i in range(len(data)):
        fig.add_trace(go.Scatter(x=[data[x][i]], y=[data[y][i]],
                                text=[data[y][i]], mode='text', textposition='top center'))

    return fig

# Gender Dynamics - Pie Chart
def gender_dynamics():
    st.markdown("### Gender Dynamics ")
    st.write("Customer shown by their Gender.")    
    
    gender_counts = df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig_gender = create_bar_chart_with_numbers(gender_counts, 'Gender', 'Count','')
    st.plotly_chart(fig_gender)

    st.markdown("#### Business Insight :")
    st.write("Male Customers are more than Female Customers whereas the difference is not much. 5k more male users. Thus every product and advertisement should cater to both genders.")

# Device Preferences - Bar Chart
def device_preferences():
    st.markdown("### Preference of Medium to buy product ")
    st.write("Sales is driven through which mode: Company app or Website.") 

    device_counts = df['Device_Type'].value_counts().reset_index()
    device_counts.columns = ['Device_Type', 'Count']
    fig_device = create_bar_chart_with_numbers(device_counts, 'Device_Type', 'Count', '')
    st.plotly_chart(fig_device)

    st.markdown("#### Business Insight :")
    st.write("Customers use web much more than the Mobile App to buy products. Maybe there is some problem with the app. To drive more customers to app certain steps are to be taken.")

# Loyalty Insights - Bar Chart
def loyalty_insights():
    st.markdown("### Loyalty Insight ")
    st.write("Customer segmentation based on Login type : new customer, old customer, other.") 

    login_counts = df['Customer_Login_type'].value_counts().reset_index()
    login_counts.columns = ['Customer_Login_type', 'Count']
    fig_login = create_bar_chart_with_numbers(login_counts, 'Customer_Login_type', 'Count', '')
    st.plotly_chart(fig_login)

    st.markdown("#### Business Insight :")
    st.write("Most of the Sales is through members which shows good retention. Very few buy products as guest or are new buyers. Company shows very good retention of member. There are almost 50k registered members.")

# Sidebar
st.sidebar.header("Customer Information Dashboard")

# Option to select and display plots
selected_plot = st.sidebar.selectbox("Select a Plot", ["Gender Dynamics", "Preference of Customers", "Loyalty Insights"])

# Display the selected plot
if selected_plot == "Gender Dynamics":
    gender_dynamics()
elif selected_plot == "Preference of Customers":
    device_preferences()
elif selected_plot == "Loyalty Insights":
    loyalty_insights()
