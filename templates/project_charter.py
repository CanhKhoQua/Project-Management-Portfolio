import streamlit as st

def display_project_charter():
    # Title of the Project Charter
    st.title("Project Charter")
    
    # Project Information
    st.header("Project Information")
    st.write("**Project Title**: Streamlit Project Management Portfolio")
    st.write("**Project Start Date**: 10/1/2024")
    st.write("**Projected Finish Date**: 12/3/2024")
    
    # Project Purpose/Justification
    st.header("Project Purpose/Justification")
    st.write("Developing project management skills")
    
    # Objectives Section
    st.header("Objectives")
    st.write("""
    1. Create the portfolio website wireframe  
    2. Creating WBS, mindmap, and Gantt chart on Streamlit  
    3. Implementing Streamlit elements into Flask
    """)
    
    # Scope Section
    st.header("Scope")
    st.write("The knowledge and skills gained through class lessons and readings")
    st.subheader("In Scope:")
    st.write("- All tasks related to creating the portfolio and integrating Streamlit with Flask")
    st.subheader("Out of Scope:")
    st.write("- Tasks unrelated to the website development and project management skills development")
    
    # Stakeholders Section
    st.header("Stakeholders")
    st.write("""
    1. Professor  
    2. Flask  
    3. Streamlit
    """)
    
    # Roles and Responsibilities Section
    st.header("Roles and Responsibilities")
    st.write("""
    **Role 1**: Rajeev Kunaparaju - Project Manager (kunaparv@mail.uc.edu)  
    **Role 2**: Loc Nguyen - Developer (nguye2lc@mail.uc.edu)  
    **Role 3**: David Rome - Developer (romedt@mail.uc.edu)  
    **Role 4**: Tanner Kern - Designer (kerntr@mail.uc.edu)  
    **Role 5**: Conner King - Researcher (king4cr@mail.uc.edu)  
    **Role 6**: Noah Ashcraft - Researcher (ashcrant@mail.uc.edu)  
    **Role 7**: Sam Anderson - Researcher (ander4sl@mail.uc.edu)  
    """)
    
    # Milestones Section
    st.header("Milestones")
    st.write("""
    1. **Description**: Get website foundation finished by end of next week **Date**: 10/11/2024  
    2. **Description**: Milestone check-in class to ensure we are on the right path  
    3. **Description**: Submission of final project on or before 12/3/2024
    """)
    
    # Risks Section
    st.header("Risks")
    st.write("""
    1. Poor grade  
    2. Missing deadlines and playing catch-up, hurting performance in other classes  
    3. Poor attendance of members creating imbalance of work for others
    """)
    
    # Budget Estimate Section
    st.header("Budget Estimate")
    st.write("""
    $240 for all members Co-Pilot
     for developers to use Streamlit
    """)
    
    # Approval Signatures Section
    st.header("Approval Signatures")
    st.write("""
    **Project Sponsor**: Streamlit  
    **Project Manager**: Rajeev Kunaparaju
    """)

if __name__ == "__main__":
    display_project_charter()
