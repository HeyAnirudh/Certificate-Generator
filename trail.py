import cv2
import streamlit as st
import numpy
import sys
from PIL import Image, ImageDraw
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
activities = ["Get certificate","About"]
choice=st.sidebar.selectbox("Select Activty",activities)


def annotate(name):
    certi = cv2.imread("C:\\Users\\Admin\Desktop\\github\\certificates_streamlit\\pics\\certificate.jpg")
    original = cv2.putText(certi, name, (380, 300), font, fontScale, (0, 0, 0), thickness=2)
    cv2.imwrite("download.png", original)
    st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR', output_format='PNG')

if choice =="Get certificate":
    img=cv2.imread('C:\\Users\\Admin\Desktop\\github\\certificates_streamlit\\pics\\apricus.png')
    na=st.text_input('Enter your name')
    annotate(na)


if choice =="About":
    st.subheader("Cerficate App")
    st.markdown("</> with ❤ by Apricus" )
    st.markdown("follow us on instagram 😃 (https://instagram.com/apricus_vjit?utm_medium=copy_link)")

