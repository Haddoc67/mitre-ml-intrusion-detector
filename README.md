# MITRE-Aware ML Intrusion Detector

This project combines machine learning with MITRE ATT&CK mapping to classify and analyze network traffic for security threats.

## 🔍 Features
- 📊 Machine learning model (Random Forest)
- 📁 Upload your own CSV with network activity
- 🧠 Predict intrusion type (e.g., neptune, satan)
- 🛡️ Map threats to MITRE ATT&CK techniques & tactics
- 🌐 Easy-to-use web interface with Streamlit

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Haddoc67/mitre-ml-intrusion-detector.git
cd mitre-ml-intrusion-detector
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app/app.py
```

4. Upload the provided `test_nsl_kdd.csv` file or your own.

## 🧠 ML Model

- Type: `RandomForestClassifier`
- Trained on sample NSL-KDD-like data
- Encodes protocol, service, and flags using `LabelEncoder`

## 🗺️ MITRE Mapping

Intrusion labels (e.g., `neptune`, `satan`) are mapped to:
- MITRE Technique ID
- Technique Name
- Tactic
- ATT&CK Link

Mapping is handled in `src/mitre_mapper.py`.

## 👤 Author

Created by **kolbySec**   
Cybersecurity Analyst & AI/ML Developer  
GitHub Profile: https://github.com/Haddoc67

