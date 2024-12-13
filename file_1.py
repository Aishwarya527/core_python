import streamlit as st
st.title("shopping bills")
sal=st.number_input("enter the salary",value=None)
st.write("The current number is ", sal)
bill1=st.number_input("enter the bill1",value=None)
st.write("The current number is ", bill1)
bill2=st.number_input("enter the bill2",value=None)
st.write("The current number is ", bill2)
bill3=st.number_input("enter the bill3",value=None)
st.write("The current number is ", bill3)
total = bill1 + bill2 + bill3
percentage = (total / sal) * 100
st.write(f"Total shopping amount: ${total}")
st.write(f"Percentage of salary spent on shopping: {percentage:.2f}%")