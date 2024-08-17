import pandas as pd

# Create a simple DataFrame with custom index
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# Rename columns and index
df.rename(columns={'A': 'Column1', 'B': 'Column2'}, index={'x': 'row1', 'y': 'row2', 'z': 'row3'}, inplace=True)

print(df)
