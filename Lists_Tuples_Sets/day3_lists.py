#.................Day 3 - Lists, Tuples and Sets..............
from Lists_Tuples_Sets.day3_sets import empty_set

print("Learn Lists......")

courses = ['Engineering','Computer Science','Mathematics','History','Physics','Chemistry']
# courses2 = ['ME','Civil Engineering']
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[0:2])
#
# url = 'https://www.google.com/'
# #reverse
# print(url[::-1])
# courses.append('Computer Engineering')
# courses.insert(1,'EEE')
# courses.insert(0, courses2)
# courses.extend(courses2)
# courses.remove(courses[1])
# courses.pop()
# courses.sort()
# nums = [1,5,15,4,8,9]
# sorted_course = sorted(courses)
# print(sorted_course)
# print(max(nums))

# for index,course in enumerate(courses, start=1):
#     print(index,course)

course_str = ','.join(courses)
new_list = course_str.split(',')
print(course_str)
print(new_list)

#empty list
empty_list= []
empty_set = list()

