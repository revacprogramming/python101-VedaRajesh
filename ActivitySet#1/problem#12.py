# Regular Expressions
fname="number.txt"
fhand = open(fname)
sum = 0
for line in fhand:
    print(line,sum)
    for i in line.split():
        if(i.isdigit()):
            sum += int(i)
    print(sum)
    input()
print(sum)
