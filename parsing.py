from io import StringIO
import pandas as pd


output = """This is version 0.01 of a parser test file
header information 1: 14
too good to be true: 80%

    u   k   r
  1.1 0.6 1.2
    9 2.3  10
"""

params = dict()
data = []
linecount = 0

with StringIO(output) as f:
    for line in f:
        linecount += 1
        s = [_.strip() for _ in line.split(":")]
        if linecount > 1:
            if len(s) == 1:
                s = line.split()
                if len(s):
                    data.append(s)
            else:
                try:
                    params[s[0]] = int(s[1])
                except:
                    try:
                        params[s[0]] = float(s[1])
                    except:
                        params[s[0]] = str(s[1])
                    

print(params)
df = pd.DataFrame(data[1:], columns=data[0])
print(df)
k = df.keys()[0]
print('mean of {}: {}'.format(k, df[k].mean()))