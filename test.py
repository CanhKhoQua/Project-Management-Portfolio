import streamlit as st
from streamlit_option_menu import option_menu
import pandas as strepd
import plotly.express as px
import function

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Gantt Chart", "Work Breakdown Structure", "Mindmap"],
        icons=["bar-chart-steps", "list-ul", "diagram-3"],
        
    )

if selected == "Gantt Chart":
    st.title(f"{selected}")

if selected == "Work Breakdown Structure":
    st.title(f"{selected}")

if selected == "Mindmap":
    st.title(f"{selected}")

    
