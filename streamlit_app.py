import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Wild Fire')
st.subheader('Wild Fire in North-Easthern of Thailand')
from PIL import Image
image = Image.open('picc.png')
st.image(image,width=800)
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

    option = st.selectbox(
        "เลือกจังหวัด",
        ("นครราชสีมา", "บุรีรัมย์", "สุรินทร์","ชัยภูมิ", "ศรีษะเกศ", "ขอนแก่น","อุดรธานี", "เลย", "หนองบัวลำภู", "มหาสารคาม","ร้อยเอ็ด", "หนองคาย", "บึงกาฬ", "สกลนคร","นครพนม", "กาฬสินธุ์", "มุกดาหาร", "ยโสธร","อำนาจเจริญ", "อุบลราชธานี"),
        )

