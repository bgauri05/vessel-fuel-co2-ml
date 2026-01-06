# -*- coding: utf-8 -*-
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

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
        background: rgba(255, 255, 255, 0.05);
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
        color: #ffffff;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    h3 {
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }
    p {
        color: #ffffff !important;
    }
    label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    .stMarkdown {
        color: #ffffff !important;
    }
    /* Input field labels */
    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    /* Dropdown selected value */
    div[data-baseweb="select"] > div,
    div[data-baseweb="select"] div,
    .stSelectbox > div > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    /* Dropdown menu options */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] div {
        background-color: #ffffff !important;
    }
    ul[role="listbox"],
    ul[role="listbox"] li {
        background-color: #ffffff !important;
    }
    li[role="option"],
    li[role="option"] div,
    li[role="option"] span {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    li[role="option"]:hover,
    li[role="option"]:hover div,
    li[role="option"]:hover span {
        background-color: #e0f2fe !important;
        color: #000000 !important;
    }
    /* Number input fields */
    input[type="number"],
    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
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
        color: #ffffff;
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-weight: bold;
    }
    div[data-testid="stMetricDelta"] {
        color: #ffffff !important;
    }
    /* Metric containers */
    div[data-testid="stMetric"] {
        background-color: rgba(30, 58, 138, 0.6) !important;
        padding: 15px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(59, 130, 246, 0.5) !important;
    }
    .element-container div[data-testid="stAlert"] {
        background-color: rgba(30, 58, 138, 0.9) !important;
        color: #ffffff !important;
        border: 1px solid rgba(59, 130, 246, 0.5) !important;
    }
    .element-container div[data-testid="stAlert"] p {
        color: #ffffff !important;
    }
    .element-container div[data-testid="stAlert"] strong {
        color: #ffffff !important;
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
    # Get the directory where this script is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Build full paths to model files
    fuel_model_path = os.path.join(base_path, 'fuel_model.pkl')
    co2_model_path = os.path.join(base_path, 'co2_model.pkl')
    encoders_path = os.path.join(base_path, 'encoders.pkl')
    
    fuel_model = joblib.load(fuel_model_path)
    co2_model = joblib.load(co2_model_path)
    encoders = joblib.load(encoders_path)
except Exception as e:
    st.error(f"⚠️ Error loading models: {e}")
    st.stop()

# Ship type to fuel type mapping (based on historical data)
# FUEL_TYPE1 = HFO (Heavy Fuel Oil), FUEL_TYPE2 = Diesel
SHIP_FUEL_CONSTRAINTS = {
    'Oil Service Boat': ['HFO', 'Diesel'],
    'Fishing Trawler': ['HFO', 'Diesel'],
    'Surfer Boat': ['Diesel'],
    'Tanker Ship': ['HFO', 'Diesel']
}

# Mapping dictionaries for display names to IDs
SHIP_TYPE_MAP = {
    'Oil Service Boat': 'TYPE1',
    'Fishing Trawler': 'TYPE2',
    'Surfer Boat': 'TYPE3',
    'Tanker Ship': 'TYPE4'
}

ROUTE_MAP = {
    'Warri-Bonny': 'ROUTE1',
    'Port Harcourt-Lagos': 'ROUTE2',
    'Lagos-Apapa': 'ROUTE3',
    'Escravos-Lagos': 'ROUTE4'
}

FUEL_TYPE_MAP = {
    'HFO': 'FUEL_TYPE1',
    'Diesel': 'FUEL_TYPE2'
}

# Header
st.markdown("# ⚓ Synergy Maritime Analytical Platform")
st.markdown("### 🌊 Intelligent Fuel & CO₂ Emission Forecasting System")
st.markdown("---")

# Sidebar with info
with st.sidebar:
    st.image("synergy-logo.webp", width=150)
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
    ship_type = st.selectbox("⚓ Ship Type", list(SHIP_TYPE_MAP.keys()), help="Select the type of vessel")
    route_id = st.selectbox("🗺️ Route", list(ROUTE_MAP.keys()), help="Select the shipping route")
    month = st.selectbox("📅 Month", list(encoders['MONTH'].classes_), help="Select the month of voyage")
    
with col2:
    st.markdown("## ⚙️ Technical Parameters")
    # Filter fuel types based on selected ship type
    available_fuels = SHIP_FUEL_CONSTRAINTS.get(ship_type, list(FUEL_TYPE_MAP.keys()))
    fuel_type = st.selectbox("⛽ Fuel Type", available_fuels, help="Type of fuel used (restricted by ship type)")
    weather = st.selectbox("🌤️ Weather Conditions", list(encoders['WEATHER_CONDITIONS'].classes_), help="Expected weather conditions")

st.markdown("---")

# Numeric inputs in columns
st.markdown("## 📐 Voyage Metrics")
col3, col4 = st.columns(2)

with col3:
    distance = st.number_input("🌍 Distance (NM)", min_value=0.0, step=10.0, value=1000.0, help="Total voyage distance in nautical miles")
    
with col4:
    engine_eff = st.number_input("⚡ Engine Efficiency (%)", min_value=0.0, max_value=100.0, step=1.0, value=85.0, help="Current engine efficiency percentage")

st.markdown("---")

# Predict button centered
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🔮 Generate Predictions")

if predict_button:
    with st.spinner('🔄 Analyzing voyage parameters...'):
        # Convert display names to IDs for encoding
        ship_type_id = SHIP_TYPE_MAP[ship_type]
        route_id_code = ROUTE_MAP[route_id]
        fuel_type_id = FUEL_TYPE_MAP[fuel_type]
        
        # Encode categoricals exactly like in training
        ship_num = encoders['SHIP_TYPE_ID'].transform([ship_type_id])[0]
        route_num = encoders['ROUTE_ID'].transform([route_id_code])[0]
        month_num = encoders['MONTH'].transform([month])[0]
        fuel_num = encoders['FUEL_TYPE_ID'].transform([fuel_type_id])[0]
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
            delta=f"{(fuel_pred/distance):.2f} L/NM" if distance > 0 else "N/A"
        )
    
    with col_res2:
        st.metric(
            label="🌍 CO₂ Emissions",
            value=f"{co2_pred:,.0f} kg",
            delta=f"{(co2_pred/distance):.2f} kg/NM" if distance > 0 else "N/A"
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
        st.markdown(f"""
        <div style='background-color: rgba(30, 58, 138, 0.9); padding: 20px; border-radius: 10px; border: 1px solid rgba(59, 130, 246, 0.5);'>
        <p style='color: white; margin: 0;'><strong style='color: white;'>📍 Route Efficiency</strong></p>
        <p style='color: white; margin: 5px 0 0 0;'>• Distance: {distance:,.0f} NM</p>
        <p style='color: white; margin: 5px 0 0 0;'>• Fuel per NM: {(fuel_pred/distance):.2f} L/NM</p>
        <p style='color: white; margin: 5px 0 0 0;'>• Engine efficiency: {engine_eff:.0f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_insight2:
        st.markdown(f"""
        <div style='background-color: rgba(30, 58, 138, 0.9); padding: 20px; border-radius: 10px; border: 1px solid rgba(59, 130, 246, 0.5);'>
        <p style='color: white; margin: 0;'><strong style='color: white;'>🌱 Environmental Impact</strong></p>
        <p style='color: white; margin: 5px 0 0 0;'>• CO₂ per NM: {(co2_pred/distance):.2f} kg/NM</p>
        <p style='color: white; margin: 5px 0 0 0;'>• Carbon footprint: {co2_pred:,.0f} kg</p>
        <p style='color: white; margin: 5px 0 0 0;'>• Trees to offset: {carbon_trees:.0f} trees/year</p>
        </div>
        """, unsafe_allow_html=True)

    # Log to Google Sheets
    from datetime import datetime
    try:
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        
        # Setup Google Sheets connection
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        # Try to use Streamlit secrets (for cloud deployment)
        try:
            creds_dict = dict(st.secrets["gcp_service_account"])
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        except:
            # Fallback to local JSON file
            creds_path = os.path.join(base_path, 'service-account.json')
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        
        client = gspread.authorize(creds)
        
        # Try to open the spreadsheet
        try:
            spreadsheet = client.open("Vessel-Predictions")
            sheet = spreadsheet.sheet1
        except gspread.exceptions.SpreadsheetNotFound:
            st.error("❌ Spreadsheet 'Vessel-Predictions' not found.")
            st.info("Please create a Google Sheet named 'Vessel-Predictions' and share it with: streamlit-app@flawless-age-483408-b0.iam.gserviceaccount.com")
            raise
        
        # Prepare row data
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            str(ship_type),
            str(route_id),
            str(month),
            str(fuel_type),
            str(weather),
            str(distance),
            str(engine_eff),
            str(round(fuel_pred, 2)),
            str(round(co2_pred, 2))
        ]
        
        # Add header if sheet is empty
        all_values = sheet.get_all_values()
        if len(all_values) == 0:
            sheet.append_row(["Timestamp", "Ship Type", "Route", "Month", "Fuel Type", "Weather", "Distance", "Engine Efficiency", "Predicted Fuel (L)", "Predicted CO2 (kg)"])
        
        sheet.append_row(row)
        st.success("✅ Prediction logged to Google Sheets successfully!")
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        st.warning(f"⚠️ Could not log to Google Sheets: {str(e)}")
        with st.expander("Error details"):
            st.code(error_details)
    
    
# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p>🚢 <strong>Synergy Maritime Analytical Platform</strong> | Powered by AI & Machine Learning</p>
    <p>Optimizing maritime operations for a sustainable future 🌊</p>
</div>
""", unsafe_allow_html=True)
