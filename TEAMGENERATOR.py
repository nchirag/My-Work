import streamlit as st
import pandas as pd
import random
import base64
from io import BytesIO

def group_students(df, team_size):
    # Shuffle the students randomly
    shuffled_students = df.sample(frac=1).reset_index(drop=True)

    # Group students based on the selected team size
    grouped_students = [shuffled_students.iloc[i:i + team_size] for i in range(0, len(shuffled_students), team_size)]
    return grouped_students

# Set page title and bold text
st.set_page_config(page_title="Team Generator")
st.title("**Team Generator**")

# Sidebar for uploading Excel file and selecting team size
uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx", "xls"])
team_size = st.sidebar.selectbox("Select Team Size:", [2, 3, 4, 5])

if uploaded_file is not None:
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file)

    # Button to group students
    if st.sidebar.button("Group Students"):
        grouped_students = group_students(df, team_size)

        # Display the grouped teams
        st.write("### Grouped Teams:")
        for i, team in enumerate(grouped_students):
            st.write(f"**Team {i + 1}:**")
            st.table(team)

        # Add a button to download the grouped teams as Excel
        if st.button("Download Grouped Teams as Excel"):
            grouped_teams_df = pd.concat(grouped_students, ignore_index=True)

            # Save the Excel file using openpyxl
            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                grouped_teams_df.to_excel(writer, sheet_name='Sheet1', index=False)
                writer.save()

            # Encode the Excel file to base64
            excel_b64 = base64.b64encode(excel_buffer.getvalue()).decode()

            # Provide a download link to the user
            st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{excel_b64}" download="grouped_teams.xlsx">Download Grouped Teams</a>', unsafe_allow_html=True)

    # Display the original student list
    st.write("### Original Student List:")
    st.table(df)
else:
    st.warning("Please upload an Excel file.")
