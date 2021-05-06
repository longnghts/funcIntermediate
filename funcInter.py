#1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 30} ]


#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
	for x in list:
		print(f'first_name - {x["first_name"]}, last_name - {x["last_name"]}')
iterateDictionary(students)		

#3
def iterateDictionary2(value, lists):
	for x in lists:
		print(x[value])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictOfList):
    for x in dictOfList:
        length1 = (len(dictOfList[x]))
        print(f'{length1} {x}')
        for y in dictOfList[x]:
            print(y)

printInfo(dojo)