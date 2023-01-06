import requests
from APITestingRequests.payload import *
from Utilities.Resources import Resource
from Utilities.configurations import getconfig

# base uri comes from configurations file from getconfig() method

# for constructing url using base uri end point and resources
addbookurl=getconfig()['API']['endpoint']+Resource.addbook

# for headers
headers={"Content-Type": "application/json;charset=UTF-8"}

query = 'select * from Books'

# we can add cookies and headers for Post, json for sending our payload.
# bring json payload from db now instead of hardcoding from payload file
# addbookresp = requests.post(addbookurl, json=buildPayLoadFromDB(query),headers=headers,)

# from addbookpayload method(isbn)
addbookresp = requests.post(addbookurl, json=addbookpayload('fefe'),headers=headers,)

print(addbookresp.text)  # {'Msg': 'successfully added', 'ID': 'xytzr008'}
print(type(addbookresp.text))  # <class 'str'>

print(addbookresp.status_code)  # 200
# assert addbookresp.status_code==200

print(addbookresp.headers)
# {'Date': 'Thu, 15 Jul 2021 07:26:58 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST'}


# use json() instead of loads to convert to dict/list if list is already present.
addbookjson = addbookresp.json()

print(addbookjson)  # {'Msg': 'successfully added', 'ID': 'xytzr008'}
print(type(addbookjson))  # <class 'dict'>

print(addbookjson['Msg'])  # successfully added

bookid = addbookjson['ID']
print(bookid)  # tert123

# Delete added book
deletebookurl=getconfig()['API']['endpoint']+Resource.deletebook

delebookresp = requests.post(deletebookurl, json={
    "ID": bookid}, headers={"Content-Type": "application/json"}, )

print(delebookresp.text)  # {"msg":"book is successfully deleted"}

# convert to dict/list using json()
delbookjson = delebookresp.json()

print(delebookresp.status_code)  # 200
assert delebookresp.status_code == 200

print(delbookjson['msg'])  # book is successfully deleted
assert delbookjson['msg'] == 'book is successfully deleted'
