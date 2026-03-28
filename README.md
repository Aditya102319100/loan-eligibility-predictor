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
<img width="1811" height="857" alt="Screenshot 2026-03-28 073549" src="https://github.com/user-attachments/assets/0549d26c-c57c-42be-97e9-08be5a2c2ceb" />
<img width="1787" height="866" alt="Screenshot 2026-03-28 073612" src="https://github.com/user-attachments/assets/0bddbcce-2f31-4bdd-969b-5bd02587e92b" />
<img width="1508" height="724" alt="Screenshot 2026-03-28 073642" src="https://github.com/user-attachments/assets/72bd16a6-e130-411e-9e32-fc45db0b3f1e" />
<img width="1870" height="857" alt="Screenshot 2026-03-28 073711" src="https://github.com/user-attachments/assets/6a9c53fd-65b6-48f2-94cf-a3e028c8e7e4" />
<img width="1384" height="744" alt="Screenshot 2026-03-28 073653" src="https://github.com/user-attachments/assets/e6c4b3f9-8555-45f6-aafd-cece7b48dc6d" />
<img width="1878" height="873" alt="Screenshot 2026-03-28 073728" src="https://github.com/user-attachments/assets/88317ee3-8818-408a-bfe9-f833f41e942a" />

