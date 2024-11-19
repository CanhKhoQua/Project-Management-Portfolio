import streamlit as st

def display_statement_of_work():
    st.title("Statement of Work (SOW)")

    # Team Roles and Responsibilities Section
    st.header("Team Roles and Responsibilities")

    # Team members data (excluding the first "hero" member)
    team_members = [
        {"name": "Rajeev Kunaparaju", "role": "Project Manager", 
         "responsibility": "Focused on helping the team stay on track and communicating with everyone about their current tasks.",
         "image": "static/images/rajeev_image.png"},
        {"name": "David Rome", "role": "Developer", 
         "responsibility": "Responsible for the styling and layout of the page.",
         "image": "static/images/david_image.png"},
        {"name": "Loc Nguyen", "role": "Developer", 
         "responsibility": "Responsible for setting up the web page, including displaying the materials using Streamlit.",
         "image": "static/images/loc_image.png"},
        {"name": "Tanner Kern", "role": "Designer", 
         "responsibility": "Website Mock-ups and aid in development. Project charter development.",
         "image": "static/images/tanner_image.png"},
        {"name": "Conner King", "role": "Researcher", 
         "responsibility": "Researched whether to use Streamlit, Flask, or both. Then created a cost estimation table. Along with a draft of a critical path analysis and developed a Risk Management Plan.",
         "image": "static/images/conner_image.png"},
        {"name": "Noah Ashcraft", "role": "Researcher", 
         "responsibility": "Working on researching topics and tasks related to the project when needed, and communicating with other members to see what assistance can be provided for them.",
         "image": "static/images/noah_image.png"},
        {"name": "Sam Anderson", "role": "Researcher", 
         "responsibility": "Working with the team to see what is needed and helping figure out what softwares we can use to help further our project and optimize performance.",
         "image": "static/images/sam_image.png"},
        {"name": "Trey Burling", "role": "Role Pending", 
         "responsibility": "To be assigned.",
         "image": "static/images/trey_image.png"},
        {"name": "Elijah Garman", "role": "Prototyper/Designer", 
         "responsibility": "Used Figma and other tools to map out and create mockups, wireframes, and webpages.",
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

# Main entry point
if __name__ == "__main__":
    display_statement_of_work()
