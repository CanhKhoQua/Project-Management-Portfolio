import streamlit as st

# Function to add a task
def add_task(name, start_date, end_date):
    st.session_state.tasks.append({'Task': name, 'Start': start_date, 'Finish': end_date})

# Function to delete a task
def delete_task(index):
    del st.session_state.tasks[index]

# Function to update a task
def update_task(index, name, start_date, end_date):
    st.session_state.tasks[index] = {'Task': name, 'Start': start_date, 'Finish': end_date}