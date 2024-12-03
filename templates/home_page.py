import streamlit as st

def display_homepage():
    st.markdown(
        """
        Welcome to the Group 5 Project Management Portfolio. This portfolio was completed for the IT4020 Management in Information Technology course taught at the University of Cincinnati. It has been created using Streamlit, with the help and expertise of Loc Nguyen and David Rome, who are the developers of this portfolio website. Other members of the team include designers (Tanner Kern and Elijah Garman), researchers (Sam Anderson, Conner King, and Noah Ashcraft), and the project manager (Rajeev Kunaparaju). For more details on the entire team responsible for this portfolio, visit the Project Charter and Statement of Work pages. Other pages on this portfolio website cover aspects and documentation that every member of the project has learned throughout the course, and both designers and researchers helped develop the documentation needed for the content of the portfolio itself. We hope you enjoy this portfolio, and can learn something about project management in information technology.
        """
    )

  

    # Call to Action
    st.subheader("What You'll Learn")
    st.markdown(
        """
        This portfolio offers insights into **project management in information technology**:
        - Detailed project planning and execution strategies.
        - Team collaboration and role responsibilities.
        - Key documentation and lessons learned throughout the course.
        
        We hope this portfolio inspires and educates others on the importance of effective project management!
        """
    )


if __name__ == "__main__":
    display_homepage()
