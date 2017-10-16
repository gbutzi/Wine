import json

#load from file
with open('test.txt', 'r') as f:
  try:
    data = json.load(f)
  except ValueError:
    data = {}

print(data)

print(data['foo'])

with open('test2.txt', 'r+') as f:
  json.dump(data, f)
