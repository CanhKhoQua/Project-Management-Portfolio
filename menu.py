import streamlit as st
from streamlit_option_menu import option_menu

# Apply CSS styling to the sidebar and the main header
st.markdown(
    """
    <style>
    /* Sidebar customization */
    .css-1d391kg { /* Sidebar container class, this might change across versions */
        background-color: #333;  /* Dark background color */
        padding: 20px;
    }
    .css-1d391kg .css-1v0mbdj { /* The menu title in sidebar */
        color: #FFF;  /* White font color */
    }
    .css-1d391kg .css-17eq0hr {  /* Sidebar menu items */
        color: #80DDFF;  /* Light blue font color */
        font-size: 1.2em;
    }
    .css-1d391kg .css-17eq0hr:hover {
        color: #FFF;  /* White font color on hover */
    }

    /* Title styling */
    .title-header {
        background-color: #80DDFF;
        color: black;
        text-align: center;
        border: solid 3px black;
        padding: 20px;
        font-size: 2em;
        margin-bottom: 20px;
    }
    
    /* Styling the page content */
    .stMarkdown {
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for page selection if it doesn't exist
if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Home"

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Project Charter", "Work Breakdown Structure", "Gantt Chart", "Statement of Work", "Mindmap", "Critical Path Analysis", "Cost Estimates", "Status and Progress Reports Templates", "Risk Management Plan"],
        icons=["house", "file-earmark-text", "list-ul", "bar-chart-steps", "person-workspace", "diagram-2", "diagram-3", "cash-coin", "file-bar-graph", "shield-exclamation"],
        default_index=["Home", "Project Charter", "Work Breakdown Structure", "Gantt Chart", "Statement of Work", "Mindmap", "Critical Path Analysis", "Cost Estimates", "Status and Progress Reports Templates", "Risk Management Plan"].index(st.session_state["selected_page"]),
        key="selected"
    )

# Update the selected page in session state
if st.session_state["selected_page"] != selected:
    st.session_state["selected_page"] = selected

# Display header
st.markdown('<h1 class="title-header">Group 5 Project Management Portfolio</h1>', unsafe_allow_html=True)

# Function to run the code in a given file
def run_script(script_path):
    with open(script_path, "r") as file:
        script_code = file.read()
        exec(script_code, globals())

# Content display based on selected page
if st.session_state["selected_page"] == "Home":
    run_script("templates/home_page.py")
elif st.session_state["selected_page"] == "Project Charter":
    run_script("templates/project_charter.py")
elif st.session_state["selected_page"] == "Work Breakdown Structure":
    run_script("templates/wbs.py")
elif st.session_state["selected_page"] == "Gantt Chart":
    run_script("templates/gantt_chart.py")
elif st.session_state["selected_page"] == "Statement of Work":
    run_script("templates/sow.py")
elif st.session_state["selected_page"] == "Mindmap":
    run_script("templates/mindmap.py")
elif st.session_state["selected_page"] == "Critical Path Analysis":
    run_script("templates/cpa.py")
elif st.session_state["selected_page"] == "Cost Estimates":
    run_script("templates/costestimates.py")
elif st.session_state["selected_page"] == "Status and Progress Reports Templates":
    pass
elif st.session_state["selected_page"] == "Risk Management Plan":
    run_script("templates/costrisk.py")

