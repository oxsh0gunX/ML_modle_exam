# To generate a series of dates from 1 May 2021 to 12 May 2021, including both dates.
import pandas as pd
x=pd.Series(pd.date_range('2021-5-01' , '2021-5-12' ,  freq='D'))
print(x)



















