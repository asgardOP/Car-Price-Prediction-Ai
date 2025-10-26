# train_model.py file
# By Ali Emad

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
df = pd.read_csv("CarPrice_Assignment.csv")

# Drop unnecessary columns
df = df.drop(columns=["car_ID", "CarName"])

# Encode categorical features
for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Split features and target
X = df.drop(columns=["price"])
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

with open("car_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as car_model.pkl")
