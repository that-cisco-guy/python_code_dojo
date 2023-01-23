# Basic
for i in range(151):
    print(i)
# Mult of 5
for i in range(5,1001,5):
    print(i)
# Dojo Way
for i in range(101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
# Huge!
count = 0
for i in range(500001):
    if i % 2 != 0:
        count = count + 1
print(count)
# Countdown
for i in range(2018,0,-4):
    print(i)
# Flex Counter
lowNum = 5
highNum = 50
mult = 2
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)