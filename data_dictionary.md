# Data Dictionary

## dim_fund

| Column Name | Description                   |
| ----------- | ----------------------------- |
| amfi_code   | Unique AMFI scheme identifier |
| scheme_name | Name of mutual fund scheme    |
| fund_house  | Fund management company       |
| category    | Mutual fund category          |
| plan        | Growth/Dividend plan type     |

## fact_nav

| Column Name | Description        |
| ----------- | ------------------ |
| amfi_code   | AMFI scheme code   |
| date        | NAV reporting date |
| nav         | Net Asset Value    |

## fact_transactions

| Column Name      | Description                |
| ---------------- | -------------------------- |
| investor_id      | Unique investor identifier |
| transaction_date | Transaction date           |
| transaction_type | SIP/Lumpsum/Redemption     |
| amount_inr       | Transaction amount         |
| state            | Investor state             |
| city             | Investor city              |

## fact_performance

| Column Name       | Description                  |
| ----------------- | ---------------------------- |
| return_1yr_pct    | 1-year return percentage     |
| return_3yr_pct    | 3-year return percentage     |
| return_5yr_pct    | 5-year return percentage     |
| sharpe_ratio      | Risk adjusted return metric  |
| alpha             | Excess return over benchmark |
| beta              | Market sensitivity           |
| expense_ratio_pct | Fund expense ratio           |
