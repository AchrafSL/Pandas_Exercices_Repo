import numpy as np
import pandas as pd

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame
df = pd.DataFrame(exam_data, labels)


#Start Coding Here

# Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
df['qualify'] = df['qualify'].map({'yes':True,'no':False })
df['qualify'] = df['qualify'].replace({'yes':True,'no':False })

print(df)