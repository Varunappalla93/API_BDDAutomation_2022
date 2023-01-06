import requests
from behave import *
from APITestingRequests.payload import *
from Utilities.Resources import Resource
from Utilities.configurations import getconfig, getAccessToken


# Library API
@given('The book details need to be added to library')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + Resource.addbook
    context.payload = addbookpayload("QA", "33")


@when('we execute post api method')
def step_impl(context):
    context.add_book = requests.post(context.url,
                                     json=context.payload, headers={"Content-Type": "application/json"}, )


@then('Books are added to library')
def step_impl(context):
    addbookjson = context.add_book.json()  # {"Msg":"successfully added","ID":"i94332"}
    context.bookID = addbookjson["ID"]
    print(context.bookID)  # i94332

    print(context.add_book.text)  # {"Msg":"successfully added","ID":"i94332"}
    print(context.add_book.status_code)
    print(context.add_book.headers)

    assert context.add_book.status_code == 200

# for datadriven using parametrization
@given('The book details with {isbn} and {aisle} which need to be added to library')
def step_impl(context, isbn, aisle):
    context.url = getconfig()['API']['endpoint'] + Resource.addbook
    context.payload = addbookpayload(isbn, aisle)


# Github API
@given('I have github creds')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ("V@runappalla93", getAccessToken())


@when('I hit gitrepo api')
def step_impl(context):
    context.gitresp2 = context.se.get(Resource.githubrepourl)


@then('status code should be {statuscode:d}')
def step_impl(context,statuscode):
    print(context.gitresp2.text)
    print(context.gitresp2.status_code)
    assert context.gitresp2.status_code == statuscode

# keep response as context.response for all step_impl methods, to use this generic
# status code method
