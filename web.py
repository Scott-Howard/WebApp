import streamlit as st #new library for building web apps
import functions as fn

todos = fn.get_todos()

st.title("My Todo app")
st.subheader("this is a subheader")
st.write("This is to improve your productivity")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="",placeholder="enter a new todo....")
