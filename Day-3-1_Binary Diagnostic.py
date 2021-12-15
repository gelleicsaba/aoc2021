with open("./Day-3_Binary Diagnostic.txt", "r") as f:
#with open("./Day-3_Binary Diagnostic-example.txt", "r") as f:
    df = f.readlines()
h = len(df[0].strip())
dl = len(df)
r = [0] * h
for x in range(dl):
    s = df[x].strip()
    for y in range(h):
        if (s[y] == '1'):
            r[y] = r[y] + 1
e = 1
gr = 0
er = 0
d2 = (int)(dl / 2)
for y in range(h):
    y = h - y - 1
    if (r[y] > d2):
        gr = gr + e
    else:
        er = er + e
    e = 2 * e
print("The result:", gr * er)
