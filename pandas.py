# Python homework: NumPy and Pandas


# Question 1:
# It can hold data of any type: string, integer, float, dictionaries, lists, booleans, and more.


# You should copy the following code into jupiter_notebook or google colab
# Question 2:

import pandas as pd
month_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
indx = ['January', 'Fabruary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
ddf = pd.Series(month_num, index = indx)
print(ddf)

# Question 3:

import pandas as pd
students = {
    'MatMIE': 40,
    'MatDAIS': 41,
    'COMIE': 40,
    'COMEC': 41
}
dddf = pd.Series(students)
print(dddf)

# Question 4:
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index = labels)
print(df)

# Question 5:
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df1 = pd.DataFrame(exam_data, index=labels)
grater_2 = df1[df1['attempts'] > 2]
print(grater_2)


