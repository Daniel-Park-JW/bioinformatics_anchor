import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load the ML-ready data
X = pd.read_csv('data/ML_ready_X.csv', index_col=0)
y = pd.read_csv('data/ML_ready_y.csv', index_col=0).iloc[:, 0]

# 2. Split the data into Training (80%) and Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the Random Forest Classifier
print("Training the Random Forest model on 10,891 features...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluate the model
predictions = model.predict(X_test)
print("\n--- Model Performance Report ---")
print(classification_report(y_test, predictions))

# 5. Extract the "Top Predictors" (The most important biomarkers)
importances = pd.Series(model.feature_importances_, index=X.columns)
top_genes = importances.nlargest(10)

print("\n--- Top 10 Predictive Biomarkers (Affymetrix Probe IDs) ---")
print(top_genes)

# Save the model results
top_genes.to_csv('data/top_predictive_genes.csv')
print("\n✅ Top predictive biomarkers saved to data/top_predictive_genes.csv")