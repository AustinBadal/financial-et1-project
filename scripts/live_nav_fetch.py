import requests
import pandas as pd

scheme_codes = {
    "HDFC": 125497,
    "SBI": 119551,
    "ICICI": 120503,
    "NIPPON": 118632,
    "AXIS": 119092,
    "KOTAK": 120841
}

for name, code in scheme_codes.items():
    
    url = f"https://api.mfapi.in/mf/{code}"
    
    response = requests.get(url)
    
    data = response.json()
    
    nav_df = pd.DataFrame(data['data'])
    
    nav_df.to_csv(f"data/raw/{name}_nav.csv", index=False)
    
    print(f"{name} NAV data saved successfully!")