import streamlit as st
import base64

def display_statement_of_work():
    st.title("Statement of Work (SOW)")

    # Team Roles and Responsibilities Section
    st.header("Team Roles and Responsibilities")

    # Team members data
    team_members = [
        {"name": "Rajeev Kunaparaju", "role": "Project Manager", 
         "responsibility": "Focused on helping the team stay on track and communicating with everyone about their current tasks.",
         "image": "templates/images/sample.jpg"},
        {"name": "David Rome", "role": "Role Pending", "responsibility": "To be assigned.",
         "image": "templates/images/sample.jpg"},
        {"name": "Loc Nguyen", "role": "Developer", 
         "responsibility": "Responsible for setting up the web page, including displaying the materials using Streamlit.",
         "image": "templates/images/loc_image.jpeg"},
        {"name": "Tanner Kern", "role": "Designer", 
         "responsibility": "Website Mock-ups and aid in development. Project charter development.",
         "image": "templates/images/sample.jpg"},
        {"name": "Conner King", "role": "Researcher", 
         "responsibility": "Researching if it's better to use both Streamlit and Flask or if we should narrow our framework to one.",
         "image": "templates/images/sample.jpg"},
        {"name": "Noah Ashcraft", "role": "Researcher", 
         "responsibility": "Working on researching topics related to the project and assisting other members as needed.",
         "image": "templates/images/noah_image.jpg"},
        {"name": "Sam Anderson", "role": "Role Pending", "responsibility": "To be assigned.",
         "image": "templates/images/sample.jpg"},
        {"name": "Trey Burling", "role": "Role Pending", "responsibility": "To be assigned.",
         "image": "templates/images/sample.jpg"},
        {"name": "Elijah Garman", "role": "Prototype Contributor", 
         "responsibility": "Contributed to prototyping using Figma.",
         "image": "templates/images/sample.jpg"},
    ]

    # Apply custom CSS to create a flex layout for team members
    st.markdown("""
        <style>
            .team-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                width: 80%;
                margin: 0 auto;
            }
            .team-member {
                text-align: center;
                padding: 20px;
                flex: 1;
                min-width: 250px; /* Ensure minimum width for each member */
            }
            .team-member img {
                border-radius: 50%;
                width: 180px;
                height: 180px;
                object-fit: cover;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Render the team members in a flexible layout
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    for i in range(0, len(team_members), 3):
        col1, col2, col3 = st.columns(3)
        with col1:
            if i < len(team_members):
                member = team_members[i]
                st.markdown(f"""
                    <div class="team-member">
                        <img src="data:image/jpeg;base64,{base64.b64encode(open(member['image'], 'rb').read()).decode()}" alt="{member['name']}">
                        <h2>{member['name']}</h2>
                        <h4>{member['role']}</h4>
                        <p>{member['responsibility']}</p>
                    </div>
                """, unsafe_allow_html=True)

        with col2:
            if i + 1 < len(team_members):
                member = team_members[i + 1]
                st.markdown(f"""
                    <div class="team-member">
                        <img src="data:image/jpeg;base64,{base64.b64encode(open(member['image'], 'rb').read()).decode()}" alt="{member['name']}">
                        <h2>{member['name']}</h2>
                        <h4>{member['role']}</h4>
                        <p>{member['responsibility']}</p>
                    </div>
                """, unsafe_allow_html=True)

        with col3:
            if i + 2 < len(team_members):
                member = team_members[i + 2]
                st.markdown(f"""
                    <div class="team-member">
                        <img src="data:image/jpeg;base64,{base64.b64encode(open(member['image'], 'rb').read()).decode()}" alt="{member['name']}">
                        <h2>{member['name']}</h2>
                        <h4>{member['role']}</h4>
                        <p>{member['responsibility']}</p>
                    </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)