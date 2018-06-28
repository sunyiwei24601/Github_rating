import json
import requests
import random
import re
s=requests.Session()
#s.auth=('sunyiwei24601','7646ec91e4625755edb7c9788a5346a68936f14e')

def get_headers():
    tokens=[
        '7646ec91e4625755edb7c9788a5346a68936f14e',
        'cad0bbf3e6bfc03e2f505f1bba5e917e34d87de2'
    ]
    headers={
        'Authorization':'token '+random.choice(tokens),
        'Accept'       :'application/vnd.github.v3.star+json,'
                        'application/vnd.github.symmetra-preview+json,'
                        'application/vnd.github.squirrel-girl-preview,'
                        'application/vnd.github.hellcat-preview+json'
    }
    return headers

def get_tools(url):
    r=s.get(url,headers=get_headers())
    j=json.loads(r.text)
    return j

def pages_tool(url):
    next=[url]
   
    while(len(next)!=0):
        print(url)
        url=next[0]
        r=s.get(url,headers=get_headers())
        j=json.loads(r.text)
       
        if(isinstance(j,dict) and j.get('message')):
            return []
        h=r.headers
        head=dict(h)
        
        if(head.get('Link')):
            link=head['Link']
            next=re.findall('.*<(.*?)>; rel="next"',link)
            yield json.loads(r.text)
        else:
            yield j
            next=[]
#获取user的内容
def get_user(name):
    url='https://api.github.com/users/'+name
    print(url)
    response=s.get(url,headers=get_headers())
    
    j=json.loads(response.text)
    return j
#得到user或org的repos
def get_repos(type,name):
    url='https://api.github.com/'+type+'/'+name+'/repos'
    print(url)
    response=s.get(url,headers=get_headers())
    
    j=json.loads(response.text)
    return j
#根据组织名得到他的详细信息，如果不是就转到getuser
def get_ogz(org):
    url='https://api.github.com/orgs/'+org
    print(url)
    response=s.get(url,headers=get_headers())
    
    j=json.loads(response.text)
    if (j.get('type')):
        return j
    else:
        return (get_user(org))
#得到具体的repos的细节
def get_repos_details(repo):
    basic=['id','node_id','name','full_name','owner','html_url','private','created_at','updated_at',
              'pushed_at','size','stargazers_count','watchers_count','forks']
    url_name=['url','teams_url','events_url','issue_events_url','assignees_url','languages_url'
              ,'contributors_url','stargazers_url','merges_url','issues_url','milestones_url',
              ]
    'collaborators_url'
    
    repo['detail']=get_tools(repo['url'])
    for u in url_name[1:]:
        repo[u[:-4]]=list(pages_tool(repo[u].split('{')[0]))
#获取用户的细节
def get_user_details(name):
    details={}
    url='https://api.github.com/users/{}'.format(name)
    detail=get_tools(url)
    details['detail']=detail
    basic=['followers_url','starred_url','subscriptions_url']
    for url in basic:
        #通过对{进行分割来得到前面无损的url
        uu=detail[url].split('{')[0]
        details[url[:-4]]=list(pages_tool(uu))
    return details

if __name__=='__main__':
    name='neurochain'
    print(get_user_details(name))
    pass