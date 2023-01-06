import requests
from APITestingRequests.payload import *
from Utilities.Resources import Resource
from Utilities.configurations import getconfig

# runs after the scenarios present with library tag feature files.
def after_scenario(context,scenario):
    if " @library" in scenario.tags:
        del_book = requests.post(getconfig()['API']['endpoint'] + Resource.deletebook,
                             json=delbookidpayload(context.bookID))

        delbookjson = del_book.json()
        print(delbookjson['msg'])  # book is successfully deleted
        print(del_book.status_code)
        assert del_book.status_code == 200
