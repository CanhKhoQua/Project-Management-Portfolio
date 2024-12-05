import streamlit as st

def display_wbs():
    st.image("static/images/WBS.png", caption="Work Breakdown Structure", use_column_width=True)
    st.markdown("""
    | Task                     | Start Date  | End Date    | Duration  |
    |--------------------------|-------------|-------------|-----------|
    | **Research/Planning**    |             |             | **58 Days** |
    | Delegating roles         | 10/1/2024   | 10/1/2024   | 1 day     |
    | SOW                      | 10/3/2024   | 10/4/2024   | 1 day     |
    | Critical Path Analysis   | 11/21/2024  | 11/26/2024  | 5 days    |
    | Software                 | 10/3/2024   | 10/7/2024   | 4 days    |
    | Cost estimates           | 11/21/2024  | 11/28/2024  | 7 days    |
    | **Design**               |             |             | **53 Days** |
    | Figma                    | 10/8/2024   | 10/10/2024  | 2 days    |
    | Critical Path Analysis   | 11/30/2024  | 11/30/2024  | 1 day     |
    | AOA                      | 11/19/2024  | 11/26/2024  | 7 days    |
    | **Implementation**       |             |             | **61 Days** |
    | Streamlit                | 10/3/2024   | 10/4/2024   | 1 day     |
    | Web pages                | 10/4/2024   | 12/3/2024   | 60 days   |
    | Gantt Chart              | 10/15/2024  | 10/17/2024  | 3 days    |
    """)


if __name__ == "__main__":
    display_wbs()
