import os
import GEOparse

# 1. Define where the downloaded data will live
# It is best practice to keep raw data separate from your code
DATA_DIR = "./data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 2. Download the GSE10072 dataset
print("Connecting to NCBI GEO database...")
print("Downloading GSE10072 (This is a large file, it may take a few minutes)...")

# GEOparse automatically connects to the server, downloads the .soft file, 
# and parses it into a Python object we can manipulate.
try:
    gse = GEOparse.get_GEO(geo="GSE10072", destdir=DATA_DIR)
    
    # 3. Verify it worked by printing some basic metadata
    print("\n✅ Download and Parsing Complete!")
    print(f"Dataset Title: {gse.metadata.get('title', ['Unknown'])[0]}")
    print(f"Number of Patient Samples: {len(gse.gsms)}")
    
    # 4. Extract the Expression Matrix
    print("\nTranslating raw data into an Expression Matrix...")
    # pivot_samples('VALUE') aligns all the RNA readouts into a perfect grid
    expression_matrix = gse.pivot_samples('VALUE')
    
    # 5. Extract the Metadata (which patient has cancer vs. healthy)
    print("Extracting Metadata...")
    metadata = gse.phenotype_data
    
    # 6. Save them as clean CSV files to your hard drive
    expression_matrix.to_csv(os.path.join(DATA_DIR, "GSE10072_expression.csv"))
    metadata.to_csv(os.path.join(DATA_DIR, "GSE10072_metadata.csv"))
    print("✅ Matrix translation complete. Files saved as CSVs!")
    
except Exception as e:
    print(f"\n❌ Error downloading dataset: {e}")
    print("Check your internet connection or try again in a few minutes.")