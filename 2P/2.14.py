import json

cities = [
    {'rank' : 1, 'city' : '상하이', 'population' : 241500},
    {'rank' : 2, 'city' : '부산', 'population' : 341500},
    {'rank' : 3, 'city' : '이란', 'population' : 441500},
    {'rank' : 4, 'city' : '러시아', 'population' : 541500},
    {'rank' : 5, 'city' : '일본', 'population' : 641500},
    {'rank' : 6, 'city' : '중국', 'population' : 741500},
]

print(json.dumps(cities, ensure_ascii=False, indent=2))

with open('cities.json', 'w') as f:
    json.dump(cities, f, ensure_ascii=False, indent=2)