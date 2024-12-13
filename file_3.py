import streamlit as st
st.title("Marks Evaluation")
project = st.number_input("Enter the project marks: ", min_value=0, max_value=100, step=1)
internal = st.number_input("Enter the internal marks: ", min_value=0, max_value=100, step=1)
external = st.number_input("Enter the external marks: ", min_value=0, max_value=100, step=1)
if project >= 50 and internal >= 50 and external >= 50:
    total_marks = 100
    project_score = (project / total_marks) * 70
    internal_score = (internal / total_marks) * 10
    external_score = (external / total_marks) * 20
    total_score = project_score + internal_score + external_score
    st.write(f"Total Percentage: {total_score:.2f}%")
    if total_score >= 90:
        st.success("Grade: A")
    elif total_score >= 80:
        st.success("Grade: B")
    elif total_score >= 50:
        st.success("Grade: C")
    else:
        st.error("Failed in certain subject")
else:
    if project < 50:
        st.error(f"Failed in project => marks={project}")
    if internal < 50:
        st.error(f"Failed in internal => marks={internal}")
    if external < 50:
        st.error(f"Failed in external => marks={external}")