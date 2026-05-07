import streamlit as st
from textblob import TextBlob
import pandas as pd
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# Configuración de página con vibra linda
st.set_page_config(page_title="Sentimientos Coquette", page_icon="💖")

# --- ESTILO CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5; /* Lavender Blush */
    }
    h1 {
        color: #FF69B4 !important; /* Hot Pink */
        font-family: 'Brush Script MT', cursive;
        text-align: center;
        font-size: 50px !important;
        text-shadow: 2px 2px #FFB6C1;
    }
    h3 {
        color: #DB7093 !important; /* Pale Violet Red */
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 2px solid #FFB6C1 !important;
    }
    .stExpander {
        border: 2px solid #FFB6C1 !important;
        border-radius: 15px;
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('💖 Sentiment Diary ✨')

# Imagen principal (asegúrate de tener el archivo o usa una URL)
try:
    image = Image.open('feelings.jpg')
    st.image(image, use_column_width=True)
except:
    st.write("✨ *Insertar imagen divina aquí* ✨")

st.subheader("🌸 Cuéntame cómo te sientes hoy, linda...")

translator = Translator()

# Sidebar con estilo
with st.sidebar:
    st.markdown("<h2 style='color: #FF69B4;'>🎀 Diccionario Estilo</h2>", unsafe_allow_html=True)
    st.info("""
        **Polaridad:** Nos dice si tu frase es un rayito de sol (Positivo), una nube gris (Negativo) o un día tranquilo (Neutral).
        
        **Subjetividad:** Mide qué tanto pusiste de tu corazoncito (emociones) frente a datos fríos (hechos).
    """)
    st.write("---")
    st.write("Hecho con ✨ por una Girl in Tech")

# Expander para el análisis
with st.expander('✨ Analizar mi Vibe'):
    text = st.text_input('Escribe algo aquí, reina: ')
    
    if text:
        # Traducción
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        
        # Resultados con diseño
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="🧸 Polarity", value=round(blob.sentiment.polarity, 2))
        with col2:
            st.metric(label="☁️ Subjectivity", value=round(blob.sentiment.subjectivity, 2))

        x = round(blob.sentiment.polarity, 2)
        
        st.write("---")
        
        # Lógica de sentimientos con animaciones y mensajes lindos
        if x > 0.0:
            st.balloons()
            st.success('¡Qué lindo! Es un sentimiento **Positivo** 🎀✨')
            try:
                with open("Cute Doggie.json") as source:
                    animation = json.load(source)
                st_lottie(animation, width=350)
            except: st.write("🐶💖")
            
        elif x < 0:
            st.error('Oh no, nena... Es un sentimiento **Negativo** 😔💔')
            try:
                with open("Sad Emoji.json") as source:
                    animation = json.load(source)
                st_lottie(animation, width=350)
            except: st.write("😔🥀")
            
        else:
            st.warning('Es un sentimiento **Neutral** 😐☁️')
            try:
                with open("Bad Cat.json") as source:
                    animation = json.load(source)
                st_lottie(animation, width=350)
            except: st.write("😐🐾")

st.markdown("<br><center>🍓 Manéjalo con estilo 🍓</center>", unsafe_allow_html=True)
