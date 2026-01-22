import joblib
import pandas as pd
import os

# ---------------------------------------
# Load trained model
# ---------------------------------------
MODEL_PATH = "rent_model.pkl"

if not os.path.exists(MODEL_PATH):
    print("❌ Error: rent_model.pkl not found. Train the model first.")
    exit(1)

model = joblib.load(MODEL_PATH)
print("✅ Rent prediction model loaded successfully\n")


# ---------------------------------------
# Take user input
# ---------------------------------------
locality = input("Enter locality (e.g., Dwarka, Rohini, Saket): ").strip()
bhk = input("Enter BHK type (e.g., 1BHK, 2BHK, 3BHK): ").strip()

# ---------------------------------------
# Input validation
# ---------------------------------------
if not locality or not bhk:
    print("❌ Locality and BHK cannot be empty.")
    exit(1)

# ---------------------------------------
# Prepare input for prediction
# ---------------------------------------
input_df = pd.DataFrame([{
    "locality": locality,
    "bhk": bhk
}])

# ---------------------------------------
# Predict rent
# ---------------------------------------
try:
    predicted_rent = model.predict(input_df)[0]
except Exception as e:
    print("❌ Prediction failed:", e)
    exit(1)

# ---------------------------------------
# Output result
# ---------------------------------------
print("\n🏠 Rent Prediction Result")
print("-" * 30)
print(f"Locality : {locality}")
print(f"BHK      : {bhk}")
print(f"Estimated Rent: ₹{int(predicted_rent)} per month")
