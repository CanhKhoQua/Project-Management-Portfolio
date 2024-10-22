import streamlit as st
import pandas as pd

# File to save data
DATA_FILE = 'gantt_chart_data.csv'

# Function to add a task
def add_task(name, start_date, end_date):
    st.session_state.tasks.append({'Task': name, 'Start': start_date, 'Finish': end_date})

# Function to delete a task
def delete_task(index):
    del st.session_state.tasks[index]

# Function to update a task
def update_task(index, name, start_date, end_date):
    st.session_state.tasks[index] = {'Task': name, 'Start': start_date, 'Finish': end_date}

# Function to load data
def load_data():
    try:
        return pd.read_csv(DATA_FILE, parse_dates=['Start', 'Finish'])
    except FileNotFoundError:
        return pd.DataFrame(columns=['Task', 'Start', 'Finish', 'Resource'])

# Function to save data
def save_data(df):
    df.to_csv(DATA_FILE, index=False)