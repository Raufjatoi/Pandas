import pandas as pd
import numpy as np
# Creating a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': ['x', 'y', 'z', np.nan]
}
df = pd.DataFrame(data)

# Filling missing values with a specific value
df_filled_value = df.fillna(value={'A': 0, 'B': 0, 'C': 'unknown'})

print("\nDataFrame after filling missing values with specific values:")
print(df_filled_value)

# Forward filling missing values
df_filled_ffill = df.fillna(method='ffill')

print("\nDataFrame after forward filling missing values:")
print(df_filled_ffill)

# Backward filling missing values
df_filled_bfill = df.fillna(method='bfill')

print("\nDataFrame after backward filling missing values:")
print(df_filled_bfill)
