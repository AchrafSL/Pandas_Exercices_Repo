import numpy as np
import pandas as pd

data = {
    'col1':np.random.randint(0,9,size = 5),
    'col2':np.random.randint(0,9,size = 5),
    'col3':np.random.randint(0,9,size = 5)
}


# Create DataFrame
df = pd.DataFrame(data)


#Start Coding Here

# Write a Pandas program to change the order of a DataFrame columns.
print(df,"\n")

df = df[['col3', 'col2', 'col1']]
print(df)


