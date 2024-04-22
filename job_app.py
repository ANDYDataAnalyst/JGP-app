import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("Welcome to Jovian Global Partners")
st.subheader("Careers in JGP")
st.write("We offer services such as Consulting, IT, Agriculture, Energy, Banking & Investment")

st.subheader("PERSONAL DETAILS")
st.text_input("FIRST NAME")
st.text_input("LAST NAME")
st.text_input("E-mail Address")
st.selectbox("Gender", ["Male", "Female", "Others"])
st.selectbox("Area of Interest", ["Agriculture", "Banking & Investment", "Consulting","Energy","IT"])
st.date_input("Date of Birth")
st.text_input("State of Residence")
st.number_input("Mobile Number", 0, 11)
st.sidebar.header("Curriculum Vitae")
st.sidebar.subheader("Attach CV")
st.sidebar.file_uploader("Upload a file", type=["png","jpg", "pdf"])

st.sidebar.header("How do you hear about this Opening")
st.sidebar.radio("Source", ["LinkedIN", "Company's Website", "Twitter", "Facebook", "Referral"])

st.header("EDUCATIONAL QUALIFICATIONS")
st.write("Please enter only qualifications obtained from Tertiary Institutions")
Tab1 = pd.DataFrame({"University":[],
                     "Course_of_study": [],
                     "Level": [],
                     "Grade": [],
                     "Year":  [],
})
st.table(Tab1)
st.write("Add row")
st.header("EMPLOYMENT HISTORY")
Tab2 = pd.DataFrame({"Employer Name": [],
                     "Position Held": [],
                     "Responsibilities": [],
                     "Achievements": [],
                     "From": [],
                     "To": [],
})
st.table(Tab2)

st.sidebar.checkbox("Submit Application")
st.sidebar.checkbox("Cancel")



