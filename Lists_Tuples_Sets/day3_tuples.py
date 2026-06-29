#.................Day 3 - Lists, Tuples and Sets..............
from Lists_Tuples_Sets.day3_lists import empty_list

print("Learn Tuples......")
print("We can not change the value in Tuples... eg - tuple = ('A','B','C')")
# courses = ['Engineering','Computer Science','Mathematics','History','Physics','Chemistry']
# courses2 = courses
# print(courses)
# print(courses2)
# courses[0] = 'Art'
# print(courses)
# print(courses2)

tuples_1 = ('Engineering','Computer Science','Mathematics','History','Physics','Chemistry')
tuples_2 = tuples_1

print(tuples_1)
print(tuples_2)
tuples_1[0] = 'Art'
print(tuples_1)
print(tuples_2)

#empty tuples
empty_tuple = ()
empty_tuple = tuple()