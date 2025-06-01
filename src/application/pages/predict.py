import streamlit as st
import pandas as pd
import numpy as np
from pycaret.regression import load_model, predict_model

model = load_model(r'C:\Users\leila\Downloads\pfaproject\house-price-prediction\notebooks\dimensionality reduction\finalmodel')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['prediction_label'][0]
    return predictions

def run():
    from PIL import Image
    #image = Image.open(r'C:\Users\leila\Downloads\pfaproject\house-price-prediction\src\application\assets\ESTILOGO.png')
    image_house = Image.open(r'C:\Users\leila\Downloads\pfaproject\house-price-prediction\src\application\assets\house1.png')

    #st.image(image, use_column_width=False)
    
    add_selectbox = st.sidebar.selectbox(
    "Comment voulez vous faire la prediction?",
    ("Online", "CSV"))

    st.sidebar.info('Cette app est faite pour prédire les prix des maisons!')
    #st.sidebar.success('https://www.projetpfa.org')
    
    st.sidebar.image(image_house)
    
    st.title("Application de Prédiction des Prix des Maisons")

    if add_selectbox == 'Online':
        OverallQual = st.slider("Qualité Globale (1-10)", 1, 10, 5)
        GarageCars = st.slider("Garage Voitures", 0, 5, 1)
        GarageArea = st.number_input("Surface du Garage (sq ft)", min_value=0, value=730)
        ExterQual = st.selectbox("Qualité d'Exterieur", ['Ex', 'Gd', 'TA', 'Fa', 'Po'], help="Ex: Excellent, Gd: Bon, TA: Moyen, Fa: Passable, Po: Mauvais")
        GarageFinish = st.selectbox("Etat du Garage", ['Fin', 'RFn', 'Unf', 'None'], help="Fin: Fini, RFn: Semi-fini, Unf: Non fini, NA: Pas de garage")
        KitchenQual = st.selectbox("Qualité de Cuisine", ['Ex', 'Gd', 'TA', 'Fa', 'Po'], help="Ex: Excellent, Gd: Bon, TA: Moyen, Fa: Passable, Po: Mauvais")
        BsmtQual = st.selectbox("Qualité du Sous-sol", ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'None'], help="Ex: Excellent (>254 cm), Gd: Bon (229,251 cm), TA: Typique (203,226 cm), Fa: Passable (178,201 cm), Po: Mauvais (<178 cm), NA: Pas de sous-sol")
        YearBuilt = st.number_input("Année Construit", min_value=1800, max_value=2025, value=1961)
        TotalBsmtSF = st.number_input("Sous-sol Total SF", min_value=0, value=882)
        GrLivArea = st.number_input("Espace de Vie Au Dessus (sq ft)", min_value=0, value=896)
        firstFlrSF = st.number_input("1er Etage SF", min_value=0, value=896)
        FullBath = st.slider("Salles de Bain Totals", 0, 5, 1)
        YearRemodAdd = st.number_input("Année Rénovée", min_value=1800, max_value=2025, value=1961)
        Fireplaces = st.slider("Nombre de Cheminées", 0, 6, 0)
        HeatingQC = st.selectbox("Qualité du Chauffage", ['Ex', 'Gd', 'TA', 'Fa', 'Po'], help="Ex: Excellent, Gd: Bon, TA: Moyen, Fa: Passable, Po: Mauvais")
        TotRmsAbvGrd = st.slider("Nombre Total de Pieces Hors Sol", 1, 16, 5)
        MasVnrArea = st.number_input("Placage de Maçonnerie (sq ft)", min_value=0, value=0)
        BsmtFinSF1 = st.number_input("Sous-sol Fini SF 1", min_value=0, value=468)
        BsmtExposure = st.selectbox("Exposition Sous-sol", ['Gd', 'Av', 'Mn', 'No', 'None'], help="Gd: Bonne exposition, Av: Moyenne, Mn: Minimale, No: Aucune exposition, NA: Pas de sous-sol")
        LotFrontage = st.number_input("Façade de Terrain", min_value=0, value=80)
        WoodDeckSF = st.number_input("Terrasse en Bois SF", min_value=0, value=140)
        OpenPorchSF = st.number_input("Véranda ouverte SF", min_value=0, value=0)
        Neighborhood = st.selectbox("Quartier", [
            'NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst', 'Sawyer', 'NridgHt', 'NWAmes', 'Mitchel',
            'Timber', 'ClearCr', 'Crawfor', 'BrkSide', 'IDOTRR', 'MeadowV', 'Blmngtn', 'SWISU', 'NPkVill',
            'Blueste', 'Veenker', 'Gilbert', 'NoRidge', 'StoneBr', 'SawyerW', 'BrDale'
            ])
        
        output=""

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
        
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)
        
        st.success('Le prix de votre maison est de {}'.format(output))

    if add_selectbox == 'CSV':

        file_upload = st.file_uploader("Upload un fichier csv pour la prediction", type=["csv"])
        
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == "__main__":
    run()