import streamlit as st

def display_cpa():
    # Display the image
    st.image("static\\images\\Critical Path Analysis.png", caption="AOA Diagram", use_column_width=True)
    
    # Add a title and explanation of the critical path
    st.title("Critical Path Analysis")
    st.markdown("""
    **Critical Path Analysis** is an essential aspect of project planning. Below are the details of the activity paths analyzed:

    **Activity Key:**
    - **A** - Group Formation
    - **B** - Decide on Project Framework
      - **B1** - Streamlit
      - **B2** - Flask
      - **B3** - HTML
    - **C** - Develop Website Wireframe
      - **C1** - Develop Streamlit Wireframe
      - **C2** - Develop Flask Wireframe
      - **C3** - Develop HTML Wireframe
    - **D** - Present Wireframe Prototype
    - **E** - Create and Implement Portfolio Documents into Website
    - **F** - Create Additional Pages
    - **G** - Present Midway Project Progress
    - **H** - Refine Current Portfolio Content and Website
    - **J** - Final Project Showcase/Presentation

    **Critical Path Analysis:**
    - **Path 1:** A-B1-C1-D-E-F-G-H-J (Length = 22 days)
    - **Path 2:** A-B2-C2-D-E-F-G-H-J (Length = 21 days)
    - **Path 3:** A-B3-C3-D-E-F-G-H-J (Length = 19 days)

    The **critical path** is **Path 1**, which is 22 days in length. This represents the timeline for developing with Streamlit, as opposed to HTML or Flask, to build the portfolio.
    """)

if __name__ == "__main__":
    display_cpa()
