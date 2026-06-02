import pandas as pd
import os
folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".csv"):
        path = os.path.join(folder_path, file)
        
        df = pd.read_csv(path)
        print("\n==============================")
        
        print("FILE NAME:", file)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nDUPLICATE ROWS:")
        print(df.duplicated().sum())