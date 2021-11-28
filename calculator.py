import streamlit as st
from time import sleep

st.title("My Calculator")

first_number=st.text_input("Enter first number", "0")
second_number=st.text_input("Enter second number", "5")

operation = st.selectbox("Select Operation:", ["Addition", "Subtraction"])

if st.button("Perform Operation"):
    with st.spinner("PLease wait for 2 secs..."):
        sleep(2)
    if operation == "Addition":
        result = int(first_number) + int(second_number)
        st.success(f"Your result is {result}")

    elif operation == "Subtraction":
        result = int(first_number) - int(second_number)
        st.success(f"Your result is {result}")
