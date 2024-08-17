import pandas as pd

# Creating a DataFrame with different data types
data = {
    'Integer': [1, 2, 3],
    'Float': [1.1, 2.2, 3.3],
    'String': ['a', 'b', 'c'],
    'Boolean': [True, False, True],
    'Date': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01'])
}

df = pd.DataFrame(data)

print(df.dtypes)
