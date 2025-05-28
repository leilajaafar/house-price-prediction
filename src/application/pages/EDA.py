import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Exploration des maisons", layout="wide")

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


st.markdown("""
    <style>
    .logo-img {
        border-radius: 15px;
        height: 100px;
        margin-right: 1.5rem;
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
    logo = Image.open("../assets/ESTILOGO.png")
    logo_base64 = image_to_base64(logo)
except Exception as e:
    logo_base64 = ""
    st.warning(f"Logo image not found or error loading image: {str(e)}")

st.markdown(f"""
<header>
    <img src="data:image/png;base64,{logo_base64}" class="logo-img">
    <h2 style="color: #AF9979; font-weight: bold;">Explorer les données sur les maisons</h2>
</header>
""", unsafe_allow_html=True)




@st.cache_data
def load_data():
    df = pd.read_csv("../used_data/EDA_set.csv", na_filter = False) 
    return df



df = load_data()


st.markdown("Bienvenue ! Ici, vous pouvez découvrir des informations intéressantes sur les maisons : leur prix, leur taille, les quartiers, et plus encore. 🔎")

# --- Section 1 : Prix ---
st.header("💰 Prix des maisons")
st.markdown("Voici comment les prix des maisons sont répartis dans notre base de données :")

fig_price = px.histogram(df, x="SalePrice", nbins=50, title="Distribution des prix des maisons", color_discrete_sequence=["#AF9979"])
fig_price.update_layout(xaxis_title="Prix", yaxis_title="Nombre de maisons")
st.plotly_chart(fig_price, use_container_width=True)

# --- Section 2 : Types de maisons ---
st.header("🏠 Types de maisons")
st.markdown("Quels sont les styles de maisons les plus fréquents ?")

style_counts = df["HouseStyle"].value_counts().reset_index()
style_counts.columns = ["Style", "Nombre"]

fig_style = px.bar(style_counts, x="Style", y="Nombre", color="Style", title="Types de maisons dans le dataset")
fig_style.update_layout(xaxis_title="Style de maison", yaxis_title="Nombre")
st.plotly_chart(fig_style, use_container_width=True)

# --- Section 3 : Quartiers ---
st.header("📍 Répartition par quartier")
st.markdown("Dans quels quartiers se trouvent le plus de maisons ?")

neigh_counts = df["Neighborhood"].value_counts().reset_index()
neigh_counts.columns = ["Quartier", "Nombre"]

fig_neigh = px.bar(neigh_counts, x="Quartier", y="Nombre", color="Quartier", title="Nombre de maisons par quartier")
fig_neigh.update_layout(xaxis_tickangle=-45, xaxis_title="Quartier", yaxis_title="Nombre")
st.plotly_chart(fig_neigh, use_container_width=True)

# --- Section 4 : Superficie vs Prix ---
st.header("📏 Taille vs Prix")
st.markdown("Y a-t-il une relation entre la surface habitable et le prix ?")

fig_scatter = px.scatter(df, x="GrLivArea", y="SalePrice", title="Surface habitable vs Prix", color="OverallQual",
                         labels={"GrLivArea": "Surface habitable (en pieds²)", "SalePrice": "Prix", "OverallQual": "Qualité globale"},
                         color_continuous_scale="viridis")
st.plotly_chart(fig_scatter, use_container_width=True)

# --- Section 5 : Filtrage interactif ---
st.header("🎛️ Explorer selon vos critères")
quartiers = df["Neighborhood"].unique()
choix_quartier = st.selectbox("Choisissez un quartier à explorer :", sorted(quartiers))

filtre = df[df["Neighborhood"] == choix_quartier]

fig_filtered = px.box(filtre, x="HouseStyle", y="SalePrice", color="HouseStyle",
                      title=f"Prix des maisons à {choix_quartier} selon le type",
                      labels={"SalePrice": "Prix", "HouseStyle": "Type de maison"})
st.plotly_chart(fig_filtered, use_container_width=True)

st.markdown("📊 Cette page vous permet de mieux comprendre les données utilisées pour prédire le prix des maisons. Vous pouvez passer à l’onglet Prédiction pour tester vous-même !")
