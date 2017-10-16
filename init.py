import pickle

c = []

with open(".wine.db", "wb") as f:
    pickle.dump(pickle.dumps(c), f)
