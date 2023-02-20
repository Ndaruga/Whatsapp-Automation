import pandas as pd
import re
import os

'''Read and transform data'''

data = pd.read_excel("Numbers/Phone_Numbers.xlsx")
data=data.T.reset_index()
df=pd.Series(data.values.ravel("C"))

# Remove null values
df=df.dropna()


data = []

ken = re.compile("254[17]")
for i in pd.Series.iteritems(df):
    i=str(i[1])
#     i=re.sub(' ','',i)
    i=re.sub('[A-Z a-z(-)-+=":_"<>/]','',i)
#     i=int(i)
    if len(i) < 9:
        pass
    
    elif len(i) > 14:
        i= i[0:13]
    elif ken.fullmatch(i, 0,4) != None:
        pass
    else:
        data.append(i)

'''Create files'''
if not os.path.exists(os.path.join("Numbers", "Employers.txt")):
    file = open(os.path.join("Numbers", "Employers.txt"), "w+")
    file.close()

if not os.path.exists(os.path.join("Numbers", "Clients.txt")):
    file = open(os.path.join("Numbers", "Clients.txt"), "w+")
    file.close()

# Check numbers repeating more than 2 times add them to an array
from collections import Counter

counts = dict(Counter(data))

for key, value in counts.items():
    if value > 2:
        with open(os.path.join("Numbers", "Employers.txt"), 'a', encoding="utf-8") as f:
            f.write(f"{key}\n")
            f.close()
    else:
        with open(os.path.join("Numbers", "Clients.txt"), 'a', encoding="utf-8") as f:
            f.write(f"{key}\n")
            f.close()








