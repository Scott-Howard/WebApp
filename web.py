import streamlit as st #new library for building web apps
import functions as fn

todos = fn.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My To do app")
st.subheader("This is my very basic todo app")
st.write("This is to improve your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.session_state["new_todo"] = ""
        st.experimental_rerun()

st.text_input(label="",placeholder="enter a new todo....",
             on_change=add_todo, key ='new_todo', label_visibility="hidden")