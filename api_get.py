import requests
import json
# url='https://api.github.com/users/defunkt/facebox/'
# url='https://api.github.com/repos/defunkt/facebox/issues?state=closed'
# url='https://api.github.com/issues?sort=created'
url='https://api.github.com/orgs/BankEx'
s=requests.Session()
s.auth=('sunyiwei24601','b470bed42a5401214b26ca926c6dbe27589e1b0f')
headers={
# 'Authorization': 'token 03de74ada736153e374e5a9efb979c361c36463b',
'Accept': 'application/vnd.github.v3.star+json,application/vnd.github.symmetra-preview+json,  application/vnd.github.squirrel-girl-preview'
}
r=s.get(url,headers=headers)

print(r.text)

