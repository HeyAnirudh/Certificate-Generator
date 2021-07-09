import cv2
import streamlit as st
import numpy
import sys
from PIL import Image, ImageDraw
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
#name=st.text_input('Enter your name')
#certi=cv2.imread("C:\\Users\\Admin\Desktop\\github\\certificates_streamlit\\pics\\certificate.jpg")
#original=cv2.putText(certi,name,(380, 300),font,fontScale,(0,0,0),thickness=2)

#cv2.imshow('fun',original)
#st.image(original,caption=None, width=350, use_column_width=None, clamp=False, channels='BGR', output_format='PNG')


def annotate(name):
    certi = cv2.imread("C:\\Users\\Admin\Desktop\\github\\certificates_streamlit\\pics\\certificate.jpg")
    original = cv2.putText(certi, name, (340, 300), font, fontScale, (0, 0, 0), thickness=2)
    cv2.imwrite("download.png",original)
    st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',
                 output_format='PNG')


na=st.text_input('Enter your name')
annotate(na)
