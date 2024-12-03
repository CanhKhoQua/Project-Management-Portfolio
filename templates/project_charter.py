import streamlit as st

def display_project_charter():
    # Title of the Project Charter
    st.title("Project Charter")

    st.markdown("The main purpose of this project is to develop a personal portfolio. The project served as a practical demonstration of concepts and skills we learned during the course.  The project put a heavy emphasis on teamwork and communication with the team, showing that we could work on individual assignments that all played the main goal. It allowed us to take what we learned in the class and sample a real-world project demonstrating our ability to work in a team or lead a team to deliver a working final product.")
    
    # Project Overview
    st.header("Project Overview")

    st.write("""
    | Field                    | Details                                   |
    |--------------------------|-------------------------------------------|
    | Project Name             | Streamlit Project Management Portfolio   |
    | Project Sponsor          | University of Cincinnati                 |
    | Project Manager (PM)     | Rajeev Kunaparaju                        |
    | PM Email Address         | kunaparv@mail.uc.edu                     |
    | PM Phone Number          | N/A                                      |
    | Business Unit            | Room 504 of Teachers Dyers College       |
    | Expected Start Date      | 10/1/2024                                |
    | Expected Completion Date | 12/3/2024                                |
    | Estimated Budget         | $7718                                    |
    """)

    
    # Project Description
    st.title("Project Description")

    st.write("""
    ### Purpose
    The purpose of this project is to demonstrate the skills we have learned in class and show an ability to be assigned at random to a team and work together to execute the tasks to create the final project. We are to have individual roles and use the concepts of working on a project team we have learned in class to work on specific tasks that contribute to the team, requiring an understanding of the work and coordination amongst each other.

    ### In-Scope
    - Creating a website to showcase a portfolio.
    - Implementing features with working functionality.
    - Ensuring that all the code works and what we worked to achieve is operable.

    ### Out-of-Scope
    - Any communication failures at the time of presentation.
    - Any technical interruptions with programs we have used to build the project.
    - Machines having unexpected errors at time of presentation limiting functionality.

    ### Key Deliverables
    - Project Charter
    - Work Breakdown Structure
    - Gantt Chart
    - Project Network Diagram
    - Risk Management Plan
    - Critical Path Analysis
    """)
    
    
    # Team members
    st.header("Team members")
    st.markdown("Provide a list of the team members, facilities, equipment, and other items that are essential to the success of the project. Use a simple table, like the one shown below.")
    st.write("""
    **Role 1**: Rajeev Kunaparaju - Project Manager (kunaparv@mail.uc.edu)  
    **Role 2**: Loc Nguyen - Developer (nguye2lc@mail.uc.edu)  
    **Role 3**: David Rome - Developer (romedt@mail.uc.edu)  
    **Role 4**: Tanner Kern - Designer (kerntr@mail.uc.edu)  
    **Role 5**: Conner King - Researcher (king4cr@mail.uc.edu)  
    **Role 6**: Noah Ashcraft - Researcher (ashcrant@mail.uc.edu)  
    **Role 7**: Sam Anderson - Researcher (ander4sl@mail.uc.edu)     
    **Role 8**: Elijah Garman - Designer (garmaneh@mail.uc.edu)  
             
    """)
    
    # Display communication details
    st.write("""
    ### Communication
    For this project, our team was able to meet twice a week in class as well as utilizing Microsoft Teams outside of the class to maintain communication outside of class hours. In moments when we all did not make it to class, the team was also able to make use of Zoom to check in.
    """)

    # Display schedule
    st.write("""
    ### Schedule
    Here are the key milestones and their respective dates:

    | Key Milestone         | Start Date | Completion Date |
    |-----------------------|------------|-----------------|
    | First team meeting    | 10/1/2024  | 10/1/2024       |
    | In class check up     | 11/19/2024 | 11/19/2024      |
    | Project Submission    | 12/3/2024  | 12/8/2024       |
    """)

    # Display risks
    st.write("""
    ### Risks
    Note any risks to project success, indicating their potential impact on the budget and timeline.

    | Potential Risk               | Perceived Impact      | Proposed Mitigation Strategy                                                       |
    |------------------------------|-----------------------|-----------------------------------------------------------------------------------|
    | Delay of graduation timeline  | Up to $2,610          | If this course is failed, you may need to retake it, possibly incurring additional costs. Retake the course. |
    | Retaking the course           | $523 per person       | Ensure everyone contributes to the project and maintains deadlines to prevent failure. |
    | Failing the project           | $523 per person       | Follow the project plan to ensure all deadlines are met and tasks are completed to a high standard. |
    """)

    #Stakeholders
    st.title("Stakeholder Approval Signatures")
    st.write("""
    #### Project Stakeholder: Streamlit
    #### Project Manager: Rajeev Kunaparaju
    """)

if __name__ == "__main__":
    display_project_charter()
