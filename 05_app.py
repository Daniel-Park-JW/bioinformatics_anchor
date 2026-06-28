import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Setup the Web Page
st.set_page_config(page_title="Lung Cancer AI", layout="wide")
st.title("🧬 Lung Adenocarcinoma Prediction App")
st.write("""
This interactive web application deploys a Machine Learning algorithm (Random Forest) trained on transcriptomic microarray data. 
It uses the top 10 most predictive genetic biomarkers discovered in our automated pipeline to instantly classify tissue samples.
""")

# 2. Data Loading & Model Training (Cached so the app runs lightning fast)
@st.cache_resource
def load_and_train():
    # Load the data generated from our previous pipeline steps
    X = pd.read_csv('data/ML_ready_X.csv', index_col=0)
    y = pd.read_csv('data/ML_ready_y.csv', index_col=0).iloc[:, 0]
    top_genes = pd.read_csv('data/top_predictive_genes.csv', index_col=0)
    
    # Filter to just the top 10 biomarkers so we can build UI sliders for them
    top_features = top_genes.index.tolist()
    X_reduced = X[top_features]
    
    # Train the Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_reduced, y)
    
    return model, top_features, X_reduced, y.unique()

model, top_features, X_reduced, classes = load_and_train()

# 3. Build the Sidebar (User Input)
st.sidebar.header("Input Patient Biomarkers")
st.sidebar.write("Adjust the gene expression levels below to simulate a patient's microarray readout:")

# Dynamically generate a slider for each of the 10 genes based on real dataset minimums and maximums
user_inputs = {}
for feature in top_features:
    min_val = float(X_reduced[feature].min())
    max_val = float(X_reduced[feature].max())
    mean_val = float(X_reduced[feature].mean())
    user_inputs[feature] = st.sidebar.slider(f"Gene: {feature}", min_value=min_val, max_value=max_val, value=mean_val)

# 4. Prediction Logic
st.write("---")
st.subheader("Diagnostic Prediction")

if st.sidebar.button("Run AI Prediction", type="primary"):
    # Convert user inputs into a format the model understands
    input_df = pd.DataFrame([user_inputs])
    
    # Get prediction and probabilities
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    
    # Map probabilities to classes
    tumor_prob = probabilities[list(model.classes_).index("Adenocarcinoma of the Lung")]
    normal_prob = probabilities[list(model.classes_).index("Normal Lung Tissue")]
    
    # 5. Display Results
    if prediction == "Adenocarcinoma of the Lung":
        st.error(f"**AI Diagnosis:** {prediction}")
    else:
        st.success(f"**AI Diagnosis:** {prediction}")
        
    st.write(f"**Confidence Metrics:**")
    st.write(f"- Adenocarcinoma Probability: **{tumor_prob * 100:.1f}%**")
    st.write(f"- Normal Tissue Probability: **{normal_prob * 100:.1f}%**")
else:
    st.info("👈 Adjust the biomarker sliders in the sidebar and click 'Run AI Prediction' to see the results.")