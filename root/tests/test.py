import pandas as pd


df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
})

print(df)
df = df.iloc[1:].reset_index(drop=True)
print(df)
