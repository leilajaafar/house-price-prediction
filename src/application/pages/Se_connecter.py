# pages/Se_connecter.py
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
from db.database import create_connection, verify_user

# SUPPRIMEZ st.set_page_config() - Il doit seulement être dans Accueil.py

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Style harmonisé avec Accueil.py
st.markdown("""
<style>
    .main {
        background-color: white !important;
    }
    .login-container {
        max-width: 500px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    .header {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    }
    .logo-img {
        height: 80px;
        border-radius: 12px;
        margin-right: 1.5rem;
    }
    /* 🎯 Champ texte personnalisé */
    .stTextInput label {
        color: #1f2937 !important; /* Texte couleur beige doré */
        font-weight: 500;
    }
    

    .stTextInput>div>div>input {
        color: #e1e2e3;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    
        div[data-testid="baseButton-primary"] button {
        background-color: #AF9979 !important;
        color: white !important;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        border: none;
    }
    div[data-testid="stNotification"] {
        background-color: #FFF5F5;
        border-left: 4px solid #AF9979;
        border-radius: 0 8px 8px 0;
    }
    div[data-testid="stNotification"] > div > div {
        color: #7A5C3C !important;
        font-family: 'Segoe UI', sans-serif;
        font-size: 14px;
    }
    div[data-testid="stNotification"] > div > div > svg {
        color: #AF9979 !important;
    }
    
</style>
""", unsafe_allow_html=True)

def show_login_form():
    """Affiche le formulaire de connexion avec style"""
    
    # Formulaire dans un conteneur stylisé
    with st.form("login_form"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        
        submitted = st.form_submit_button("Se connecter")
        
        if submitted:
            connection = create_connection()
            if connection:
                user = verify_user(connection, username, password)
                if user:
                    st.session_state['authenticated'] = True
                    st.session_state['user'] = user
                    st.success("Connexion réussie!")
                    st.rerun()
                else:
                    st.error("Nom d'utilisateur ou mot de passe incorrects")
                connection.close()
            else:
                st.error("Erreur de connexion à la base de données")
    
    # Lien vers inscription
    st.markdown("""
    <div class="footer">
        Pas encore de compte? <a href="/S_inscrire" target="_self" style="color: #AF9979;">S'inscrire</a>
    </div>
    """, unsafe_allow_html=True)