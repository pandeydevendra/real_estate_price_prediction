import pandas as pd
import numpy as np
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]  # real_estate_price_prediction
DATASET_PATH = BASE_DIR / "data" / "delhi_rent_dataset.csv"
df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully")
print(df.head())

# ---------------------------------------
# 2. Features & Target
# ---------------------------------------
X = df[["locality", "bhk"]]
y = df["rent_inr"]

# ---------------------------------------
# 3. Train / Test Split
# ---------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------
# 4. Preprocessing (One-Hot Encoding)
# ---------------------------------------
categorical_features = ["locality", "bhk"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# ---------------------------------------
# 5. Model
# ---------------------------------------
model = LinearRegression()

# ---------------------------------------
# 6. Pipeline (Preprocessing + Model)
# ---------------------------------------
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# ---------------------------------------
# 7. Train Model
# ---------------------------------------
pipeline.fit(X_train, y_train)

print("Model training completed")

# ---------------------------------------
# 8. Evaluate Model
# ---------------------------------------
y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Evaluation:")
print(f"MAE  : ₹{int(mae)}")
print(f"RMSE : ₹{int(rmse)}")

# ---------------------------------------
# 9. Save Model
# ---------------------------------------
joblib.dump(pipeline, "rent_model.pkl")

print("\nModel saved as rent_model.pkl")
