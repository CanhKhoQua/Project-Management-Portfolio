import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from datetime import datetime
from templates import ganttchart, sow

# Check for query parameters in the URL
default_page = st.query_params.get("page", ["Gantt Chart"])[0]

# Sidebar with navigation options
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Gantt Chart", "Work Breakdown Structure", "Mindmap", "SOW"],
        icons=["bar-chart-steps", "list-ul", "diagram-3", "person-workspace"],
        default_index=["Gantt Chart", "Work Breakdown Structure", "Mindmap", "SOW"].index(default_page),
    )

# Show content based on selected option
if selected == "Gantt Chart":
    ganttchart.display_gantt_chart()

if selected == "Work Breakdown Structure":
    st.title(f"{selected}")

if selected == "Mindmap":
    st.title(f"{selected}")

if selected == "SOW":
    sow.display_statement_of_work()
