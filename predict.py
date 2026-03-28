import pickle

# Load the trained model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

print("\n====== 🏦 Loan Eligibility Predictor ======\n")

# Ask user for inputs
income       = float(input("Enter your annual income (₹): "))
credit_score = int(input("Enter your credit score (300–900): "))
employed     = int(input("Are you employed? (1=Yes, 0=No): "))
loan_amount  = float(input("Enter loan amount requested (₹): "))

# Make prediction
result = model.predict([[income, credit_score, employed, loan_amount]])[0]

# Show result
print("\n" + "="*42)
if result == 1:
    print("✅ Loan APPROVED! You are eligible.")
else:
    print("❌ Loan REJECTED. You are not eligible.")
print("="*42 + "\n")