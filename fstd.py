import pandas as pd
import statistics as st
df = pd.read_csv('data.csv')
height = df[('Height(Inches)')].tolist()
mean = st.mean(height)
std = st.stdev(height)
fsstd = mean - std
festd = mean + std
fstd = []
for h in height:
    if(h<festd and h>fsstd):
        fstd.append(h)
fp = (len(fstd)/len(height))*100
print(fp)
