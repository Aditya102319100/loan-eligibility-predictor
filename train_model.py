import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
df = pd.read_csv("loan_data.csv")

# X = inputs, y = output (eligible or not)
X = df[["income", "credit_score", "employed", "loan_amount"]]
y = df["eligible"]

# Split: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define all 3 models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree":       DecisionTreeClassifier(),
    "Random Forest":       RandomForestClassifier(n_estimators=100)
}

best_model = None
best_accuracy = 0

# Train each model and check accuracy
for name, model in models.items():
    model.fit(X_train, y_train)           # Train
    preds = model.predict(X_test)         # Test
    acc = accuracy_score(y_test, preds)   # Check accuracy
    print(f"{name}: {acc * 100:.2f}%")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model

# Save the best model to a file
with open("best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print(f"\n✅ Best model saved with {best_accuracy * 100:.2f}% accuracy!")