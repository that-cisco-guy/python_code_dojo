
#  Countdown
def countdown(num):
    while num > 0:
        print(num)
        num -= 1

countdown(10)

# Print and Return
def printAndReturn(list):
    print(list[0])
    return(list[1])

my_list=[7,11]

printAndReturn(my_list)

# First + Len
def firstPlusLen(list):
    return list[0] + len(list)

my_list=[7,9,2]

firstPlusLen(my_list)

# Values greater than 2nd
def greaterThanSecond(list):
    new_list=[]
    for i in list:
        if i > list[1]:
            new_list.append(i)
    if len(new_list) < 2:
        return('false')
    else:
        print(len(new_list))
    return(new_list)
my_list=[1,2,3,4,5]
my_list2=[1,2,1,1,]
greaterThanSecond(my_list)
greaterThanSecond(my_list2)


# This len that val
def thisLenThatVal(size,value):
    my_list=[]
    while size > 0:
        my_list.append(value)
        size -= 1
    return(my_list)

thisLenThatVal(7,5)
