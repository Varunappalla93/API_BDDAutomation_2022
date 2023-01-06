import json

'''
# parsing json string to dict
courses = '{"name":"Varun","languages":["Java","Python"]}'

dict_courses = json.loads(courses)  # to convert to dict
print(type(dict_courses)) # <class 'dict'>

print(dict_courses) # {'name': 'Varun', 'languages': ['Java', 'Python']}


print(dict_courses["languages"][1]) # Python
'''

# parse json content present in external file
with open("C:\\Users\\VARUN\\Desktop\\Varun_Personal\\API_BDDAutomation_2022\\JsonParsers\\courses.json") as f:
    jsonfile_dict = json.load(f)
    print(jsonfile_dict)  # json data in dict format
    print(type(jsonfile_dict))  # <class 'dict'>
    print(jsonfile_dict['courses'][1]['title'])  # Cypress
    print(jsonfile_dict['dashboard'])  # {'purchaseAmount': 910, 'website': 'rahulshettyacademy.com'}
    print(type(jsonfile_dict['dashboard']))  # <class 'dict'>
    print(jsonfile_dict['dashboard']['website'])

    # get price of course RPA
    courseslist = jsonfile_dict['courses']
    print(type(courseslist))  # <class 'list'>
    print(courseslist)

    for course in courseslist:
        print(course)
        if course['title'] == "RPA":
            print("RPA Price is", course["price"])
            assert course["price"] == 45

# {'title': 'Selenium Python', 'price': 50, 'copies': 6}
# {'title': 'Cypress', 'price': 40, 'copies': 4}
# {'title': 'RPA', 'price': 45, 'copies': 10}
# RPA Price is 45
