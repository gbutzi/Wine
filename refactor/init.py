import json

c = []

with open(".wine.rf.db", "w") as f:
    json.dump(c, f)
