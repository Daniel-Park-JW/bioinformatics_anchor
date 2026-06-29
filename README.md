Transcriptomic Biomarker Discovery Pipeline: Lung Adenocarcinoma
**🟢 Live Web App:** [Click here to access the deployed Clinical AI Dashboard](https://gse10072-diagnostic-model.streamlit.app)

Overview

This repository contains an automated, end-to-end bioinformatics pipeline designed to identify predictive genetic biomarkers for lung adenocarcinoma.

Using raw microarray data from the National Center for Biotechnology Information (NCBI GEO), this pipeline performs data ingestion, statistical feature selection, dimensionality reduction, trains a Machine Learning classifier to distinguish between tumor and normal lung tissue, and deploys the resulting model as an interactive web application.

Project Architecture

The analysis is broken down into five modular, reproducible Python scripts:

01_ingest.py: Programmatically queries the NCBI server to download the GSE10072 microarray dataset. Parses the raw .soft files and extracts the expression matrix and clinical metadata.

02_statistics.py: Performs differential gene expression analysis. Calculates Welch's T-statistics for over 22,000 features and applies the Benjamini-Hochberg False Discovery Rate (FDR) correction to isolate statistically significant genes.

03_visualizations.py: Generates publication-grade mathematical visualizations:

Volcano Plot: Visualizes the trade-off between statistical significance and biological effect size.

PCA Plot: Performs Principal Component Analysis to prove the selected features mathematically separate the clinical states into distinct clusters.

04_machine_learning.py: Trains a Random Forest Classifier on the filtered expression matrix. Achieves high predictive accuracy on a withheld testing set and extracts the top 10 most predictive Affymetrix probe IDs (biomarkers).

05_app.py: Deploys a live, interactive web application using Streamlit. Allows users to simulate patient transcriptomic profiles via UI sliders and receive instant, real-time diagnostic predictions (Normal vs. Adenocarcinoma) using the trained 100-tree Random Forest model.

Data Source

Dataset: GSE10072

Platform: Affymetrix Human Genome U133A Array

Samples: 58 Lung Adenocarcinoma, 49 Normal Lung Tissue

Technologies Used

Languages: Python, Bash

Environment: Linux (WSL), Virtual Environments (venv)

Core Libraries: pandas, scipy, scikit-learn, matplotlib, seaborn, GEOparse, streamlit

Quick Start

To reproduce this analysis and launch the web app locally:

# 1. Clone the repository
git clone [https://github.com/Daniel-Park-JW/bioinformatics_anchor.git](https://github.com/Daniel-Park-JW/bioinformatics_anchor.git)
cd bioinformatics_anchor

# 2. Activate a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy scipy scikit-learn matplotlib seaborn GEOparse streamlit

# 3. Run the data pipeline sequentially
python 01_ingest.py
python 02_statistics.py
python 03_visualizations.py
python 04_machine_learning.py

# 4. Launch the interactive clinical dashboard
streamlit run 05_app.py


Results

The Machine Learning model successfully isolates a predictive genomic signature capable of perfectly separating healthy tissue from adenocarcinoma samples within the testing cohort. The top identified predictive biomarkers are exported to data/top_predictive_genes.csv for downstream pathway analysis, and the deployed interactive web interface bridges the gap between raw computational pipelines and real-time clinical utility.