import numpy as np
df = np.loadtxt('./Day-1_Sonar-Sweep.txt')
#df = np.loadtxt('./Day-1_Sonar-Sweep-example.txt')
p = 0
inc = 0
for x in range(len(df)):
    e = (int)(df[x])
    if (e > p and p > 0):
        inc = inc + 1
    p = e
print("The result:", inc)
