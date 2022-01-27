import json

matches_list=[]
for line in open('Data/matches.json', 'r'):
    matches_list.append(json.loads(line))