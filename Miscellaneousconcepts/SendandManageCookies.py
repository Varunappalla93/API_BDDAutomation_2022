# Send cookies.

# Handle redirection history such as 301 status code which redirects from 301 internally
# to 200/201 etc.

# timeout - will wait for some time to get response to avoid wait issues
import requests

cookiecall=requests.get("http://rahulshettyacademy.com", cookies={'visit-month': 'February'},
                        timeout=2)


print(cookiecall) # <Response [200]>
print(cookiecall.text)
print(cookiecall.status_code) # 200
print(cookiecall.history) # [<Response [301]>]

# To check if any re-directions are present instead of actual
# status code, use allow_redirects=False in request.
# o/p - now status code is 301 if allow_redirects=False is used .

'''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Rahul Shetty Academy</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <script data-ad-client="ca-pub-9851078085090971" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<link rel="stylesheet" href="styles.1dd7dba42f16dcc4d92b.css"></head>
<body>
  <app-root></app-root>
<script src="runtime-es2015.1eba213af0b233498d9d.js" type="module"></script><script src="runtime-es5.1eba213af0b233498d9d.js" nomodule defer></script><script src="polyfills-es5.049f620af8c864cf4d88.js" nomodule defer></script><script src="polyfills-es2015.f2c5ab749249a66bdf26.js" type="module"></script><script src="scripts.96315435df8f90fcd841.js" defer></script><script src="main-es2015.ad38df072d61fc90a3c6.js" type="module"></script><script src="main-es5.ad38df072d61fc90a3c6.js" nomodule defer></script></body>
</html>

'''
# eg-2


# use session() and update() to send common cookies for api calls.
import requests
se=requests.session()
se.cookies.update({'visit-month': 'February'})

cookie2=se.get("https://httpbin.org/cookies",cookies={'visit-year':'2021'})
print(cookie2.text)
print(cookie2.status_code)


'''
{
  "cookies": {
    "visit-month": "February", 
    "visit-year": "2021"
  }
}

200
'''