# -*- coding: utf-8 -*-
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Maritime Analytics Platform",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Logo in top right corner
st.markdown("""
<div class="logo-container">
    <img src="https://www.synergymg.com/images/logo.png" width="120" alt="Synergy Marine Group" onerror="this.src='https://via.placeholder.com/120x40/1e40af/ffffff?text=Synergy+Marine'">
</div>
""", unsafe_allow_html=True)

# Custom CSS for maritime theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.85);
        z-index: -1;
    }
    .main {
        background: transparent;
    }
    h1 {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        text-align: center;
        padding: 20px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    h2 {
        color: #1e40af;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 10px;
    }
    h3 {
        color: #1e40af;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0ea5e9, #0369a1);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 40px;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0369a1, #075985);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        color: #1e40af;
    }
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(2px);
    }
    [data-testid="stSidebar"] h2 {
        color: #1e40af !important;
        font-weight: bold !important;
    }
    [data-testid="stSidebar"] h3 {
        color: #1e40af !important;
        font-weight: bold !important;
    }
    [data-testid="stSidebar"] p {
        color: #000000 !important;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: #000000 !important;
    }
    [data-testid="stSidebar"] li {
        color: #000000 !important;
    }
    .logo-container {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 999;
        background: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Load models & encoders
try:
    fuel_model = joblib.load('fuel_model.pkl')
    co2_model = joblib.load('co2_model.pkl')
    encoders = joblib.load('encoders.pkl')
except Exception as e:
    st.error(f"⚠️ Error loading models: {e}")
    st.stop()

# Header
st.markdown("# ⚓ Synergy Maritime Analytical Platform")
st.markdown("### 🌊 Intelligent Fuel & CO₂ Emission Forecasting System")
st.markdown("---")

# Sidebar with info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=150)
    st.markdown("## 📊 About")
    st.info("""
    This advanced AI-powered platform helps ship management companies:
    
    ✅ Predict fuel consumption  
    ✅ Estimate CO₂ emissions  
    ✅ Optimize voyage planning  
    ✅ Reduce operational costs  
    ✅ Meet environmental compliance
    """)
    st.markdown("---")
    st.markdown("### 🎯 How to Use")
    st.markdown("""
    1. Select vessel parameters
    2. Enter voyage details
    3. Click **Predict**
    4. View results & insights
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 🚢 Vessel Information")
    ship_type = st.selectbox("⚓ Ship Type", list(encoders['SHIP_TYPE_ID'].classes_), help="Select the type of vessel")
    route_id = st.selectbox("🗺️ Route", list(encoders['ROUTE_ID'].classes_), help="Select the shipping route")
    month = st.selectbox("📅 Month", list(encoders['MONTH'].classes_), help="Select the month of voyage")
    
with col2:
    st.markdown("## ⚙️ Technical Parameters")
    fuel_type = st.selectbox("⛽ Fuel Type", list(encoders['FUEL_TYPE_ID'].classes_), help="Type of fuel used")
    weather = st.selectbox("🌤️ Weather Conditions", list(encoders['WEATHER_CONDITIONS'].classes_), help="Expected weather conditions")

st.markdown("---")

# Numeric inputs in columns
st.markdown("## 📐 Voyage Metrics")
col3, col4 = st.columns(2)

with col3:
    distance = st.number_input("🌍 Distance (km)", min_value=0.0, step=10.0, value=1000.0, help="Total voyage distance in kilometers")
    
with col4:
    engine_eff = st.number_input("⚡ Engine Efficiency (%)", min_value=0.0, max_value=100.0, step=1.0, value=85.0, help="Current engine efficiency percentage")

st.markdown("---")

# Predict button centered
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🔮 Generate Predictions")

if predict_button:
    with st.spinner('🔄 Analyzing voyage parameters...'):
        # Encode categoricals exactly like in training
        ship_num = encoders['SHIP_TYPE_ID'].transform([ship_type])[0]
        route_num = encoders['ROUTE_ID'].transform([route_id])[0]
        month_num = encoders['MONTH'].transform([month])[0]
        fuel_num = encoders['FUEL_TYPE_ID'].transform([fuel_type])[0]
        weather_num = encoders['WEATHER_CONDITIONS'].transform([weather])[0]

        row = np.array([[ship_num, route_num, month_num, distance,
                         fuel_num, weather_num, engine_eff]])

        fuel_pred = fuel_model.predict(row)[0]
        co2_pred = co2_model.predict(row)[0]

    st.markdown("---")
    st.markdown("## 📊 Prediction Results")
    
    # Display results in metric cards
    col_res1, col_res2, col_res3 = st.columns(3)
    
    with col_res1:
        st.metric(
            label="⛽ Fuel Consumption",
            value=f"{fuel_pred:,.0f} L",
            delta=f"{(fuel_pred/distance):.2f} L/km" if distance > 0 else "N/A"
        )
    
    with col_res2:
        st.metric(
            label="🌍 CO₂ Emissions",
            value=f"{co2_pred:,.0f} kg",
            delta=f"{(co2_pred/distance):.2f} kg/km" if distance > 0 else "N/A"
        )
    
    with col_res3:
        carbon_trees = co2_pred / 21  # 1 tree absorbs ~21kg CO2/year
        st.metric(
            label="🌳 Carbon Offset",
            value=f"{carbon_trees:.0f} trees",
            delta="Required for 1 year"
        )
    
    # Insights section
    st.markdown("---")
    st.markdown("### 💡 Voyage Insights")
    
    col_insight1, col_insight2 = st.columns(2)
    
    with col_insight1:
        st.info(f"""
        **📍 Route Efficiency**  
        - Distance: {distance:,.0f} km  
        - Fuel per km: {(fuel_pred/distance):.2f} L/km  
        - Engine efficiency: {engine_eff:.0f}%
        """)
    
    with col_insight2:
        st.warning(f"""
        **🌱 Environmental Impact**  
        - CO₂ per km: {(co2_pred/distance):.2f} kg/km  
        - Carbon footprint: {co2_pred:,.0f} kg  
        - Trees to offset: {carbon_trees:.0f} trees/year
        """)

    # Optional: log to CSV for Power BI
    result_df = pd.DataFrame([{
        "SHIP_TYPE": ship_type,
        "ROUTE_ID": route_id,
        "MONTH": month,
        "FUEL_TYPE": fuel_type,
        "WEATHER": weather,
        "DISTANCE": distance,
        "ENGINE_EFFICIENCY": engine_eff,
        "Predicted_Fuel_L": fuel_pred,
        "Predicted_CO2_kg": co2_pred
    }])

    import os
    LOG_PATH = "prediction_log.csv"
    if os.path.exists(LOG_PATH):
        result_df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        result_df.to_csv(LOG_PATH, index=False)

    st.success("✅ Prediction saved to prediction_log.csv for Power BI analytics!")
    
# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p>🚢 <strong>Synergy Maritime Analytical Platform</strong> | Powered by AI & Machine Learning</p>
    <p>Optimizing maritime operations for a sustainable future 🌊</p>
</div>
""", unsafe_allow_html=True)
