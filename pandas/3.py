# To create a Pandas DataFrame using a dictionary.
import pandas as pd 
d={
    'name':['tester','hy']
   ,
   'tester':['thega','testering']
   }
print(d)
x=pd.DataFrame(d)
print(x) 

