import streamlit as st


def main():

    st.title("Simple Login App")

    menu = ["Home", "Login", "Singup"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Signup":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Singup"):
            st.success("You have  successfully created an valid Account")
            st.info("Go to Login Menu to login")

    else:
        st.subheader("login Setion")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            if password == '12345':
                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task",["Add Post", "Analytics", "Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")

                elif task == "Profiles":
                    st.subheader("User Profiles")
            else:
                st.warning("Incorrect Username/Password")






    


if __name__ == '__main__':
    main()