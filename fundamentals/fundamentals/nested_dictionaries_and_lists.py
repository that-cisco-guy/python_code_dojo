#1 Udate values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print(x)
print(students)
print(sports_directory)
print(z)

#2 Iterate through a list of dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(my_list):
    for i in range(0,len(my_list)):
        my_dict = ""
        for key, val in my_list[i].items():
            my_dict += f"{key} - {val}"
        print(my_dict)

iterateDictionary(students)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3 Get Values from list of dict
def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        my_dict = some_list[i]
        print(my_dict['first_name'])

iterateDictionary2('first_name', students)

# 4 Iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key,value in some_dict.items():
        print(len(key),key)
        for i in range(0,len(value)):
            print(value[i])


printInfo(dojo)