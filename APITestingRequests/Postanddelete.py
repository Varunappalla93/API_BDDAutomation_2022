import requests
from APITestingRequests.payload import *
from Utilities.Resources import Resource
from Utilities.configurations import getconfig

add_book = requests.post(getconfig()['API']['endpoint'] + Resource.addbook,
                         json=addbookpayload("VAQN"), headers={"Content-Type": "application/json"}, )

addbookjson = add_book.json()  # {"Msg":"successfully added","ID":"i94332"}
bookID = addbookjson["ID"]
print(bookID)  # i94332

print(add_book.text)  # {"Msg":"successfully added","ID":"i94332"}
print(add_book.status_code)
print(add_book.headers)

assert add_book.status_code == 200

del_book = requests.post(getconfig()['API']['endpoint'] + Resource.deletebook, json=
delbookidpayload(bookID))

delbookjson = del_book.json()
print(delbookjson['msg'])  # book is successfully deleted
print(del_book.status_code)
assert del_book.status_code == 200
