import pandas as pd
from sqlalchemy import create_engine

# =======================================
# CREATED SQLITE DATABASE
# =======================================

engine = create_engine("sqlite:///bluestock_mf.db")
print("Database created Successfully!..")

# ========================================
# LOAD FUND MASTER
# ========================================

fund_df = pd.read_csv("data/raw/01_fund_master.csv")

fund_df.to_sql(
        "dim_fund",
        engine,
        if_exists="replace",
        index=False
)

print("dim_fund table loaded!")

# LOAD CLEAN NAV DATA

nav_df = pd.read_csv("data/processed/clean_nav_history.csv")

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# Load Clean Transaction Data

trans_df = pd.read_csv("data/processed/clean_investor_transactions.csv")

trans_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions table loaded!")

#Load clean performance data

perf_df = pd.read_csv("data/processed/clean_scheme_performance.csv")

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance table loaded")

print("ALL Data Loaded Successfully..")