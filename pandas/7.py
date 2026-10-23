# Sort a DataFrame by Multiple Columns
import pandas as pd 
dt=pd.DataFrame(
    {
        'name':['mikku','raiden','monna'],
        'age':[5002,3223,232],
        'type':['el','el','el']
    }
)
print(dt.to_string(index=False))
dt=dt.sort_values(by=['name','age'], ascending=[True,True])
print(dt.to_string(index=False))


