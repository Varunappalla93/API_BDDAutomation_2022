# from Utilities.configurations import getQuery
from Utilities.configurations import getQuery


def addbookpayload(isbn):
    body = {
        "name": "Learn Sel with varun",
        "isbn": isbn,
        "aisle": 32,
        "author": "Varun App"
    }
    return body


def delbookidpayload(bookID):
    body = {
        "ID": bookID
    }
    return body


def buildpayloadfromdb(query):
    addbody = {}
    tuplerow = getQuery(query)
    addbody['name'] = tuplerow[0]
    addbody['isbn'] = tuplerow[1]
    addbody['aisle'] = tuplerow[2]
    addbody['author'] = tuplerow[3]
    return addbody

