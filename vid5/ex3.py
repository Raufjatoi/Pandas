import pandas as pd

# Creating a DataFrame with datetime data type
data = {
    'Date': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01']),
    'Value': [100, 200, 300]
}

df = pd.DataFrame(data)
print(df['Date'].dt.year)  # Extracting year from datetime
