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
    i=i.split(".")[0]
    if len(i) < 9:
        pass
    elif len(i) > 14:
        i= i[0:13]
    elif ken.fullmatch(i, 0,4) != None:
        pass
    else:
        data.append(i)


# Check numbers repeating more than 2 times add them to an array
from collections import Counter
counts = dict(Counter(data))

emp_file= os.path.join(".", "Numbers", "Employers.txt")
client_file = os.path.join(".", "Numbers", "Clients.txt")

def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if str(string_to_search) in line:
                return True
    return False


sort = sorted(counts.items(), key=lambda x:x[1], reverse=True)

for i in sort:
    if check_if_string_in_file(emp_file, i[0]) == True:
        pass
    elif i[1] > 3:
        with open(emp_file, 'a+', encoding="utf-8") as f:
            f.write(f"{i[0]}\n")
            f.close()
    else:
        with open(client_file, 'a+', encoding="utf-8") as f:
            if check_if_string_in_file(client_file, i[0]) == True:
                pass
            else:
                f.write(f"{i[0]}\n")
                f.close()








