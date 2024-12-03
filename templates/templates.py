import streamlit as st

def display_template():

    # Title Project Progress Report
    st.title("IT Project Progress Report")

    # Markdown content
    st.markdown("""
    ## Project Information
    - **Project Name**: Streamlit Project Management Portfolio  
    - **Project Manager**: Rajeev Kunaparaju  
    - **Date of Report**: _________________  
    - **Reporting Period**: From ______________ to _______________  

    ## Project Overview
    Provide a brief description of the project, its objectives, and the key deliverables. Include any important background information.


    ## Executive Summary
    ### Summary of Current Status
    A brief summary of the current project status (e.g., on track, behind schedule, etc.).

    ### Key Highlights
    - A summary of major accomplishments or updates since the last report.


    ## Project Status
    ### Overall Project Status
    - Current status (e.g., On Track, Delayed, At Risk, Completed).

    ### Progress
    - Percentage of completion compared to the project plan (e.g., 70% completed).

    ### Milestones Completed
    | Milestone  | Description  | Completion Date  |
    |------------|--------------|------------------|
    | Milestone 1| [Description]| [Completion Date]|
    | Milestone 2| [Description]| [Completion Date]|

    ### Upcoming Milestones
    | Milestone  | Description  | Expected Completion Date |
    |------------|--------------|--------------------------|
    | Milestone 1| [Description]| [Expected Completion Date]|
    | Milestone 2| [Description]| [Expected Completion Date]|


    ## Budget and Resource Status
    ### Budget Status
    - Overview of the project's budget status (e.g., on budget, over budget, etc.).

    ### Expenditure
    - Total amount spent so far and comparison with the planned budget.

    ### Resources
    - Resource usage, including human resources, hardware, software, and any external services.

    ### Resource Constraints
    - Any resource issues (e.g., staff shortages, equipment delays).


    ## Conclusion
    ### Summary of Progress
    - A brief overall assessment of the project's progress.

    ### Final Comments
    - Any additional comments, feedback, or notes for stakeholders.
    """)

    st.markdown("""  ---
    """)

    # Project Status Report

    st.title("IT Project Status Report")

    st.markdown("""
    ## Project Information
    - **Project Name**: Streamlit Project Management Portfolio  
    - **Project Manager**: Rajeev Kunaparaju  
    - **Date of Report**: _________________  
    - **Reporting Period**: From ______________ to _______________  

                
    ## Milestones and Deliverables

    | **Milestone/Deliverable**       | **Due Date**  | **Status**               | **Notes**                  |
    |---------------------------------|---------------|--------------------------|----------------------------|
    | Milestone 1 (e.g., development phase) | MM/DD/YYYY    | On Track / Delayed / Completed | Add any relevant notes.    |
    | Milestone 2 (e.g., development phase) | MM/DD/YYYY    | On Track / Delayed / Completed | Add any relevant notes.    |
    | Milestone 3 (e.g., testing phase)     | MM/DD/YYYY    | On Track / Delayed / Completed | Add any relevant notes.    |


    ## Key Accomplishments This Period
    - List major tasks or milestones that were completed during this reporting period:
    - **Task 1**: __________________________  
    - **Task 2**: __________________________  
    - **Task 3**: __________________________  


    ## Issues and Challenges

    ### Critical Issues
    List any major issues that are affecting project progress, such as delays, resource shortages, or technical challenges:
    - **Issue 1**: __________________________ (Impact: Low / Medium / High)  
    - **Issue 2**: __________________________ (Impact: Low / Medium / High)  

    ### Mitigation Actions
    Describe any actions being taken to address these issues:
    - **Action 1**: __________________________  
    - **Action 2**: __________________________  


    ## Additional Notes or Comments
    - Add any other relevant information or observations that stakeholders should be aware of.
    """)


if __name__ == "__main__":
    display_template()   