import json

c = []

with open(".wine.db", "w") as f:
    json.dump(c, f)
