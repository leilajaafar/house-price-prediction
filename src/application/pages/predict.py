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
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict house prices')
    st.sidebar.success('https://www.projetpfa.org')
    
    st.sidebar.image(image_house)
    
    st.title("House Price Prediction App")

    if add_selectbox == 'Online':
        OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
        GarageCars = st.slider("Garage Cars", 0, 5, 1)
        GarageArea = st.number_input("Garage Area (sq ft)", min_value=0, value=730)
        ExterQual = st.selectbox("Exterior Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
        GarageFinish = st.selectbox("Garage Finish", ['Fin', 'RFn', 'Unf', 'None'])
        KitchenQual = st.selectbox("Kitchen Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
        BsmtQual = st.selectbox("Basement Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'None'])
        YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=1961)
        TotalBsmtSF = st.number_input("Total Basement SF", min_value=0, value=882)
        GrLivArea = st.number_input("Above Ground Living Area (sq ft)", min_value=0, value=896)
        firstFlrSF = st.number_input("1st Floor SF", min_value=0, value=896)
        FullBath = st.slider("Full Bathrooms", 0, 4, 1)
        YearRemodAdd = st.number_input("Year Remodeled", min_value=1800, max_value=2025, value=1961)
        Fireplaces = st.slider("Number of Fireplaces", 0, 5, 0)
        HeatingQC = st.selectbox("Heating Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
        TotRmsAbvGrd = st.slider("Total Rooms Above Grade", 1, 15, 5)
        MasVnrArea = st.number_input("Masonry Veneer Area (sq ft)", min_value=0, value=0)
        BsmtFinSF1 = st.number_input("Basement Finished SF 1", min_value=0, value=468)
        BsmtExposure = st.selectbox("Basement Exposure", ['Gd', 'Av', 'Mn', 'No', 'None'])
        LotFrontage = st.number_input("Lot Frontage", min_value=0, value=80)
        WoodDeckSF = st.number_input("Wood Deck SF", min_value=0, value=140)
        OpenPorchSF = st.number_input("Open Porch SF", min_value=0, value=0)
        Neighborhood = st.selectbox("Neighborhood", [
            'NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst', 'Sawyer', 'NridgHt', 'NWAmes', 'Mitchel',
            'Timber', 'ClearCr', 'Crawfor', 'BrkSide', 'IDOTRR', 'MeadowV', 'Blmngtn', 'SWISU', 'NPkVill',
            'Blueste', 'Veenker', 'Gilbert', 'NoRidge', 'StoneBr'
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
        
        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == "__main__":
    run()