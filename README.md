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

4. ## 📄 Try It Instantly – Sample Data

You can test the intrusion detection app using one of the sample files below:

- ⚡ **Quick Demo (4 rows)** – lightweight and fast:  
  [small_sample_network_log.csv](https://raw.githubusercontent.com/Haddoc67/mitre-ml-intrusion-detector/main/sample_data/small_sample_network_log.csv)

- 🧪 **Large Test (approx. 21 MB, 200K rows)** – for performance testing:  
  [large_sample_network_log.csv](https://raw.githubusercontent.com/Haddoc67/mitre-ml-intrusion-detector/main/large_sample/large_sample_network_log.csv)

---

Just download the file that suits your test needs, then upload it directly to the app to see predictions and MITRE ATT&CK mappings.

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

