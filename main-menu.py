import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import function
from datetime import datetime

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Gantt Chart", "Work Breakdown Structure", "Mindmap"],
        icons=["bar-chart-steps", "list-ul", "diagram-3"],
        
    )

if selected == "Gantt Chart":
    st.title(f"{selected}")

    df = function.load_data()
    # Form to add new tasks
    with st.form("add_task"):
        st.write("Add a new task")
        task_name = st.text_input("Task")
        task_start = st.date_input("Start Date", datetime.now())
        task_finish = st.date_input("Finish Date", datetime.now())
        task_resource = st.text_input("Resource")
        
        add_task_button = st.form_submit_button("Add Task")
        
        if add_task_button:
            # Append new task
            new_task = pd.DataFrame({
                'Task': [task_name],
                'Start': [task_start],
                'Finish': [task_finish],
                'Resource': [task_resource]
            })
            df = pd.concat([df, new_task], ignore_index=True)
            
            # Save the updated tasks
            function.save_tasks(df)
            st.success("Task added and saved!")

    # Plot the Gantt chart
    if not df.empty:
        fig = px.timeline(
            df,
            x_start="Start",
            x_end="Finish",
            y="Task",
            color="Resource",
            title="Project Timeline"
        )
        fig.update_layout(
            xaxis_title="Timeline",
            yaxis_title="Tasks",
            hovermode="x",
            dragmode="pan"
        )
        st.plotly_chart(fig)


if selected == "Work Breakdown Structure":
    st.title(f"{selected}")

if selected == "Mindmap":
    st.title(f"{selected}")

    
