# Created by KolbySec, 2025
__author__ = "KolbySec"

# app/app.py

import streamlit as st
import pandas as pd
import joblib
import os
import sys
 
from mitre_mapper import map_to_mitre


st.title("MITRE ML Intrusion Detector")

st.markdown("""
Upload en netværkslogfil i CSV-format. Appen vil analysere hver forbindelse og vurdere om den er normal eller en kendt angrebstype.
Resultaterne bliver derefter matchet til relevante MITRE ATT&CK teknikker.
""")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

uploaded_file = st.file_uploader("Vælg din CSV-fil", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Gem originale kolonner til visning
    original_data = df.copy()

    # Fjern label hvis den findes
    if 'label' in df.columns:
        df = df.drop('label', axis=1)

    # Sikrer at kolonnerne matcher det modellen forventer
    expected_cols = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes']
    if not all(col in df.columns for col in expected_cols):
        st.error("Filen mangler nødvendige kolonner. Forventet: " + ", ".join(expected_cols))
    else:
        # One-hot encode de nødvendige kolonner (med dummy_na for sikkerhed)
        df_encoded = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'], dummy_na=True)

        # Sikr kolonner matcher modelens input
        model_input_cols = model.feature_names_in_
        for col in model_input_cols:
            if col not in df_encoded.columns:
                df_encoded[col] = 0  # tilføj manglende kolonner som 0

        df_encoded = df_encoded[model_input_cols]

        # Forudsig
        predictions = model.predict(df_encoded)
        original_data["Prediction"] = predictions
        original_data["MITRE Technique"] = original_data["Prediction"].apply(map_to_mitre)

        st.success("Analyse fuldført.")
        st.dataframe(original_data)

        # Download knap
        csv = original_data.to_csv(index=False).encode('utf-8')
        st.download_button("Download resultater som CSV", data=csv, file_name="mitre_analysis.csv", mime="text/csv")
