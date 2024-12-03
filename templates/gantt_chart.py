import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# File to save data
DATA_FILE = 'data/gantt_chart_data.csv'

def save_data(df):
    """Saves the DataFrame to a CSV file."""
    df.to_csv(DATA_FILE, index=False, encoding='utf-8')

def load_data():
    """Loads data from the CSV file."""
    try:
        df = pd.read_csv(DATA_FILE, encoding='utf-8')
        # Ensure that date columns are parsed correctly
        df['Start'] = pd.to_datetime(df['Start'], dayfirst=False).dt.date
        df['Finish'] = pd.to_datetime(df['Finish'], dayfirst=False).dt.date
        
        # Add a small time offset to Finish date if it's the same as Start date
        df['Finish'] = df.apply(lambda row: row['Finish'] if row['Start'] != row['Finish'] else row['Finish'] + timedelta(hours=1), axis=1)
        
        return df
    except FileNotFoundError:
        # Return an empty DataFrame if the file doesn't exist
        return pd.DataFrame(columns=["Task", "Start", "Finish", "Dependencies"])

def display_gantt_chart():
    """Displays the Gantt chart and allows task addition."""
    st.title("Gantt Chart")

    # Load existing task data
    df = load_data()

    # Form to add a new task
    with st.form("add_task"):
        st.write("Add a new task")
        task_name = st.text_input("Task")
        task_start = st.date_input("Start Date")
        task_finish = st.date_input("Finish Date")
        task_dependencies = st.text_input("Dependencies")
        
        add_task_button = st.form_submit_button("Add Task")
        
        if add_task_button:
            # Validate form inputs
            if not task_name or not task_start or not task_finish:
                st.error("Please fill in all fields.")
            elif task_finish < task_start:
                st.error("Finish date cannot be earlier than start date.")
            else:
                # Check for duplicates
                is_duplicate = ((df['Task'] == task_name) & 
                                (df['Start'] == pd.Timestamp(task_start).date()) & 
                                (df['Finish'] == pd.Timestamp(task_finish).date())).any()
                
                if is_duplicate:
                    st.warning("This task already exists.")
                else:
                    # Append new task to the DataFrame
                    new_task = pd.DataFrame({
                        'Task': [task_name],
                        'Start': [task_start],
                        'Finish': [task_finish],
                        'Dependencies': [task_dependencies]
                    })
                    df = pd.concat([df, new_task], ignore_index=True)
                    
                    # Save the updated tasks to the CSV
                    save_data(df)
                    st.success("Task added and saved!")
                    # Reload data to ensure the Gantt chart is updated
                    df = load_data()

    # Delete functionality
    with st.form("delete_task"):
        st.write("Delete a task")
        task_to_delete = st.selectbox("Select a task to delete", df['Task'].unique() if not df.empty else [])
        delete_task_button = st.form_submit_button("Delete Task")
        
        if delete_task_button:
            if task_to_delete:
                # Remove the selected task from the DataFrame
                df = df[df['Task'] != task_to_delete]
                
                # Save the updated tasks to the CSV
                save_data(df)
                st.success("Task deleted successfully!")
                # Reload data to ensure the Gantt chart is updated
                df = load_data()

    # Filter out rows with invalid dates
    df = df.dropna(subset=['Start', 'Finish'])

    # Check if data is valid for display
    if df.empty:
        st.write("No tasks to display.")
    else:
        # Calculate dynamic height for better display
        chart_height = 400 + len(df) * 20

        # Plot the Gantt chart with proper datetime format
        fig = px.timeline(
            df,
            x_start="Start",
            x_end="Finish",
            y="Task",
            color="Dependencies",
            title="Project Timeline"
        )

        # Ensure proper layout
        fig.update_layout(
            xaxis_title="Timeline",
            yaxis_title="Tasks",
            hovermode="x",
            dragmode="pan",
            height=chart_height,
            autosize=True,
            margin=dict(l=20, r=20, t=30, b=20),  # Reduce margins
            xaxis=dict(tickformat="%Y-%m-%d")  # Format the X axis as Date
        )

        # Enable horizontal scroll if needed
        st.plotly_chart(fig, use_container_width=True)

# Main entry point
if __name__ == "__main__":
    display_gantt_chart()
