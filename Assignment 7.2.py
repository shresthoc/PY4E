#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values
#and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

count = 0
addition = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x=line.find('0')
    number = float(line[x:])
    count = count + 1
    addition = addition + number
avg = addition/count
print('Average spam confidence:', avg)

#OR

count = 0
addition = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    number = float(line[20:])
    count = count + 1
    addition = addition + number
avg = addition/count
print('Average spam confidence:', avg)
#The second method is working because the position of the "0" is the same on every line i.e. 20. IF it was different, then the
#second method would fail but the first method would still work.