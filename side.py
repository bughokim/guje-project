import streamlit as st
import pandas as pd

from db_fxns import create_table, add_data

def main():
    st.title("ToDo App with Streamlit")

    menu = ["Creat", "Read", "Update", "Delete", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == 'Creat':
        st.subheader("Add Items")

        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Task To Do")

        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            add_data(task, task_status, task_due_date)
            st.success("Successfully Added Data:{}".format(task))

    elif choice == 'Read':
        st.subheader('View Items')

    elif choice == 'Update':
        st.subheader('Edit/Update Items')

    elif choice == 'Delete':
        st.subheader('Delete Items')

    else:
        st.subheader('About')



if __name__ == '__main__':
    main()