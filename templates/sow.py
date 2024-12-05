import streamlit as st

def display_statement_of_work():
    st.title("Statement of Work (SOW)")

    # Team Roles and Responsibilities Section
    st.header("Team Roles and Responsibilities")

    # Team members data (excluding the first "hero" member)
    team_members = [
        {"name": "Rajeev Kunaparaju", "role": "Project Manager", 
         "responsibility": "Currently focused on helping the team stay on track and communicating with everyone about what they are currently working on.",
         "image": "static/images/rajeev_image.png"},
        {"name": "David Rome", "role": "Developer", 
         "responsibility": "Responsible for the styling and layout of the page.",
         "image": "static/images/david_image.png"},
        {"name": "Loc Nguyen", "role": "Developer", 
         "responsibility": "Responsible for setting up the web page including displaying all the materials on the web page using Streamlit and deploying it online.",
         "image": "static/images/loc_image.png"},
        {"name": "Tanner Kern", "role": "Designer", 
         "responsibility": "Website Mock-ups and aid in development. Project charter development. Gantt Chart content development.",
         "image": "static/images/tanner_image.png"},
        {"name": "Conner King", "role": "Researcher", 
         "responsibility": "Researched whether to use Streamlit, Flask, or both. Then created a cost estimation table. Along with a draft of a critical path analysis and developed a Risk Management Plan.",
         "image": "static/images/conner_image.png"},
        {"name": "Noah Ashcraft", "role": "Researcher", 
         "responsibility": "Worked on researching topics and tasks related to the project when needed, and communicating with other members to see what assistance can be provided for them, and worked closely with developers. Also created the AOA Network Diagram and Critical Path Analysis. Wrote the project's welcome statement on the portfolio's homepage, and helped finish up Gantt chart entries.",
         "image": "static/images/noah_image.png"},
        {"name": "Sam Anderson", "role": "Researcher", 
         "responsibility": "As a researcher for this project, I was responsible for several key deliverables that played a vital role in the planning and execution of the portfolio. My primary contributions included:\n"
                          "- **Project Charter**: I developed the project charter, which established the project's scope, defined team roles and responsibilities, and outlined the success criteria. It also included a detailed timeline, budget, and a comprehensive plan to ensure the final project was delivered on time and met all requirements.\n"
                          "- **Cost Estimates**: I conducted an analysis to estimate the potential costs of the project, factoring in the hypothetical expenses we would incur if student resources were not available. These estimates were benchmarked against University of Cincinnati charges to provide a realistic financial framework.\n"
                          "- **Cost Risk Evaluation**: I identified potential cost-related risks, including financial and time-related challenges that could arise if the project encountered setbacks. This evaluation included strategies to mitigate these risks, ensuring project stability and feasibility.",
         "image": "static/images/sam_image.png"},
        {"name": "Elijah Garman", "role": "Prototyper/Designer", 
         "responsibility": "Responsible for using Figma and other tools to map out and create website mockups. Creating and designing a visual for the work breakdown structure, status report, and progress report.\n"
                        "- **Cost Risk Evaluation**: I identified potential cost-related risks, including financial and time-related challenges that could arise if the project encountered setbacks. This evaluation included strategies to mitigate these risks, ensuring project stability and feasibility.\n",
         "image": "static/images/elijah_image.png"},
    ]

    # Display the remaining team members in the same "hero" style
    for member in team_members:
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image(member['image'], width=230)

        with col2:
            st.title(member['name'], anchor=False)
            st.write(f"**{member['role']}**")
            st.write(f"{member['responsibility']}")

    #Deliverables Schedule section
    st.title("Deliverables Schedule")
    st.subheader("October 1st: Group Formation/Decide on Project Framework")
    st.write(
        "We created a group for the project and delegated roles to everyone. "
        "The team then decided on a framework, Streamlit, which would be used to build the portfolio."
    )

    st.subheader("October 14th: Develop Website Wireframe")
    st.write(
        "Developed a basic framework using HTML to sketch how the portfolio might look. "
        "This included work on an interactive Gantt chart within Streamlit."
    )

    st.subheader("October 15th: Present Wireframe Prototype")
    st.write(
        "Presented a rough prototype of the website's layout and discussed features and improvements "
        "we planned to develop further."
    )

    st.subheader("November 18th: Create and Implement Portfolio Documents into Website")
    st.write(
        "Added additional pages to the portfolio, including the work breakdown structure, a refined Gantt chart, "
        "statement of work, critical path analysis, cost estimates, status and reports template, and risk management details."
    )

    st.subheader("November 19th: Present Midway Project Progress")
    st.write(
        "Presented a nearly complete website showcasing all major elements outlined in the project checklist."
    )

    st.subheader("November 26th: Refine Current Portfolio Content and Website")
    st.write(
        "Reviewed the project checklist to ensure all required elements were included. "
        "Performed final cleanups and enhancements to make the website more visually appealing and polished."
    )

    st.subheader("December 5th: Final Project Showcase/Presentation")
    st.write(
        "Presented the finished portfolio, highlighting all completed components and meeting project expectations."
    )
# Main entry point
if __name__ == "__main__":
    display_statement_of_work()
