import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("TOTAL FUND MASTER CODES:", len(fund_codes))

print("TOTAL NAV HISTORY CODES:", len(nav_codes))

print("MISSING CODES:", len(missing_codes))

print("\nMISSING AMFI CODES:")
print(missing_codes)