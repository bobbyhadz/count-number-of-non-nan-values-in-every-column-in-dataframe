# Count number of non-NaN values in each column of DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', None, None],
    'experience': [None, 5, None, None],
    'salary': [None, 180.2, 190.3, 205.4],
})

print(df)

print('-' * 50)

print(df.count())