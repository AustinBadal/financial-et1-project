import pandas as pd

# =========================
# CLEAN NAV HISTORY
# =========================

print("Cleaning NAV History Dataset...")

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column into datetime format
nav_df['date'] = pd.to_datetime(nav_df['date'])

# Sort values
nav_df = nav_df.sort_values(by=['amfi_code', 'date'])

# Remove duplicate rows
nav_df = nav_df.drop_duplicates()

# Forward fill missing NAV values
nav_df['nav'] = nav_df['nav'].ffill()

# Keep only positive NAV values
nav_df = nav_df[nav_df['nav'] > 0]

# Save cleaned dataset
nav_df.to_csv("data/processed/clean_nav_history.csv", index=False)

print("NAV History Cleaned Successfully!")



# =========================
# CLEAN INVESTOR TRANSACTIONS
# =========================

print("Cleaning Investor Transactions Dataset...")

trans_df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
trans_df['transaction_type'] = trans_df['transaction_type'].str.upper()

# Keep only positive transaction amounts
trans_df = trans_df[trans_df['amount_inr'] > 0]

# Convert transaction date
trans_df['transaction_date'] = pd.to_datetime(trans_df['transaction_date'])

# Remove duplicates
trans_df = trans_df.drop_duplicates()

# Save cleaned dataset
trans_df.to_csv("data/processed/clean_investor_transactions.csv", index=False)

print("Investor Transactions Cleaned Successfully!")



# =========================
# CLEAN SCHEME PERFORMANCE
# =========================

print("Cleaning Scheme Performance Dataset...")

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Validate expense ratio range
perf_df = perf_df[
    (perf_df['expense_ratio_pct'] >= 0.1) &
    (perf_df['expense_ratio_pct'] <= 2.5)
]

# Remove duplicates
perf_df = perf_df.drop_duplicates()

# Save cleaned dataset
perf_df.to_csv("data/processed/clean_scheme_performance.csv", index=False)

print("Scheme Performance Cleaned Successfully!")