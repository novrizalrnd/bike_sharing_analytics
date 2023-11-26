import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# load dataset

df = pd.read_csv('https://raw.githubusercontent.com/novrizalrnd/bike_sharing/main/dataset/hour.csv')
df['dteday'] = pd.to_datetime(df['dteday'])

st.set_page_config(page_title='Capital Bikeshare: Bike-sharing Time Series Dashboard',
                   page_icon='bar_chart:',
                   layout='wide',
                   initial_sidebar_state='expanded')

# create functions

def monthly_trends(df):
    monthly_users = df.resample(rule='M', on='dteday').agg({
        'casual': 'sum',
        'registered': 'sum'
    })
    monthly_users.index = monthly_users.index.strftime('%b-%y')
    monthly_users = monthly_users.reset_index()
    monthly_users.rename(columns={
        'dteday': 'month_year',
        'casual': 'casual_users',
        'registered': 'registered_users'
    }, inplace=True)

    return monthly_users

def hourly_trends(df):
    hourly_users = df.groupby('hr').agg({
        'casual': 'sum',
        'registered': 'sum'
    })
    hourly_users = hourly_users.reset_index()
    hourly_users.rename(columns={
        'casual': 'casual_users',
        'registered': 'registered_users'
    }, inplace=True)

    return hourly_users


# sidebar

with st.sidebar:
    # add logo
    st.image('https://raw.githubusercontent.com/novrizalrnd/bike_sharing/main/img/logo.png')

    st.sidebar.header('Date Filters:')
    start_date = pd.Timestamp(st.sidebar.date_input('Start date', df['dteday'].min().date()))
    end_date = pd.Timestamp(st.sidebar.date_input('End date', df['dteday'].max().date()))

st.sidebar.header('Visit My Github:')

with st.sidebar:
    st.markdown('[![Github](https://raw.githubusercontent.com/novrizalrnd/bike_sharing/main/img/github_logo.png)](https://github.com/novrizalrnd)')

# connect to df_filtered

df_filtered = df[
    (df['dteday'] >= str(start_date)) &
    (df['dteday'] <= str(end_date))
]

# assign df_filtered to functions

monthly_users = monthly_trends(df_filtered)
hourly_users = hourly_trends(df_filtered)

# mainpage

st.title(':bar_chart: Capital Bikeshare: Bike-Sharing Trend Dashboard')
st.markdown('##')

col1, col2, col3 = st.columns(3)

with col1:
    total_all_users = df_filtered['cnt'].sum()
    st.metric('Total Users', value=f'{total_all_users/1000000:.2f}M')
with col2:
    total_casual_users = df_filtered['casual'].sum()
    st.metric('Total Casual Users', value=f'{total_casual_users/1000:.2f}K')
with col3:
    total_registered_users = df_filtered['registered'].sum()
    st.metric('Total Registered Users', value=f'{total_registered_users/1000000:.2f}M')

st.markdown('---')

# chart

fig1 = px.line(monthly_users,
              x='month_year',
              y=['casual_users', 'registered_users'],
              color_discrete_sequence=['forestgreen', 'royalblue'],
              markers=True,
              title='Monthly Trend of Bikeshare Users').update_layout(xaxis_title='Month/Year', yaxis_title='Total Users')

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(hourly_users,
              x='hr',
              y=['casual_users', 'registered_users'],
              color_discrete_sequence=['forestgreen', 'royalblue'],
              markers=True,
              title='Hourly Trend of Bikeshare Users').update_layout(xaxis_title='Hour', yaxis_title='Total Users')

st.plotly_chart(fig2, use_container_width=True)

st.caption('Created by Novrizal Roynanda')

# hide streamlit style
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
