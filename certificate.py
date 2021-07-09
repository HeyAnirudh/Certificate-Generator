import cv2
from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import cv2 as cv
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1

image = Image.open("/pics/certificate.jpg")
img=cv.imread('C:\\Users\\Admin\Desktop\\github\\certificates_streamlit\\pics\\apricus.png')
st.image(img,caption=None, width=350, use_column_width=None, clamp=False, channels='BGR', output_format='PNG')
st.title("Get your certificates")
name=st.text_input('Enter your name')
#original=cv2.putText(certi,name,(50, 50),font,fontScale,(0,0,0),thickness=2)
#roll=cv.imshow("sample.jpg",original)
#st.image(original,caption=None, width=350, use_column_width=None, clamp=False, channels='BGR', output_format='PNG')



def annotate(image,name):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20, encoding="unic")
    original = draw.text((10, 10), text=u'{}'.format(name), font=font)
    st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR', output_format='PNG')
    return image

st.image(annotate(image,name),caption=None, width=350, use_column_width=None, clamp=False, channels='BGR', output_format='PNG')



