# Created by KolbySec, 2025
__author__ = "KolbySec"

import streamlit as st
import pandas as pd
import joblib
import sys
import os

# Gør det muligt at importere src/ uanset hvor app.py ligger
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from mitre_mapper import map_to_mitre

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("AI Intrusion Detection with MITRE ATT&CK Mapping")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    # Fjern 'label'-kolonnen hvis den findes
    X = df.drop(columns=["label"], errors='ignore')

    predictions = model.predict(X)

    st.subheader("Predictions")
    for i, pred in enumerate(predictions):
        st.write(f"Row {i+1}: {pred}")
        mitre = map_to_mitre(pred)
        if mitre:
            st.markdown(f"""
            - Technique: {mitre['technique']} ({mitre['id']})  
            - Tactic: {mitre['tactic']}  
            - [View on MITRE ATT&CK]({mitre['url']})
            """)
        else:
            st.write("No MITRE mapping found.")
