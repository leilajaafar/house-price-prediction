import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from io import BytesIO



st.set_page_config(page_title="Analyse Immobilière", layout="wide")


def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

st.markdown("""
    <style>
    .logo-img { border-radius: 15px; height: 90px; margin-right: 1.5rem; }
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
        color: #AF9979;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

try:
    logo = Image.open("./assets/ESTILOGO.png")
    logo_base64 = image_to_base64(logo)
except:
    logo_base64 = ""

st.markdown(f"""
<header>
    <img src="data:image/png;base64,{logo_base64}" class="logo-img">
    <h2 style="color: #AF9979; font-weight: bold;">Analyse des Maisons - Pour acheteurs, agents & investisseurs</h2>
</header>
""", unsafe_allow_html=True)

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("./used_data/EDA_set.csv")
    return df

df = load_data()

st.markdown("🔎 **Cette page vous permet de mieux comprendre les caractéristiques des maisons proposées** : leur prix, leur emplacement, leur taille et bien plus.")

# ----------- GRAPHE 1 : Prix moyen par quartier ------------
st.subheader("📍 Prix moyen par quartier")
st.markdown("Découvrez où se situent les maisons les plus chères ou les plus accessibles.")

quartier_price = df.groupby("Neighborhood")["SalePrice"].mean().reset_index().sort_values(by="SalePrice", ascending=False)

fig_qp = px.bar(quartier_price, x="Neighborhood", y="SalePrice", color="SalePrice",
                title="Prix moyen des maisons par quartier",
                color_continuous_scale="sunsetdark")
fig_qp.update_layout(xaxis_title="Quartier", yaxis_title="Prix moyen ($)", xaxis_tickangle=-45)
st.plotly_chart(fig_qp, use_container_width=True)

# ----------- GRAPHE 2 : Superficie moyenne par type de maison ------------
st.subheader("🏠 Taille moyenne selon le style de maison")
surface_by_type = df.groupby("HouseStyle")["GrLivArea"].mean().reset_index().sort_values(by="GrLivArea", ascending=False)

fig_size = px.bar(surface_by_type, x="HouseStyle", y="GrLivArea", color="GrLivArea",
                  title="Surface habitable moyenne selon le type de maison",
                  color_continuous_scale="tealgrn")
fig_size.update_layout(xaxis_title="Type de maison", yaxis_title="Surface (pieds²)")
st.plotly_chart(fig_size, use_container_width=True)

# ----------- GRAPHE 3 : Prix en fonction de la qualité ------------
st.subheader("💎 La qualité des maisons influe-t-elle sur le prix ?")

fig_quality = px.box(df, x="OverallQual", y="SalePrice", color="OverallQual",
                     title="Prix des maisons selon leur qualité globale (1 = très faible, 10 = excellente)",
                     color_discrete_sequence=px.colors.qualitative.Vivid)
fig_quality.update_layout(xaxis_title="Qualité", yaxis_title="Prix ($)")
st.plotly_chart(fig_quality, use_container_width=True)

# ----------- GRAPHE 4 : les facteurs qui influencent le prix ------------

st.subheader("🧭 Ce qui influence le prix d’une maison")

st.markdown("""
Sélectionnez un critère pour visualiser comment il affecte le prix moyen des maisons.
Cela peut vous aider à identifier des tendances intéressantes pour acheter ou investir 💡
""")

choix = st.selectbox(
    "📌 Choisissez un critère à explorer :",
    [
        "Nombre de chambres",
        "Qualité globale",
        "Surface habitable",
        "Style de maison"
    ]
)

if choix == "Nombre de chambres":
    chambre_stats = df.groupby("BedroomAbvGr")["SalePrice"].mean().reset_index()
    fig = px.bar(
        chambre_stats, x="BedroomAbvGr", y="SalePrice",
        labels={"BedroomAbvGr": "Nombre de chambres", "SalePrice": "Prix moyen ($)"},
        title="💰 Prix moyen selon le nombre de chambres",
        color="SalePrice", color_continuous_scale="sunset",
        template="plotly_dark"
    )

elif choix == "Qualité globale":
    qual_stats = df.groupby("OverallQual")["SalePrice"].mean().reset_index()
    fig = px.bar(
        qual_stats, x="OverallQual", y="SalePrice",
        labels={"OverallQual": "Qualité (1=faible, 10=excellente)", "SalePrice": "Prix moyen ($)"},
        title="💰 Prix moyen selon la qualité de la maison",
        color="SalePrice", color_continuous_scale="viridis",
        template="plotly_dark"
    )

elif choix == "Surface habitable":
    df["SurfaceGroup"] = pd.cut(df["GrLivArea"], bins=[0, 1000, 1500, 2000, 2500, 4000],
                                labels=["Petite", "Moyenne", "Grande", "Très grande", "Luxueuse"])
    surf_stats = df.groupby("SurfaceGroup")["SalePrice"].mean().reset_index()
    fig = px.bar(
        surf_stats, x="SurfaceGroup", y="SalePrice",
        labels={"SurfaceGroup": "Taille de la maison", "SalePrice": "Prix moyen ($)"},
        title="💰 Prix moyen selon la taille de la maison",
        color="SalePrice", color_continuous_scale="tealgrn",
        template="plotly_dark"
    )

elif choix == "Style de maison":
    style_stats = df.groupby("HouseStyle")["SalePrice"].mean().reset_index().sort_values(by="SalePrice", ascending=False)
    fig = px.bar(
        style_stats, x="HouseStyle", y="SalePrice",
        labels={"HouseStyle": "Type de maison", "SalePrice": "Prix moyen ($)"},
        title="💰 Prix moyen selon le style de maison",
        color="SalePrice", color_continuous_scale="peach",
        template="plotly_dark"
    )

fig.update_layout(
    xaxis_title=None,
    yaxis_title="Prix moyen ($)"
)
st.plotly_chart(fig, use_container_width=True)

# ----------- Filtrage selon le quartier et type ------------
st.subheader("🎛️ Explorer un quartier spécifique")
col1, col2 = st.columns(2)

with col1:
    quartier = st.selectbox("Choisissez un quartier :", sorted(df["Neighborhood"].unique()))

with col2:
    style = st.selectbox("Choisissez un style de maison :", sorted(df["HouseStyle"].unique()))

filtre = df[(df["Neighborhood"] == quartier) & (df["HouseStyle"] == style)]

st.markdown(f"**📌 {len(filtre)} maisons** trouvées à **{quartier}** de type **{style}**")

fig_filtered = px.histogram(filtre, x="SalePrice", nbins=30,
                            title=f"Distribution des prix à {quartier} ({style})",
                            color_discrete_sequence=["#AF9979"])
fig_filtered.update_layout(xaxis_title="Prix ($)", yaxis_title="Nombre de maisons")
st.plotly_chart(fig_filtered, use_container_width=True, key="prix_par_quartier_style")


st.markdown("""
<hr>
📊 **Grâce à cette exploration, vous pouvez comparer facilement les maisons selon vos préférences, que vous soyez acheteur, agent ou investisseur.**  
N’hésitez pas à passer à l’onglet Prédiction pour estimer le prix d'une maison selon ses caractéristiques.  
""", unsafe_allow_html=True)
