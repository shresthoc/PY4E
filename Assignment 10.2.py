RIGHT:
name = input("Enter file:")
fh = open(name)
d=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)





WRONG:
name = input("Enter file:")
fh = open(name)
d = dict()
for line in fh:
    line = line.strip()
    if not line.startswith('From '):
        continue
    t = line[5]
    tsplit = t.split[0]
    for time in t:
        if time not in d:
            d[time] = 1
        else:
            d[time] = d[time] + 1
lst = list()
for hour,count in d.items():
    lst.append((hour,count))

lst = sorted(lst)

for hour,count in lst:
    print(hour,count)