s = input().strip()

for i in ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]:
    s = s.replace(i, "*")  

print(len(s))