import requests
import json

# params take in dict format
getbookresp = requests.get("http://216.10.245.166/Library/GetBook.php", params={'AuthorName': 'Rahul Shetty2'})
print(getbookresp.text)
print(type(getbookresp.text))  # <class 'str'>

print(getbookresp.status_code)
print(getbookresp.headers)

assert getbookresp.headers['Content-Type'] == 'application/json;charset=UTF-8'

print(getbookresp.cookies)

getbookdict = json.loads(getbookresp.text)
print(getbookdict)
print(type(getbookdict))  # <class 'list'>

print(getbookdict[1]['book_name'])

# or directly use json without getting text of api first
getbookjsonresp = getbookresp.json()
print(getbookjsonresp)
print(type(getbookjsonresp))  # <class 'list'>
print(getbookdict[1]['book_name'])

for book in getbookjsonresp:
    if book['isbn'] == 'abcd':
        print(book)
        break

print(book)
assert book == {'book_name': 'Devops', 'isbn': 'abcd', 'aisle': '75'}
