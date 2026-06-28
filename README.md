Transcriptomic Biomarker Discovery Pipeline: Lung Adenocarcinoma

Overview

This repository contains an automated, end-to-end bioinformatics pipeline designed to identify predictive genetic biomarkers for lung adenocarcinoma.

Using raw microarray data from the National Center for Biotechnology Information (NCBI GEO), this pipeline performs data ingestion, statistical feature selection, dimensionality reduction, and trains a Machine Learning classifier to distinguish between tumor and normal lung tissue.

Project Architecture

The analysis is broken down into four modular, reproducible Python scripts:

01_ingest.py: Programmatically queries the NCBI server to download the GSE10072 microarray dataset. Parses the raw .soft files and extracts the expression matrix and clinical metadata.

02_statistics.py: Performs differential gene expression analysis. Calculates Welch's T-statistics for over 22,000 features and applies the Benjamini-Hochberg False Discovery Rate (FDR) correction to isolate statistically significant genes.

03_visualizations.py: Generates publication-grade mathematical visualizations:

Volcano Plot: Visualizes the trade-off between statistical significance and biological effect size.

PCA Plot: Performs Principal Component Analysis to prove the selected features mathematically separate the clinical states into distinct clusters.

04_machine_learning.py: Trains a Random Forest Classifier on the filtered expression matrix. Achieves high predictive accuracy on a withheld testing set and extracts the top 10 most predictive Affymetrix probe IDs (biomarkers).

Data Source

Dataset: GSE10072

Platform: Affymetrix Human Genome U133A Array

Samples: 58 Lung Adenocarcinoma, 49 Normal Lung Tissue

Technologies Used

Languages: Python, Bash

Environment: Linux (WSL), Virtual Environments (venv)

Core Libraries: pandas, scipy, scikit-learn, matplotlib, seaborn, GEOparse

Quick Start

To reproduce this analysis locally:

# 1. Clone the repository
git clone [https://github.com/](https://github.com/)[YOUR-USERNAME]/bioinformatics_anchor.git
cd bioinformatics_anchor

# 2. Activate a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy scipy scikit-learn matplotlib seaborn GEOparse

# 3. Run the pipeline sequentially
python 01_ingest.py
python 02_statistics.py
python 03_visualizations.py
python 04_machine_learning.py


Results

The Machine Learning model successfully isolates a predictive genomic signature capable of perfectly separating healthy tissue from adenocarcinoma samples within the testing cohort. The top identified predictive biomarkers are exported to data/top_predictive_genes.csv for downstream pathway analysis and clinical literature review.