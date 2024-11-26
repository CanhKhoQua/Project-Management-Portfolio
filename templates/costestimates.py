import streamlit as st

def display_cost_estimate():
    # Add a title for the cost estimate section
    st.title("Project Cost Estimate")
    
    # Display a summary of the cost estimation
    st.subheader("Summary")
    st.markdown("""
    To estimate the cost of office space we used the cost of the course at $566 per person, which we considered to be the office space expense for our group. This cost reflects our team's ability to meet in person and collaborate with each other face to face. The space also included access to the internet. Using this we used the classroom as an office space we budgeted this in as our office space. 

    All members of our group in any certain way used AI to help them along the way on this project and although we used free ChatGPT and Co-pilot which is paid for by the school we went ahead and added the cost of what this would have been if we weren't students. With 8 team members co-pilot came out to a total of \$240 dollars and ChatGPT was \$200 dollars total or \$25 per person for ChatGPT and \$30 per person for Co-pilot. 

    Although the classroom included machines for us to use, we could only access these in the allotted class times which would not work if we were to finish this project on time. To add to our budget, we took the average cost of our personal machines between the 8 of us and averaged it out to \$750 per person bringing the total we would have spent in machines to \$2750 

    While we did not pay for everything that was listed such as the AI, we felt this was the most accurate way to create a budget that truly represents the project that we worked on and covered the true cost of the things we created and the spaces that we occupied. In the end our final budget came out to \$7,718 total.  

    In addition to the tools and resources previously mentioned we utilized Streamlit to support our project. Streamlit is free to use, it didn't add any cost to our budget making it the ideal choice for this project. It served the purpose that we needed it without incurring additional cost.  
    """)

    # Cost estimate table
    st.subheader("Cost Breakdown")
    cost_data = [
        {"Category": "Software/Technology", "Item": "ChatGPT Subscription", "Cost Per Person": "$20.00", "Number of People": 8, "Total Cost": "$160.00"},
        {"Category": "Software/Technology", "Item": "CoPilot Subscription", "Cost Per Person": "$25.00", "Number of People": 8, "Total Cost": "$240.00"},
        {"Category": "Hardware", "Item": "Personal Machines", "Cost Per Person": "$750.00", "Number of People": 8, "Total Cost": "$6,000.00"},
        {"Category": "Office Space", "Item": "Shared Office Rental", "Cost Per Person": "$566.00", "Number of People": 8, "Total Cost": "$4,528.00"},
        {"Category": "Design", "Item": "Streamlit", "Cost Per Person": "$0.00", "Number of People": 8, "Total Cost": "$0.00"}
    ]
    
    # Create a table for the cost breakdown
    st.table(cost_data)
    
    # Add a total budget summary
    st.subheader("Total Budget")
    st.write("The total estimated cost for the project is **$7,718.00**.")

if __name__ == "__main__":
    display_cost_estimate()