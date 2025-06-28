# train_model.py
# By KolbySec (Jens Kolby) - 2025

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Sample data
data = {
    'duration': [0, 0, 2, 0, 1],
    'protocol_type': ['tcp', 'udp', 'tcp', 'icmp', 'tcp'],
    'service': ['http', 'domain_u', 'ftp', 'ecr_i', 'smtp'],
    'flag': ['SF', 'SF', 'S0', 'SF', 'REJ'],
    'src_bytes': [181, 239, 0, 1032, 545],
    'dst_bytes': [5450, 486, 0, 0, 0],
    'label': ['normal', 'normal', 'neptune', 'neptune', 'satan']
}

df = pd.DataFrame(data)

# Encode categorical values
for col in ['protocol_type', 'service', 'flag']:
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop(columns=['label'])
y = df['label']

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, "model.pkl")
print("✅ Model saved as model.pkl")
