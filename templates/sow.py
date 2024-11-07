import streamlit as st

# Statement of Work (SOW) Page with Predefined Team Roles and Responsibilities
def display_statement_of_work():
    st.title("Statement of Work (SOW)")

    # Team Roles and Responsibilities Section
    st.header("Team Roles and Responsibilities")
    
    # Team members data
    team_members = [
        {"name": "Rajeev Kunaparaju", "role": "Project Manager", 
         "responsibility": "Focused on helping the team stay on track and communicating with everyone about their current tasks."},
        {"name": "Loc Nguyen", "role": "Developer", 
         "responsibility": "Responsible for setting up the web page, including displaying the Gantt chart, work breakdown structure, mind map, and statement of work using Streamlit."},
        {"name": "David Rome", "role": "Role Pending", "responsibility": "To be assigned."},
        {"name": "Tanner Kern", "role": "Role Pending", "responsibility": "To be assigned."},
        {"name": "Conner King", "role": "Role Pending", "responsibility": "To be assigned."},
        {"name": "Noah Ashcraft", "role": "Researcher", 
         "responsibility": "Working on researching topics related to the project and assisting other members as needed."},
        {"name": "Sam Anderson", "role": "Role Pending", "responsibility": "To be assigned."},
        {"name": "Trey Burling", "role": "Role Pending", "responsibility": "To be assigned."},
        {"name": "Elijah Garman", "role": "Prototype Contributor", 
         "responsibility": "Contributed to prototyping using Figma."},
    ]

    # Display each team member's information in a grid layout
    num_columns = 2  # Adjust the number of columns as needed
    columns = st.columns(num_columns)
    
    for index, member in enumerate(team_members):
        col = columns[index % num_columns]
        with col:
            st.subheader(member["name"])
            st.write(f"**Role:** {member['role']}")
            st.write(f"**Responsibilities:** {member['responsibility']}")
            st.write(" ")



