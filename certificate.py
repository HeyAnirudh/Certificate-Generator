import cv2
import os
import base64
import streamlit as st
from st_click_detector import click_detector
import numpy
import sys
from PIL import Image, ImageDraw
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
activities = ["Get certificate","About"]
st.sidebar.image("images\\logo.png")
choice=st.sidebar.selectbox("Select Activty",activities)


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def annotate(name):
    # this line of code is used to display the Images on the site which are clickable
    st.write("Select Below Templates")
    content = """
                    <a id="Image_1" href="#"><img src="https://i.ibb.co/5WvJgFQ/new-Certificate-template-1.png" alt="new-Certificate-template-1" border="0" width="300px" aspect-ratio="16:9" ></a>

                    <a id="Image_2" href="#"><img src="https://i.ibb.co/CmhrK9d/new-Certificate-template-2.png" alt="new-Certificate-template-2" border="0" width="300px" aspect-ratio="16:9" ></a>
            """
    # we store the Id of the clicked image in Clicked Variable 
    clicked = click_detector(content)
    # st.markdown(f"**{clicked} clicked**" )

    # the path will be default to the defualt image
    path = "images\\img.png"

    # we cross check id with the paths available and assign the path for the selected image

    if(clicked == "Image_1"):
        path = "certificate_templates\\new_Certificate-template-1.png"
    if (clicked == "Image_2"):
        path = "certificate_templates\\new_Certificate-template-2.png"

    
    certi = cv2.imread(path)
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
