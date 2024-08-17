import pandas as pd

# Create two DataFrames with a common key
df1 = pd.DataFrame({'key': [1, 2], 'value1': ['A', 'B']})
df2 = pd.DataFrame({'key': [1, 2], 'value2': ['C', 'D']})

# Merge the DataFrames based on the 'key' column
merged_df = df1.merge(df2, on='key')

print(merged_df)
