import pandas as pd 
import joblib 

model = joblib.load("houseprice_model.pkl")

features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF',
     'FullBath', 'YearBuilt', '1stFlrSF',               # numeric
    'Neighborhood', 'ExterQual', 'KitchenQual', 'BsmtQual',
    'GarageFinish', 'Foundation', 'GarageType', 
    'HeatingQC', 'BsmtFinType1', 'MSZoning']

sample = pd.DataFrame({
    "OverallQual":[7],
    "GrLivArea":[1710],
    "GarageCars":[2],
    'TotalBsmtSF': [856],
    '1stFlrSF': [1262],
    'FullBath': [1],
    'YearBuilt': [2003],
    'Neighborhood': ['CollgCr'],
    'ExterQual': ["Gd"],
    'KitchenQual': ['Gd'],
    'BsmtQual':['Gd'],
    'GarageFinish':['RFn'],
    'Foundation':['PConc'],
    'GarageType':['Attchd'],
    'HeatingQC':['Ex'],
    'BsmtFinType1':['GLQ'],
    'MSZoning':['RL']

})

#Make prediciton 
pred = model.predict(sample)
print(f"Predicted Sales: Rs. {pred[0]:,.2f}")