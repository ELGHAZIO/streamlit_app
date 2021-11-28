import streamlit as st

st.title("Hack for Africa - AI OCR")
st.subheader("Optical Character Recognition with Voice output")

st.text("Select source language from the sidebar")

image_file = st.file_uploader("Upload Image", ["JFIF", "PNG", "JPG"])

if st.button("Convert"):
    pass

st.sidebar.title("Select...")

from_language = st.sidebar.selectbox("From Language", ["English", "French"], key=1)

st.sidebar.write("")

st.sidebar.subheader("Select...")

to_language = st.sidebar.selectbox("To Language", ["English", "French"], key=2)

st.sidebar.write("")

st.sidebar.subheader("Enter Text...")
st.sidebar.text_input("Auto detection enabled")

if st.sidebar.button("Translated"):
    pass
