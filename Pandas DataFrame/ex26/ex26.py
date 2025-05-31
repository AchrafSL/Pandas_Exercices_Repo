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

df.loc['5'] = np.random.randint(0,9,size = 3)
print(df)
