#-----------------------------------------#
# -- Loop on many Iterators with zip() --
#-----------------------------------------#
#   zip()   Return a zip Object contains all Objects
#   zip()   Length is the Length of the lowest Object

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {'name': 'Ahmad', "age": 28, "country": "Syria", "skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print(f"List 1 item => {item1}")
    print(f"List 2 item => {item2}")
    print(f"Tuple 1 item => {item3}")
    print(f"Dictionary 1 Key => {item4} - it's Value => {dict1[item4]}")

# ultimateList = zip(list1, list2)
# print(ultimateList)
# for item in ultimateList:
#     print(item)