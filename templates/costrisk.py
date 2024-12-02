import streamlit as st

def display_cost_risk_report():
    st.title("Cost Risk Analysis Report")

    st.header("Project Name: Personal Portfolio Project")
    st.text("Prepared By: Sam Anderson")

    st.subheader("Objective")
    st.write("""
    Analyze risks related to time and cost that could lead to failing the course and 
    requiring a retake, delaying graduation and adding to the money we will spend 
    on education in our time at Cincinnati, and propose strategies to minimize these risks.
    """)

    st.subheader("Project Overview")
    st.write("**Description:** Develop a personal portfolio to showcase skills learned in and outside of class.")
    st.write("**Budget:** Indirect costs such as tuition, software subscriptions, and time.")
    st.write("**Timeline:** 10/1/2024 – 12/13/2024.")

    st.subheader("Identified Cost Risks")
    risks = [
        {"Risk ID": "Risk 1", "Description": "Failing to complete the project on time", "Likelihood": "High", "Impact": "Critical"},
        {"Risk ID": "Risk 2", "Description": "Delivering a project that does not meet requirements", "Likelihood": "Medium", "Impact": "High"},
        {"Risk ID": "Risk 3", "Description": "Mismanaging time, leading to rushed work and errors", "Likelihood": "High", "Impact": "High"},
        {"Risk ID": "Risk 4", "Description": "Software or tool costs exceeding budget", "Likelihood": "Low", "Impact": "Medium"},
    ]
    for risk in risks:
        st.write(f"**{risk['Risk ID']}** - {risk['Description']}")
        st.write(f"- Likelihood: {risk['Likelihood']}")
        st.write(f"- Impact: {risk['Impact']}")

    st.subheader("Risk Impact Analysis")
    st.write("""
    **Risk 1 - Failing to Complete on Time**
    - Impact: Failing the class results in additional tuition costs (approximately $566) and delays in academic progression.
    - Root Cause: Poor time management or unforeseen technical challenges.
    - Affected Milestones: Project submission deadline.

    **Risk 2 - Not Meeting Requirements**
    - Impact: Low grades may require class retake.
    - Root Cause: Misunderstanding project goals or lack of instructor feedback.
    - Affected Milestones: Final grading.

    **Risk 3 - Time Mismanagement**
    - Impact: Errors from rushing lead to lower grades or incomplete work.
    - Root Cause: Procrastination or overcommitment to other tasks.
    - Affected Milestones: All project phases.

    **Risk 4 - Tool/Software Costs**
    - Impact: Unexpected costs can lead to financial strain.
    - Root Cause: Underestimating required software and tools.
    - Affected Milestones: Development phase.
    """)

    st.subheader("Risk Mitigation Strategies")
    mitigation_strategies = [
        {"Risk ID": "Risk 1", "Strategy": "Create and follow a detailed project schedule", "Cost": "Free"},
        {"Risk ID": "Risk 2", "Strategy": "Regularly review project requirements and seek feedback", "Cost": "Free"},
        {"Risk ID": "Risk 3", "Strategy": "Dedicate fixed weekly hours to project work", "Cost": "Free"},
        {"Risk ID": "Risk 4", "Strategy": "Use free and open-source tools or seek student discounts", "Cost": "Free or Discounted"},
    ]
    for strategy in mitigation_strategies:
        st.write(f"**{strategy['Risk ID']}** - {strategy['Strategy']} (Cost: {strategy['Cost']})")

    st.subheader("Contingency Plan")
    st.write("""
    - Allocate additional time buffers for unexpected delays.
    - Maintain open communication with the instructor and team members.
    - Prepare a backup plan for any failures on due date.
    """)

    st.subheader("Conclusion and Recommendations")
    st.write("""
    The main risks around this project are centered on the need to retake the course or failing if we don’t achieve a satisfactory grade. 
    A solid approach, ensuring a good timeline, and maintaining effective communication among team members can help mitigate the risk. 
    Contingency plans will be essential for addressing any potential hiccups.
    """)

# Call this function in your Streamlit app
display_cost_risk_report()
