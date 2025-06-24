import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(
    page_title="À propos",
    page_icon="ℹ️",
    layout="wide"
)


def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


st.markdown("""
    <style>
    .section {
        background-color: #F0F1F5;
        border-radius: 15px;
        padding: 2.5rem 3rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
        max-width: 1000px;
        margin: 3rem auto;
        color: #1f2937;
        font-family: 'Segoe UI', sans-serif;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    .logo-img {
        border-radius: 15px;
        height: 100px;
        margin-right: 1.5rem;
    }
    .section h3 {
        color: #0f172a;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .section ul {
        padding-left: 1.5rem;
        margin-top: 0.5rem;
    }
    .section li {
        margin-bottom: 0.5rem;
    }
    .section strong {
        color: #111827;
    }
    ul {
        margin-left: 1.2rem;
        padding-left: 0.5rem;
    }
    
    li {
        margin-bottom: 0.5rem;
    }
    .section hr {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 2rem 0;
    }
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
try:
    #logo = Image.open("assets/ESTILOGO.png")
    logo = Image.open("../assets/ESTILOGO.png")
    logo_base64 = image_to_base64(logo)
except Exception as e:
    logo_base64 = ""
    st.warning(f"Logo image not found or error loading image: {str(e)}")


st.markdown(f"""
<header>
    <img src="data:image/png;base64,{logo_base64}" class="logo-img">
    <h2 style="color: #AF9979; font-weight: bold;">À propos du projet Estimaison</h2>
</header>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">

<h3>🏡 Présentation</h3>

<strong>Estimaison</strong> est une application intelligente permettant d’estimer le prix de biens immobiliers résidentiels, à partir d’un jeu de données réel issu de la ville d’Ames (Iowa, USA).  
Ce projet combine la <strong>data science</strong>, l’<strong>analyse exploratoire</strong>, la <strong>modélisation prédictive</strong> et une <strong>interface utilisateur interactive</strong>.

<hr/>

<h3>🧠 Méthodologie</h3>

Le pipeline de développement inclut :
<ul>
    <li>Une analyse exploratoire détaillée (EDA) pour comprendre les variables influentes</li>
    <li>L’application de techniques de réduction de dimensionnalité (PCA)</li>
    <li>Des essais de plusieurs modèles de régression (linéaire, Lasso, Ridge, etc.)</li>
    <li>Une expérimentation approfondie avec <strong>PyCaret</strong>, une bibliothèque AutoML puissante</li>
    <li>L’évaluation fine des performances via la validation croisée</li>
</ul>

<hr/>

<h3>🔧 Technologies utilisées</h3>

Python, Streamlit, Pandas, Seaborn, Matplotlib, scikit-learn, PyCaret, PCA, Jupyter

<hr/>

<h3>👩‍💻 Réalisé par</h3>

<ul>
    <li><strong>Chahd HATTAB</strong></li>
    <li><strong>Leila JAAFAR</strong></li>
    <li><strong>Rihab RHARRABI</strong></li>
    <li><strong>Roufayda MAGOURI</strong></li>
</ul>

<hr/>

<h3>🎓 Contexte</h3>

Ce projet a été réalisé dans le cadre d’un travail universitaire visant à appliquer concrètement les notions d’apprentissage automatique à un cas pratique du domaine immobilier, tout en développant une application web fonctionnelle et esthétique.

</div>
""", unsafe_allow_html=True)
