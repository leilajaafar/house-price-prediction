# Accueil.py - Version sécurisée
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import sys
from pathlib import Path

# --- Configuration de la page (DOIT être la première commande) ---
st.set_page_config(
    page_title="🏡 Prédicteur de Prix Immobilier",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialisation sécurisée de la session ---
if 'authenticated' not in st.session_state:
    st.session_state.update({
        'authenticated': False,
        'user': {'username': ''}  # Structure minimale garantie
    })

# --- Fonctions utilitaires ---
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- CSS Personnalisé ---
st.markdown("""
    <style>
    body, .main, .stApp {
    
        background-color: #f8fafc !important;
        color: #333 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
body, .main {
    background-color: #f8fafc;
    font-family: 'Segoe UI', sans-serif;
    color: #333;
}
.logo-img {
        border-radius: 15px;
        height: 100px;
        margin-right: 1.5rem;
}

/* Réduction du gap supérieur */
.centered-text {
    text-align: center;
    margin-top: 1rem;
    font-size: 1.2rem;
    color: #555;
}

/* Conteneur principal */
.block {
    background-color: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.03);
    max-width: 900px;
    margin: 1rem auto; /* réduit l'espace vertical */
}

/* Style pour les balises code */
code {
    background-color: #e2e8f0; /* gris clair */
    color: #1e3a8a; /* bleu foncé élégant */
    padding: 3px 6px;
    border-radius: 6px;
    font-size: 0.95rem;
}

/* En-tête */
    header {
        background-color: #F0F1F5;
        border-radius: 15px;
        display: flex;
        align-items: center;
        padding: 1rem 2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    header h2 {
        font-size: 1.8rem;
        font-weight: bold;
        color: #D1BB9B;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Gestion de l'authentification ---
if not st.session_state.get('authenticated', False):
    try:
        logo = Image.open("assets/ESTILOGO.png")
        logo_base64 = image_to_base64(logo)
        st.markdown(f"""
        <header>
            <img src="data:image/png;base64,{logo_base64}" class="logo-img">
            <h2 style="color: #AF9979; font-weight: bold;">Connexion à Estimaison</h2>
        </header>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Logo non trouvé : {str(e)}")
    
    from pages.Se_connecter import show_login_form
    show_login_form()
    st.stop()

# --- Contenu après authentification (version sécurisée) ---
try:
    username = st.session_state.get('user', {}).get('username', 'Invité')
    st.markdown(f"""
    <header>
        <img src="data:image/png;base64,{image_to_base64(Image.open("assets/ESTILOGO.png"))}" class="logo-img">
        <h2 style="color: #AF9979; font-weight: bold;">Bienvenue {username}</h2>
    </header>
    """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Erreur de chargement : {str(e)}")
    st.stop()

# Sidebar sécurisée
with st.sidebar:
    username = st.session_state.get('user', {}).get('username', 'Invité')
    st.write(f"Connecté en tant que : **{username}**")
    
    if st.button("Déconnexion"):
        st.session_state.update({
            'authenticated': False,
            'user': {'username': ''}
        })
        st.rerun()


st.markdown("""
<div class="centered-text">
    <h2 style="font-size: 2.2rem; color: #1f2937;"> Bienvenue sur Estimaison : votre assistant intelligent de l'immobilier</h2>
    <p style="font-size: 1.1rem; color: #4b5563; max-width: 720px; margin: auto;">
        Cette application utilise l’apprentissage automatique pour estimer la valeur d’un bien immobilier résidentiel.
        Elle s’appuie sur un jeu de données riche issu de ventes à Ames (Iowa), intégrant plus de 70 caractéristiques 
        comme la surface habitable, la qualité de la cuisine, le quartier, le type de garage ou encore l’année de construction.
    </p>
</div>
""", unsafe_allow_html=True)


with st.container():
    st.markdown('<h2 style="color:#1f2937">🔍 Fonctionnalités disponibles</h2>', unsafe_allow_html=True)
    st.markdown("""
- 🗂️ **Analyse exploratoire (EDA)** : 
  Visualisez et filtrez les données selon différents critères tels que le quartier ou la taille des maisons.

- 🧠 **Prédiction intelligente** : 
  Grâce à un modèle entraîné sur des données normalisées, obtenez une **estimation en temps réel** du prix 
  de votre bien.

- 📚 **Compréhension des données** :
  Un accès transparent à la signification de chaque variable pour mieux comprendre la valeur de chaque logement.

- 🌐 **Expérience fluide & interactive** : 
  Interface claire, boutons personnalisés, structure responsive.

---
🟢 **Commencez dès maintenant** en sélectionnant un onglet dans le menu de gauche.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

