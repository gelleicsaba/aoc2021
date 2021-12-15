import numpy as np
df = np.loadtxt('./Day-1_Sonar-Sweep.txt')
#df = np.loadtxt('./Day-1_Sonar-Sweep-example.txt')
p = 0
inc = 0
for x in range(len(df)-2):
    e1 = (int)(df[x])
    e2 = (int)(df[x+1])
    e3 = (int)(df[x+2])
    y = e1 + e2 + e3
    if (y > p and p > 0):
        #print("I")
        inc = inc + 1
    p = y
print("The result:", inc)
