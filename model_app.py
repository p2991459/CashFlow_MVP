import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import streamlit as st

st.title('XGBOOST CASH_FLOW Predictor')
uploaded_file = st.file_uploader("Upload CASH FLOW CSV HERE", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], infer_datetime_format=True)
    df['Due  Date'] = pd.to_datetime(df['Due  Date'], infer_datetime_format=True)
    df['Transaction Date_year'] = df['Transaction Date'].dt.year
    df['Transaction Date_quarter'] = df['Transaction Date'].dt.quarter
    df['Transaction Date_month_number'] = df['Transaction Date'].dt.month
    df['Transaction Date_dayofyear'] = df['Transaction Date'].dt.dayofyear
    df['Transaction Date_dayofweek'] = df['Transaction Date'].dt.dayofweek
    df['Due  Date_year'] = df['Due  Date'].dt.year
    df['Due  Date_quarter'] = df['Due  Date'].dt.quarter
    df['Due  Date_month_number'] = df['Due  Date'].dt.month
    df['Due  Date_week'] = df['Due  Date'].dt.week
    df['Due  Date_dayofyear'] = df['Due  Date'].dt.dayofyear
    df['Due  Date_dayofweek'] = df['Due  Date'].dt.dayofweek
    inputs = list(df.columns)
    target = 'Outstanding Amount'
    features = st.multiselect("Select input Features", inputs)
    if len(features) > 0:
        X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.25, random_state=42)
        model = xgb.XGBRegressor(n_estimators=300)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        model.save_model('Oustanding_amount.bin')
        mse = mean_squared_error(y_test, y_pred)
        rmse = (mse ** 0.5)
        r2 = r2_score(y_test, y_pred)
        st.write(f"MSE Calculated: {mse}")
        st.write(f"RMSE Calculated: {rmse}")
        st.write(f"R Square Calculated: {r2}")
        with open("Oustanding_amount.bin", "rb") as bin_file:
            binary_data = bin_file.read()
        st.download_button(
            label="Download model file",
            data=binary_data,
            file_name="Oustanding_amount.bin",
            key="download-binary-button"
        )
