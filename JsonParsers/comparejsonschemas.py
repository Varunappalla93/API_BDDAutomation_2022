import json
# convert to dict using load and compare dicts
with open("courses.json") as f1:
    courses=json.load(f1)
    print(courses)


with open("courses2.json") as f2:
    courses2=json.load(f2)
    print(courses2)

print(courses==courses2) # False as both contents are different
assert courses==courses2 # AssertionError
