import streamlit as st
import easyocr
from googletrans import Translator
from gtts import gTTS
import pyttsx3
from PIL import Image
import cv2
import numpy as np

st.title("Hack for Africa - AI OCR")
st.subheader("Optical Character Recognition with Voice output")

st.text("Select source language from the sidebar")

image_file = st.file_uploader("Upload Image", ["JFIF", "PNG", "JPG"])

if st.button("Convert"):
    if image_file is not None:
        img = Image.open(image_file)
        img = np.array(img)
        
        st.subheader('Image you Uploaded...')
        st.image(image_file,width=450)
        
        if src=='English':
            with st.spinner('Extracting Text from given Image'):
                eng_reader = easyocr.Reader(['en'])
                detected_text = eng_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)
            

        elif src=='Swahili':
            with st.spinner('Extracting Text from given Image'):
                swahili_reader = easyocr.Reader(['sw'])
                detected_text = swahili_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)
              

        elif src=='Afrikaans':
            with st.spinner('Extracting Text from given Image'):
                afrikaans_reader = easyocr.Reader(['af'])
                detected_text = afrikaans_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)
            
        
        elif src=='Arabic':
            with st.spinner('Extracting Text from given Image...'):
                arabic_reader = easyocr.Reader(['ar'])
                detected_text = arabic_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)
        st.write('')
        ta_tts = gTTS(text,lang=f'{source}')
        ta_tts.save('trans.mp3')
        st.audio('trans.mp3',format='audio/mp3')
        

        with st.spinner('Translating Text...'):
            result = translator.translate(text, src=f'{source}', dest=f'{dst}').text
        st.subheader("Translated Text is ...")
        st.write(result) 

        st.write('')
        st.header('Generated Audio')
        
        with st.spinner('Generating Audio ...'):
            ta_tts2 = gTTS(result,lang=f'{dst}')
            ta_tts2.save('trans2.mp3')
        st.audio('trans2.mp3',format='audio/mp3')  
        st.balloons()  
               
            
    else:
        st.subheader('Image not found! Please Upload an Image.')

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