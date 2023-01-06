import requests

from Utilities.configurations import getAccessToken

# Session Management to create a session with
# common auth details for reusing the same in other requests.
se = requests.session()
se.auth = auth=("V@runappalla93", getAccessToken())

url2 = "https://api.github.com/users/repos"
gitresp2 = se.get(url2)

print(gitresp2.text)
print(gitresp2.status_code)

# {"login":"repos","id":77416,"node_id":"MDQ6VXNlcjc3NDE2","avatar_url":"https://avatars.githubusercontent.com/u/77416?v=4","gravatar_id":"","url":"https://api.github.com/users/repos","html_url":"https://github.com/repos","followers_url":"https://api.github.com/users/repos/followers","following_url":"https://api.github.com/users/repos/following{/other_user}","gists_url":"https://api.github.com/users/repos/gists{/gist_id}","starred_url":"https://api.github.com/users/repos/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/repos/subscriptions","organizations_url":"https://api.github.com/users/repos/orgs","repos_url":"https://api.github.com/users/repos/repos","events_url":"https://api.github.com/users/repos/events{/privacy}","received_events_url":"https://api.github.com/users/repos/received_events","type":"User","site_admin":false,"name":null,"company":null,"blog":"","location":null,"email":null,"hireable":null,"bio":null,"twitter_username":null,"public_repos":0,"public_gists":0,"followers":21,"following":0,"created_at":"2009-04-24T13:53:27Z","updated_at":"2014-03-09T10:18:05Z"}
# 200
