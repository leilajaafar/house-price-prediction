import streamlit as st
import pandas as pd
import numpy as np
from pycaret.regression import load_model, predict_model

#model = load_model(r'/Users/macbook/house-price-prediction/notebooks/dimensionality reduction/finalmodel')
#model = load_model('../../notebooks/dimensionality reduction/finalmodel')
model = load_model('notebooks/dimensionality reduction/finalmodel')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['prediction_label'][0]
    return predictions

def run():
    from PIL import Image
    #image = Image.open(r'C:\Users\leila\Downloads\pfaproject\house-price-prediction\src\application\assets\ESTILOGO.png')
    #image_house = Image.open(r'/Users/macbook/house-price-prediction/src/application/assets/house1.png')
    image_house = Image.open('assets/house1.png')

    #st.image(image, use_column_width=False)
    
    add_selectbox = st.sidebar.selectbox(
    "Comment souhaitez-vous effectuer la prédiction ?",
    ("En ligne", "Par lot"))

    st.sidebar.info("Cette application est conçue pour prédire les prix des maisons.")
    st.sidebar.success("https://www.projetpfa.org")
    
    st.sidebar.image(image_house)
    
    st.title("Prédiction de Prix des Maisons")

    if add_selectbox == 'En ligne':
        OverallQual = st.slider("Qualité globale (1-10)", 1, 10, 5)
        GarageCars = st.slider("Nombre de voitures dans le garage", 0, 5, 1)
        GarageArea = st.number_input("Surface du garage (en pieds carrés)", min_value=0, value=730)
        ExterQual = st.selectbox("Qualité extérieure", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
        GarageFinish = st.selectbox("Finition du garage", ['Fin', 'RFn', 'Unf', 'None'])
        KitchenQual = st.selectbox("Qualité de la cuisine", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
        BsmtQual = st.selectbox("Qualité du sous-sol", ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'None'])
        YearBuilt = st.number_input("Année de construction", min_value=1800, max_value=2025, value=1961)
        TotalBsmtSF = st.number_input("Surface totale du sous-sol", min_value=0, value=882)
        GrLivArea = st.number_input("Surface habitable au-dessus du sol (en pieds carrés)", min_value=0, value=896)
        firstFlrSF = st.number_input("Surface du 1er étage (en pieds carrés)", min_value=0, value=896)
        FullBath = st.slider("Nombre de salles de bain complètes", 0, 4, 1)
        YearRemodAdd = st.number_input("Année de rénovation", min_value=1800, max_value=2025, value=1961)
        Fireplaces = st.slider("Nombre de cheminées", 0, 5, 0)
        HeatingQC = st.selectbox("Qualité du système de chauffage", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
        TotRmsAbvGrd = st.slider("Nombre total de pièces au-dessus du sol", 1, 15, 5)
        MasVnrArea = st.number_input("Surface du parement en maçonnerie (en pieds carrés)", min_value=0, value=0)
        BsmtFinSF1 = st.number_input("Surface aménagée du sous-sol (partie 1)", min_value=0, value=468)
        BsmtExposure = st.selectbox("Exposition du sous-sol", ['Gd', 'Av', 'Mn', 'No', 'None'])
        LotFrontage = st.number_input("Façade du terrain (en pieds)", min_value=0, value=80)
        WoodDeckSF = st.number_input("Surface de la terrasse en bois", min_value=0, value=140)
        OpenPorchSF = st.number_input("Surface du porche ouvert", min_value=0, value=0)
        Neighborhood = st.selectbox("Quartier", [
            'NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst', 'Sawyer', 'NridgHt', 'NWAmes', 'Mitchel',
            'Timber', 'ClearCr', 'Crawfor', 'BrkSide', 'IDOTRR', 'MeadowV', 'Blmngtn', 'SWISU', 'NPkVill',
            'Blueste', 'Veenker', 'Gilbert', 'NoRidge', 'StoneBr'
            ])
        
        output = ""

        input_dict = {
            'OverallQual': OverallQual,
            'GarageCars': GarageCars,
            'GarageArea': GarageArea,
            'ExterQual': ExterQual,
            'GarageFinish': GarageFinish,
            'KitchenQual': KitchenQual,
            'BsmtQual': BsmtQual,
            'YearBuilt': YearBuilt,
            'TotalBsmtSF': TotalBsmtSF,
            'GrLivArea': GrLivArea,
            '1stFlrSF': firstFlrSF,
            'FullBath': FullBath,
            'YearRemodAdd': YearRemodAdd,
            'Fireplaces': Fireplaces,
            'HeatingQC': HeatingQC,
            'TotRmsAbvGrd': TotRmsAbvGrd,
            'MasVnrArea': MasVnrArea,
            'BsmtFinSF1': BsmtFinSF1,
            'BsmtExposure': BsmtExposure,
            'LotFrontage': LotFrontage,
            'WoodDeckSF': WoodDeckSF,
            'OpenPorchSF': OpenPorchSF,
            'Neighborhood': Neighborhood
        }
        
        input_df = pd.DataFrame([input_dict])
        
        if st.button("Prédire"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)
        
        st.success(f'Le prix estimé est {output}')

    if add_selectbox == 'Par lot':

        file_upload = st.file_uploader("Téléchargez un fichier CSV pour les prédictions", type=["csv"])
        
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model, data=data)
            st.write(predictions)

if __name__ == "__main__":
    run()
