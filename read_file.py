import json
import pandas
import csv
result=[]
with open('overview_alan_1.csv',newline='',encoding='UTF-8')as f:
    reader=csv.DictReader(f)
    n=1
    for row in reader:
        result.append([row['name_p1'],row['Github']])
with open('github_url.json','w') as f:
    json.dump(result,f)