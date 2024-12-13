import streamlit as st
st.title("Gross Salary Calculator")
basic_salary = st.number_input("Enter your basic salary: ",min_value=0,step=1)
if st.button("Calculate Gross salary"):
    hra=0
    da=0
if basic_salary < 10000:
    hra = 0.67 * basic_salary
    da = 0.73 * basic_salary
elif 10000 <= basic_salary <= 20000:
    hra = 0.69 * basic_salary
    da = 0.76 * basic_salary
else:
    hra = 0.73 * basic_salary
    da = 0.89 * basic_salary
gross_salary = basic_salary + hra + da
st.write(f"Gross Salary: {gross_salary:.2f}")
