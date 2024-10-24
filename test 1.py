import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a task
def add_task(name, start_date, end_date):
    st.session_state.tasks.append({'Task': name, 'Start': start_date, 'Finish': end_date})

# Function to delete a task
def delete_task(index):
    del st.session_state.tasks[index]

# Function to update a task
def update_task(index, name, start_date, end_date):
    st.session_state.tasks[index] = {'Task': name, 'Start': start_date, 'Finish': end_date}

# Sidebar for task input
st.sidebar.header("Add/Update Task")
task_name = st.sidebar.text_input("Task Name")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

if st.sidebar.button("Add Task"):
    add_task(task_name, start_date, end_date)

# Display tasks
st.header("Gantt Chart")
if st.session_state.tasks:
    df = pd.DataFrame(st.session_state.tasks)
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Project Gantt Chart")
    st.plotly_chart(fig)

    # Task management
    st.header("Manage Tasks")
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"Task {i+1}: {task['Task']} (Start: {task['Start']}, Finish: {task['Finish']})")
        if st.button(f"Delete Task {i+1}"):
            delete_task(i)
        if st.button(f"Update Task {i+1}"):
            update_task(i, task_name, start_date, end_date)
else:
    st.write("No tasks added yet.")
