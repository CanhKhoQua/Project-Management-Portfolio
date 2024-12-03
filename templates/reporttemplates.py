import streamlit as st

def display_report_template():
    # Display the report title
    st.title("IT Project Progress Report")

    # Project Information
    st.write("""
    ### Project Name: Flask Project Management Portfolio
    ### Project Manager: Rajeev Kunaparaju
    ### Date of Report: _________________
    ### Reporting Period: From ______________ to _______________
    """)

    # Project Overview
    st.write("""
    ### Project Overview
    Provide a brief description of the project, its objectives, and the key deliverables. Include any important background information.
    """)

    # Executive Summary
    st.write("""
    ### Executive Summary

    #### Summary of Current Status:
    A brief summary of the current project status (on track, behind schedule, etc.)

    #### Key Highlights:
    A summary of major accomplishments or updates since the last report.
    """)

    # Project Status
    st.write("""
    ### Project Status

    #### Overall Project Status:
    (e.g., On Track, Delayed, At Risk, Completed)

    #### Progress:
    Percentage of completion compared to the project plan (e.g., 70% completed).

    #### Milestones Completed:
    List of completed milestones or deliverables:

    | Milestone              | Description                | Completion Date  |
    |------------------------|----------------------------|------------------|
    | Milestone 1            | [Description]              | [Completion Date]|
    | Milestone 2            | [Description]              | [Completion Date]|

    #### Upcoming Milestones:
    Key milestones expected to be achieved in the upcoming period:

    | Milestone              | Description                | Expected Completion Date |
    |------------------------|----------------------------|--------------------------|
    | Milestone 1            | [Description]              | [Expected Completion Date]|
    | Milestone 2            | [Description]              | [Expected Completion Date]|
    """)

    # Budget and Resource Status
    st.write("""
    ### Budget and Resource Status

    #### Budget Status:
    Overview of the project's budget status (on budget, over budget, etc.).

    #### Expenditure:
    Total amount spent so far and comparison with the planned budget.

    #### Resources:
    Resource usage, including human resources, hardware, software, and any external services.

    #### Resource Constraints:
    Any resource issues (e.g., staff shortages, equipment delays).
    """)

    # Conclusion
    st.write("""
    ### Conclusion

    #### Summary of Progress:
    A brief overall assessment of the project's progress.

    #### Final Comments:
    Any additional comments, feedback, or notes for stakeholders.
    """)

if __name__ == "__main__":
    display_report_template()