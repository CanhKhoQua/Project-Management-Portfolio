import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import pandas as pd
import plotly.express as px
from templates import ganttchart, sow  # Import display functions for specific pages

# Default page if query parameter is specified
default_page = st.experimental_get_query_params().get("page", ["Home"])[0]

# Sidebar with navigation options
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Gantt Chart", "Work Breakdown Structure", "Mindmap", "SOW"],
        icons=["house", "bar-chart-steps", "list-ul", "diagram-3", "person-workspace"],
        default_index=["Home", "Gantt Chart", "Work Breakdown Structure", "Mindmap", "SOW"].index(default_page),
    )

# Global styling for consistent look
st.markdown(
    """
    <style>
    * { box-sizing: border-box; }
    body { background-color: #B9B9B9; }
    
    .title-header {
        background-color: #80DDFF;
        color: black;
        text-align: center;
        border: solid 3px black;
        padding: 20px;
        font-size: 2em;
    }
    .nav-main { display: flex; justify-content: center; margin-bottom: 20px; }
    .nav-pages {
        display: flex; flex-direction: row; justify-content: center;
    }
    .nav-pages a {
        text-decoration: none;
        background-color: #62D9F3;
        color: black;
        font-weight: bold;
        border: solid 2px #5E9EFF;
        margin-right: 10px;
        margin-top: 5px;
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 0.8em;
    }
    .nav-pages a:hover { cursor: pointer; background-color: #5E9EFF; }
    #charter-anchor { margin-top: 40px; font-size: 1.8em; text-align: center; color: #333; }
    </style>
    """,
    unsafe_allow_html=True
)

# Content based on the selected page
if selected == "Home":
    # Home page layout and navigation links
    st.markdown('<h1 class="title-header">Group 5 Project Management Portfolio</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nav-main">
        <nav class="nav-pages">
            <a href="#">Home Page</a>
            <a href="#">Gantt Chart</a>
            <a href="#charter-anchor">Project Charter</a>
            <a href="#">Team Profile</a>
            <a href="#">WBS</a>
            <a href="#">SOW</a>
        </nav>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<h1 id="charter-anchor">Our Project Charter</h1>', unsafe_allow_html=True)
    st.write("Here you can include more information or an iframe for the project charter document.")

elif selected == "Gantt Chart":
    ganttchart.display_gantt_chart()  # Call function to display Gantt chart from ganttchart module

elif selected == "Work Breakdown Structure":
    st.title("Work Breakdown Structure")

elif selected == "Mindmap":
    st.title("Mindmap")

elif selected == "SOW":
    sow.display_statement_of_work()  # Call function to display SOW content from sow module
