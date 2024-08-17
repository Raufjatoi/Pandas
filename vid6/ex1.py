import pandas as pd

# Create a simple DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Rename columns using the rename method
df.rename(columns={'A': 'Column1', 'B': 'Column2'}, inplace=True)

print(df)
