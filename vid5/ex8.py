import pandas as pd
import numpy as np
# Creating a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': ['x', 'y', 'z', np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:")

# Dropping rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)


