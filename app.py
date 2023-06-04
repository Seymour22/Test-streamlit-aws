import streamlit as st

def sum_numbers(a, b):
    return a + b

st.title("Number Summation")
number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")

result = sum_numbers(number1, number2)
st.write("The sum is:", result)
