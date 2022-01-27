import json

matches_list=[]
for line in open('Data/matches.json', 'r'):
    matches_list.append(json.loads(line))


history_list=[]
for line in open('Data/matches_history.json', 'r'):
    history_list.append(json.loads(line))