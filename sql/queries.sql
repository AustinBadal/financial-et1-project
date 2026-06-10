-- QUERYING THE DATABASE CREATED

-- TOP 10 FUNDS BY 5 YEAR RETURN

SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- AVERAGE NAV BY FUND

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- TOTAL TRANSACTION AMOUNT BY STATE

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- TOP FUNDS BY SHARPE RATIO

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- TOTAL TRANSACTIONS BY TRANSACTION TYPE

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;