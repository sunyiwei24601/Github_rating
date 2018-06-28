import json
import csv
filename='data.json'
with open(filename) as f:
    j=json.load(f)
basic=['id','node_id','name','full_name','owner','html_url','private','created_at','updated_at',
              'pushed_at','size','stargazers_count','watchers_count','forks']

result=[]
for i in j:
    repos=j[i]['repos']
    if(isinstance(repos,list)):
        print(repos)
        for repo in repos:
            
            data={}
            data['project']=i
            for key in basic:
                data[key]=repo.get(key,'')
            result.append(data)
    else:
        repo=repos
        
        print(repo)
        data={}
        data['project']=i
        for key in basic:
            data[key]=repo.get(key,'')
        result.append(data)
with open('project_details.csv','w',newline='') as csvfile:
    fieldnames=['project']+['id','node_id','name','full_name','owner','html_url','private','created_at','updated_at',
              'pushed_at','size','stargazers_count','watchers_count','forks']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for d in result:
        print(d)
        writer.writerow(d)




