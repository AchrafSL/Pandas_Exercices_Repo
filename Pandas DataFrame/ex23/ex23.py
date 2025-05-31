import numpy as np
import pandas as pd

data = {
    'col1':np.random.randint(0,9,size = 3),
    'col2':np.random.randint(0,9,size = 3),
    'col3':np.random.randint(0,9,size = 3)
}


# Create DataFrame
df = pd.DataFrame(data)


#Start Coding Here
# Write a Pandas program to rename columns of a given DataFrame

df.columns = ['Column1','Column2','Column3']
print(df)


