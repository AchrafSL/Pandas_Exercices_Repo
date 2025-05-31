import numpy as np
import pandas as pd

exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]


# Create DataFrame
df = pd.DataFrame(exam_data)


#Start Coding Here
print(df)

for k,v in df.values:
    print(k,v)