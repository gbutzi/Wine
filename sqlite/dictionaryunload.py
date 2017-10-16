import json

# save to file
with open('test.txt', 'w') as f:
  data = {}
  data['foo'] = 'bar'
  json.dump(data, f)

  f.seek(0)

  data['check'] = 'bar'
  data['foo'] = 'bar'
  json.dump(data, f)
