🚢 Vessel Fuel & CO₂ Emission Prediction

A machine learning-powered web application that predicts vessel fuel consumption and CO₂ emissions based on operational parameters. This project combines data science, cloud-based data collection, and business intelligence visualization to deliver actionable insights for maritime efficiency and sustainability.

🔗 Live App: https://vessel-fuel-co2-prediction-synergyship.streamlit.app/

📂 Repository: https://github.com/bgauri05/vessel-fuel-co2-ml

📌 Overview

This application enables maritime stakeholders to:

🚢 Predict vessel fuel consumption
🌍 Estimate CO₂ emissions
📊 Analyze operational efficiency
⚡ Make data-driven sustainability decisions

The system is designed as an end-to-end pipeline integrating ML predictions with real-time data storage and visualization tools.

🧠 Key Features
🔮 Machine Learning-based prediction (Regression model)
📊 Interactive Streamlit web interface
☁️ Google Sheets as a real-time cloud database
📈 Power BI dashboards for advanced analytics
⚡ Fast, user-friendly, and deployable system
🏗️ Tech Stack
Frontend/UI: Streamlit
Backend/ML: scikit-learn
Data Processing: pandas, NumPy
Cloud Data Layer: Google Sheets API
Visualization: Power BI
📊 How It Works
User inputs vessel parameters (speed, engine specs, etc.)
Data is processed and passed to the trained ML model
Model predicts:
Fuel consumption
CO₂ emissions
Predictions are:
Displayed in Streamlit
Stored in Google Sheets
Power BI connects to this dataset for visualization
⚙️ Machine Learning Model
Model Type: Regression (e.g., Random Forest)
Captures non-linear relationships between vessel parameters and emissions
Key Features:
Speed
Engine power
Load conditions
Voyage characteristics
☁️ Data Storage & Collection (Google Sheets)

This application uses Google Sheets as a lightweight cloud database to store prediction data in real time.

🔗 Workflow
User Input → ML Model → Prediction → Google Sheets → Power BI Dashboard
⚙️ API Integration

The app integrates with the Google Sheets API via a service account.

🔑 Implementation Steps:
Created project in Google Cloud Console
Enabled Google Sheets API
Generated service account credentials (JSON)
Shared Google Sheet with service account email
Connected using Python (gspread, google-auth)
💻 Example Code
import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("Vessel Fuel Data").sheet1
sheet.append_row([speed, engine_power, fuel, co2])
✅ Benefits
No need for traditional database setup
Real-time data logging
Easy integration with analytics tools
Cloud accessibility
📈 Power BI Integration (Visual Analytics)

This project integrates Power BI to transform prediction data into interactive dashboards.

🔄 Workflow
Prediction data stored in Google Sheets
Power BI connects to the dataset
Dashboards update with new predictions
📊 Dashboard Insights
Fuel consumption trends
CO₂ emission patterns
Efficiency comparisons
Operational optimization scenarios

This enhances the application into a decision-support system, not just a prediction tool.

🛠️ How This Application Was Built
1. Data Preprocessing
Cleaned dataset and handled missing values
Selected key influencing features
2. Exploratory Data Analysis
Identified relationships between variables
Guided feature engineering
3. Model Development
Tested multiple regression models
Selected best-performing model
Tuned hyperparameters
4. Deployment
Serialized model using pickle
Built UI using Streamlit
5. Cloud Data Integration
Connected app to Google Sheets API
Stored predictions in real time
6. Business Intelligence Layer
Connected Power BI to dataset
Built dashboards with KPIs and trends
🚀 Installation & Setup
# Clone repository
git clone https://github.com/bgauri05/vessel-fuel-co2-ml.git

cd vessel-fuel-co2-ml

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
📂 Project Structure
vessel-fuel-co2-ml/
│
├── app.py
├── model.pkl
├── data/
├── notebooks/
├── requirements.txt
└── README.md
🌍 Use Cases
Maritime fuel optimization
Emission monitoring
Sustainability reporting
Operational efficiency analysis
🔮 Future Improvements
Real-time IoT data integration
Cloud deployment (AWS/Azure)
API-based architecture
Advanced ML/DL models
🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

📜 License

This project is open-source under the MIT License.
