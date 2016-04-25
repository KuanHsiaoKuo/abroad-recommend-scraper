import json
# Reading data back
with open('items.json','r') as f:
    data = json.load(f)
    #data = json.dumps(f)
    print type(data)
    for value in data.values():
        print value
        for v in value:
            print type(v)
            print v
           # print v.encode('utf-8')
