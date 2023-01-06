import requests

from Utilities.configurations import *

# for uploading files using post http method

# url= base end point uri
# myfiles={'file':open('report.xlsx','rb')}

# we use files=myfiles similar to headers=myheaders

# filedata=requests.post(url,files=myfiles)
# print(filedata.text)

# verify=False for skipping SSL certifications, auth for authentication using username and accesstoken.
gitresp = requests.get(" https://api.github.com/user", verify=False, auth=("V@runappalla93", getAccessToken()))

print(gitresp.text)
print(gitresp.status_code)
