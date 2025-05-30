import numpy as np
import pandas as pd

exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data,labels)

# Write a Pandas program to select the rows where the score is between 15 and 20 (inclusive).

# cond = df["score"].isin(range(15,21)) that would be perfect if score was an int.

cond = (df["score"] >= 15) & (df["score"] <= 20)

cond = df['score'].between(15, 20)

print(df[ cond ])
