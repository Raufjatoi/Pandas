import pandas as pd

# Creating a DataFrame with category data type
data = {
    'Category': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)
df['Category'] = df['Category'].astype('category')

print(df.dtypes)
print(df['Category'].cat.categories)
