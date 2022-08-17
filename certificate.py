import cv2
import os
import base64
import streamlit as st
from st_click_detector import click_detector
from st_clickable_images import clickable_images
import numpy
import sys
from PIL import Image, ImageDraw

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
activities = ["Get certificate","About"]
st.sidebar.image("images\\logo.png")
choice=st.sidebar.selectbox("Select Activty",activities)


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"> Download {file_label}</a>'
    return href

def annotate(name):
    # using Clickable Images to Make Displaying Templates to be Responsive
    images = []
    for file in ["certificate_templates\\new_Certificate-template-1.png", "certificate_templates\\new_Certificate-template-2.png","certificate_templates\\Certificate-template-3.png"]:
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")

    clicked = clickable_images(
    images,
    titles=[f"Template #{str(i+1)}" for i in range(3)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
    )
    # clicked variable Stores the Id of the image clicked.

    # the path will be default to the defualt image
    path = "images\\img.png"

    # we cross check id with the paths available and assign the path for the selected image

    if(clicked == 0):
        path = "certificate_templates\\new_Certificate-template-1.png"
    if (clicked == 1):
        path = "certificate_templates\\new_Certificate-template-2.png"
    if (clicked == 2):
        path = "certificate_templates\\Certificate-template-3.png"

    
    certi = cv2.imread(path)

    if(clicked==2):
        original = cv2.putText(certi, name, (600, 850),font,   fontScale, (255, 255, 255), thickness=5)
    else:
        original = cv2.putText(certi, name, (600, 790),font,   fontScale, (0, 0, 0), thickness=5)
    cv2.imwrite("Certificate.jpg",original)

    
    if st.button("View certificate"):
        st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',output_format='PNG')
        st.markdown(get_binary_file_downloader_html('Certificate.jpg', 'Certificate'), unsafe_allow_html=True)


if choice =="Get certificate":
    st.title("Get Your Certificate")
    na=st.text_input('Enter your name')
    if len(na)>0:
        annotate(na)
    else:
        st.write("Please enter Your name in the Above Field To download the Certificate")    
    #st.markdown(get_binary_file_downloader_html(original, 'Picture'), unsafe_allow_html=True)


if choice =="About":
    st.subheader("Cerficate App")
    st.markdown("</> with ❤ by Anirudh Soni" )
    st.markdown("connect with me 😃 (https://www.linkedin.com/in/heyanirudh)")
