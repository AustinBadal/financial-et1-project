import pandas as pd

performance = pd.read_csv(
    "../data/processed/clean_scheme_performance.csv"
)

risk = input(
    "Enter risk appetite (Low/Moderate/High): "
)

if risk == "Low":
    result = (
        performance[
            performance['risk_grade']
            == 'Low'
        ]
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )

elif risk == "Moderate":
    result = (
        performance[
            performance['risk_grade']
            == 'Moderate'
        ]
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )

else:
    result = (
        performance[
            performance['risk_grade'].isin(
                ['High','Very High']
            )
        ]
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )

print(
    result[
        ['scheme_name',
         'risk_grade',
         'sharpe_ratio']
    ]
)