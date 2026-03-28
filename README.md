# loan-eligibility-predictor
🏦 AI-Powered Loan Eligibility System
An End-to-End Machine Learning Web Application

📖 Project Overview

This project is a high-performance Loan Eligibility Prediction System that bridges the gap between raw data science and modern web design. By analyzing key financial indicators—Income, Credit Score, Employment Status, and Loan Amount—the system provides a real-time assessment of an applicant's eligibility.


Key Highlights
Automated ML Pipeline: Evaluates multiple algorithms and deploys the highest-performing model automatically.
85% Prediction Accuracy: Optimized using ensemble learning methods.
Professional FinTech UI: A sleek, responsive neon-dark themed interface designed for optimal user experience.


1. Technical Architecture
The system is built using a modular "Data-to-UI" approach:
Data Layer: Managed with pandas for cleaning and preprocessing the loan_data.csv dataset.
Logic Layer: A Python-based training engine that pits Logistic Regression, Decision Trees, and Random Forests against each other.
Persistence Layer: The winning model is serialized using pickle for instant loading
Presentation Layer: A modern frontend (HTML5/CSS3/JS) that visualizes the results and model statistics.


2. Machine Learning Deep Dive
In the train_model.py script, the project performs a "Battle of the Models" to ensure maximum reliability.
Models Evaluated:
Logistic Regression: Established a mathematical baseline for linear probability.
Decision Tree: Captured non-linear decision boundaries through recursive partitioning.
Random Forest (The Winner): An ensemble method utilizing 100 decision trees to reduce variance and minimize overfitting.


3. Repository Structure
├── data/
│   └── loan_data.csv        # Financial training dataset
├── src/
│   ├── train_model.py       # ML training & model selection logic
│   ├── predict.py           # CLI-based real-time predictor
│   └── best_model.pkl       # The serialized "winning" model
├── web/
│   ├── index.html           # Main UI / Calculator interface
│   └── style.css            # Custom neon-dark theme styling        
└── README.md                # In-depth project documentation

4. Quick Start
Install: pip install pandas scikit-learn
Train: Run python train_model.py to generate best_model.pkl.
Test: Run python predict.py to check eligibility via terminal.


5. Key Features of the UI
Based on the implementation, the web interface includes:
Interactive Input Controls: Credit score sliders and employment toggles for effortless data entry.
Model Comparison Cards: Displays the accuracy and logic types for all evaluated models.
Instant Result Feedback: Dynamic color-coded alerts (✅ Approved / ❌ Rejected) based on model output.

