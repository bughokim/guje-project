from matplotlib import animation
import streamlit as st
import requests
from streamlit_lottie import st_lottie 
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

animation_symbol = "⁕"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True
)


lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_JenNba.json")
img_contact_form = Image.open("image/aaa.jpg")
img_lottie_animation = Image.open("image/qqq.jpg")

with st.container():
    st.subheader("Hi I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write("I am passionate about finding ways to use Python and VBA ")
    st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube
            - are looking
            - are struggling
            - want to learn
            - are working with

            If this sounds interesting to you,
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="leature")

with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_contact_form)

        with text_column:
            st.subheader("Integrate Lottie ")
            st.write(
                    """
                    Learn how to
                    Animation
                    In
                    """
            )
            st.markdown("[Watch Video ...](https://youtube/TXSOitGoINE)")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.write(
                """
                Want to add
                In this video
                """
            )
            st.markdown("[Watch Video...](https://youtube/FOULV9Xij_8)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/jichan14@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


