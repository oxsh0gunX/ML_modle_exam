import pandas as pd
hi=pd.read_csv('hi.csv')
print(hi.to_string(index=False))