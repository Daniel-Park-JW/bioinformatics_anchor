import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

print("Loading Day 1 Matrices...")
# Load the clean CSVs you generated on Wednesday
expr = pd.read_csv('data/GSE10072_expression.csv', index_col=0)
meta = pd.read_csv('data/GSE10072_metadata.csv', index_col=0)

# Align the sample IDs perfectly between the two files
common_samples = expr.columns.intersection(meta.index)
expr = expr[common_samples]
meta = meta.loc[common_samples]

# Isolate the index names for Tumor vs Normal samples
# Note: You may need to change 'disease_state' and 'lung adenocarcinoma' 
# to exactly match the text inside your specific metadata.csv file
tumor_samples = meta[meta['source_name_ch1'] == 'Adenocarcinoma of the Lung'].index
normal_samples = meta[meta['source_name_ch1'] == 'Normal Lung Tissue'].index

expr_tumor = expr[tumor_samples]
expr_normal = expr[normal_samples]

print(f"Processing {len(tumor_samples)} Tumor and {len(normal_samples)} Normal samples...")

# Run T-tests across all 20,000+ genes simultaneously
print("Calculating T-statistics and p-values...")
t_stats, p_values = ttest_ind(expr_tumor, expr_normal, axis=1, nan_policy='omit')

# Apply Benjamini-Hochberg FDR correction to prevent false positives
print("Applying False Discovery Rate (FDR) correction...")
reject, q_values, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')

# Create a complete statistical summary dataframe
stats_df = pd.DataFrame({
    't_statistic': t_stats,
    'p_value': p_values,
    'q_value': q_values,
    'significant': reject
}, index=expr.index)

# FEATURE ENGINEERING: Drop the useless genes, keep only the significant ones
significant_genes = stats_df[stats_df['significant'] == True].index
X_matrix = expr.loc[significant_genes].T  # Transposed so rows=samples, columns=features
y_vector = meta['source_name_ch1']

# Save the ML-ready outputs
X_matrix.to_csv('data/ML_ready_X.csv')
y_vector.to_csv('data/ML_ready_y.csv')
stats_df.to_csv('data/differential_expression_stats.csv')

print(f"Pipeline Complete. Filtered down to {len(significant_genes)} predictive features.")
print("Outputs saved: ML_ready_X.csv, ML_ready_y.csv")