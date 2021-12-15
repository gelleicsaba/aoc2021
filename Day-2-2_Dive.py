#with open("Day-2_Dive!-example.txt", "r") as f:
with open("Day-2_Dive!.txt", "r") as f:
    df = f.readlines()
h = 0
d = 0
a = 0
for x in range(len(df)):
    e = (str)(df[x]).strip().split(' ')
    c = (str)(e[0])
    v = (int)(e[1])
    if (c[0] == 'f'):
        h = h + v
        d = d + a * v
    elif (c[0] == 'd'):
        a = a + v
    elif (c[0] == 'u'):
        a = a - v
print("The result:", (h * d))



