import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 25]
})

# Group by 'Category' and sum 'Value'
result = df.groupby('Category').sum()

print(result)
