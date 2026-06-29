#.................Day 3 - Lists, Tuples and Sets..............
print("Learn Sets......")
#Set will now follow any order. It will print random but it will not allow duplicate
courses = {'Engineering','Computer Science','Mathematics','History','Physics'}
courses2 = {'Engineering','Computer Science','Mathematics','History','Physics','Chemistry','Art'}
# print(courses)

print(courses.intersection(courses2)) # common in both sets
print(courses.union(courses2))#combine the both set and will print without repeat
print(courses.difference(courses2))

#empty set
empty_set = set()
