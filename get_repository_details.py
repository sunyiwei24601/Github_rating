import json
import requests
import random
from Gitrating.tools import *
s=requests.Session()
s.auth=('sunyiwei24601','9a9c1d46c47f75f57aa382d76b0b0ed98b71ffcc')
headers={
# 'Authorization': 'token 03de74ada736153e374e5a9efb979c361c36463b',
'Accept': 'application/vnd.github.v3.star+json,application/vnd.github.symmetra-preview+json,  application/vnd.github.squirrel-girl-preview'
}

with open('github_url.json') as f:
    projects=json.load(f)
    
project_details={}

#把project分为两类，一种是只有一个repos的，还有是拥有多个repos的users或是orgs
#根据分的长度来区分具体是多个repos还是单个，单个的就直接将获取的repos细节放入
for project in projects[2300:]:
    url=project[1]
    name=project[0]
    if url:
        parts=url.split('/')
        if(parts[2]!='github.com'):
            continue
        if len(parts)==4:
            project_details[name]={'organization_url':url}
        elif len(parts)==5 and parts[-1]=='':
            project_details[name]={'organization_url':url}
        else:
            j=get_tools('https://api.github.com/'+'repos'+'/'+parts[3]+'/'+parts[4])
            project_details[name]={'repos':[j],
                                   'type':'single repos'}

#对于不是单个repo的提取具体的repos数量和信息
for project in project_details:
    p=project_details[project]
    if p.get('organization_url'):
        #提取名称，先尝试organization，再尝试username
        
        try:
            url=p.get('organization_url')
            parts=url.split('/')
            type=get_ogz(parts[-1])['type']
            
        except:
            pass
        #得到他们目录下的repos
        
        if type=='User':
            p['type']=type
            p['repos']=get_repos('users',parts[-1])
        else:
            p['repos']=get_repos('orgs',parts[-1])
            p['type']=type

#分别得到不同项目的repos的具体信息
n=0
error=[]
for project in project_details:
    p=project_details[project]
    n+=1
    print("第"+str(n)+"个project")
    for repo in p['repos']:
        try:
            print('这里要输出'+str(repo['id']))
            get_repos_details(repo)
        except:
            print(error)
            error.append(repo)
            

with open('data8.json','w') as f:
    json.dump(project_details,f)
    print(error)
    print(len(error))
    
    
    



    






