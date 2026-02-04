import streamlit as st
st.title("My age and city app")
age=st.slider("Enter your age", 0,100,step=1) 
city=st.selectbox("Select your city", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
if st.button("Show details"):
    st.write(f"You are {age} years old and live in {city}.")
    
