import pandas as pd
import statistics as st
df = pd.read_csv('data.csv')
height2 = df['Height(Inches)'].tolist()
mean = st.mean(height2)
std = st.stdev(height2)
ssstd = mean - 2*std
sestd = mean + 2*std
sstd = []
for h in height2:
    if(h>ssstd and h<sestd):
        sstd.append(h)
fp = (len(sstd)/len(height2))*100
print(fp)