import streamlit as st
import piexif
from PIL import Image


st.title("Mon application Streamlit")
st.markdown("Ici vous pouvez voir nos images(la mienne et celle de la mnemosyne")

st.image('mnemosyne.jpeg',caption="La mnemosyne")
st.image('am.jpg',caption="Ma photo")
st.markdown("Les champs de texte pour la modification des informations Exif")
marque = st.text_input('Changer la marque ')
dated_de_capture = st.text_input('La date capture')