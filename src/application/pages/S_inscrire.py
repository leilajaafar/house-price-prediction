# pages/S_inscrire.py
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
from db.database import create_connection, create_user

# Configuration de la page (doit être la première commande)
st.set_page_config(
    page_title="Inscription - Estimaison",
    page_icon="✍️",
    layout="wide"
)

# --- Fonctions utilitaires ---
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- CSS Personnalisé ---
st.markdown("""
<style>
    .register-container {
        max-width: 700px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    .header {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    }
    .logo {
        height: 80px;
        margin-right: 1.5rem;
        border-radius: 12px;
    }
    .title {
        color: #AF9979;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 8px !important;
        padding: 10px !important;
    }
    .stButton>button {
        background-color: #AF9979 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        width: 100%;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #6B7280;
    }
</style>
""", unsafe_allow_html=True)

# --- Header avec logo ---
try:
    logo = Image.open("assets/ESTILOGO.png")
    logo_base64 = image_to_base64(logo)
    header_html = f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
        <div>
            <h1 class="title">Créer un compte</h1>
            <p style="color: #6B7280;">Rejoignez notre plateforme d'estimation immobilière</p>
        </div>
    </div>
    """
except:
    header_html = """<h1 class="title">Créer un compte</h1>"""

# --- Formulaire d'inscription ---
def main():
    st.markdown(header_html, unsafe_allow_html=True)
    
    with st.container():
        with st.form("register_form"):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("Prénom*")
            with col2:
                last_name = st.text_input("Nom*")
            
            email = st.text_input("Email*")
            username = st.text_input("Nom d'utilisateur*")
            password = st.text_input("Mot de passe*", type="password")
            password_confirm = st.text_input("Confirmer le mot de passe*", type="password")
            
            submitted = st.form_submit_button("S'inscrire", use_container_width=True)
            
            if submitted:
                if password != password_confirm:
                    st.error("Les mots de passe ne correspondent pas")
                elif not all([first_name, last_name, email, username, password]):
                    st.error("Veuillez remplir tous les champs obligatoires (*)")
                else:
                    connection = create_connection()
                    if connection:
                        if create_user(connection, username, password, email, f"{first_name} {last_name}"):
                            st.success("Inscription réussie! Redirection...")
                            st.session_state['authenticated'] = True
                            st.switch_page("./Accueil.py")
                        else:
                            st.error("Ce nom d'utilisateur existe déjà")
                        connection.close()
        
        st.markdown("""
        <div class="footer">
            Déjà un compte? <a href="/Se_connecter" style="color: #AF9979; text-decoration: none;">Se connecter</a>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()