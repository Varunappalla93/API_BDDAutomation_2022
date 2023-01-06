import requests

# Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
myfiles = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
r = requests.post(url, files=myfiles)
print(r.status_code)
print(r.text)
