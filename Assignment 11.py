import re
x = list()
fh = open("venv/question.txt", "r")
for line in fh:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    for number in y:
        x.append(float(number))
print(sum(x))