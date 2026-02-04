import streamlit as st 
st.title("Calculator App")
num1=st.number_input("Enter first number: ")
num2=st.number_input("Enter second number: ")
operation=st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
if st.button("Calculate"):
    if operation=="Add":
        result=st.write(num1 + num2)
    elif operation=="Subtract":
        result=st.write(num1 - num2)  
    elif operation=="Multiply":
        result=st.write(num1 * num2)
    elif operation=="Divide":
        if num2 != 0:
            result=st.write(num1 / num2)
        else:
            st.write("Error: Division by zero is not allowed.")
    