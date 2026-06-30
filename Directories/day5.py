# Dictionaries.......
# Key-Value pair

student = {'name':'Jhon',
           'age': 25,
           'courses':['Maths','Physics','Chemistry']}
print(student)
print((student.get('name')))
print(student['name'])
print(student['courses'])
student.update({'name':'Jane','age':28,'phone':'555-5555'})

print(student['courses'][1])

del student['name']
age = student.pop('age')
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key,value in student.items():
    print(key,value)