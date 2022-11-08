# -*- coding: utf-8 -*-

import pickle
import json

mylist = [["aaaa", "bbbb", "cccc"], ["dddd", "eeee", "ffff"],
          ["gggg", "hhhh", "iiii"], ["jjjj", "kkkk", "llll"],
          ["mmmm", "nnnn", "oooo"]]

with open('example.json', 'w') as f:
    json.dump(mylist, f)


with open('example.pickle', 'wb') as f:
    pickle.dump(mylist, f)
