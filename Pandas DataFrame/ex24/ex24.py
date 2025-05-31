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
print("Original DataFrame:\n",df)
cond = df['col1'] == 4

print("\nRows for colum1 value == 4:\n",df)
print(df[cond])


