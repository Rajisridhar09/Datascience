import streamlit as st #framework building interactive web application directly from python without an UI
import pandas as pd
import joblib

model = joblib.load("houseprice_model.pkl")

st.set_page_config(page_title = "House Price  Prediction",page_icon="🛒", layout = 'centered')

st.title("🛒 House Price Prediction APP")
st.markdown("""This app is going to predict ***House Price*** based on the 
input values I provide, Once done click ***Predict Sales*** button""")


with st.form("input_form"):
    st.header("Enter Product & Outlet Details")
    col1, col2 = st.columns(2)
    with col1: 
        OverallQual = st.number_input("OverallQual", min_value=0.0, step= 0.1)
        GrLivArea = st.number_input("GrLivArea", min_value=0.0, step= 0.001)
        GarageCars = st.selectbox("GarageCars",[0,1,2,3])
        TotalBsmtSF = st.number_input("TotalBsmtSF", min_value=0, step= 1)
        #1stFlrSF = st.number_input("Outlet Location Score",min_value=0.0, step= 0.1)
        Flr1SF = st.number_input("1st Floor Square Feet", min_value=0.0, step=0.1)

        FullBath = st.selectbox("FullBath",[0,1,2])
        YearBuilt = st.number_input("YearBuilt", min_value=0.0, step= 0.5)
        
    with col2: 
        Neighborhood =  st.selectbox("Neighborhood",['CollgCr','Veenker','Mitchel','Somerst','NWAmes','BrkSide'])
        ExterQual = st.selectbox("ExterQual", ["Gd","TA","Ex",'Fa'])
        KitchenQual = st.selectbox("KitchenQual",["Gd","TA","Ex",'Fa'])
        BsmtQual = st.selectbox("BsmtQual", ["Gd","TA","Ex",'Fa'])
        GarageFinish = st.selectbox("GarageFinish", ['RFn','Unf','Fin','NA'])
        Foundation = st.selectbox("Foundation",['PConc','CBlock','BrkTil','Wood','Slab'])
        GarageType =  st.selectbox("GarageType",['Attchd','Detchd','BuiltIn'])
        HeatingQC = st.selectbox("HeatingQC", ["Gd","TA","Ex",'Fa'])
        BsmtFinType1 = st.selectbox("BsmtFinType1",['GLQ',"ALQ","Unf",'LwQ','NA'])
        MSZoning = st.selectbox("MSZoning", ['RM','RL','FV'])

    # values = st.text_input("Enter multiple MPRs")
    # m_values = [float(v) for v in values.split(',')]
    # st.write("MRPs entered:",m_values)
    #uploaded = st.file_uploder("Enter your CSV",type = ['csv','xlsx'])
    #data = pd.read_csv(uploaded)
    submitted = st.form_submit_button("Predict Sales")
    

if submitted: 
    input_df = pd.DataFrame({
    "OverallQual":[OverallQual],
    "GrLivArea":[GrLivArea],
    "GarageCars":[GarageCars],
    "TotalBsmtSF":[TotalBsmtSF],
    '1stFlrSF': [Flr1SF],
    'FullBath': [FullBath],
    'YearBuilt': [YearBuilt],
    'Neighborhood': [Neighborhood],
    'ExterQual': [ExterQual],
    'KitchenQual': [KitchenQual],
    'BsmtQual': [BsmtQual],
    'GarageFinish': [GarageFinish],
    'Foundation': [Foundation],
    'GarageType': [GarageType],
    'HeatingQC': [HeatingQC],
    'BsmtFinType1': [BsmtFinType1],
    'MSZoning': [MSZoning]

    })

    pred = model.predict(input_df)[0]
    st.success(f" Predicted Sales: Rs. {pred:.2f}")
    st.balloons()