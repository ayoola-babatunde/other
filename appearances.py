#%%
import json
import pickle
from itertools import chain
from collections import Counter
with open("library.json") as jsonfile: 
    library = json.load(jsonfile) 

#%%
try: 
    with open("allguests.txt", "rb") as f: 
        allguests = pickle.load(f)
except FileNotFoundError: 
    allguests = []
    for title in library: 
        deet = library[title] #deet = details
        groups = deet.split('\t')[1:3]
        for group in groups: 
            guests = group.split(' and ')
            allguests = chain(allguests, guests)
    with open("allguests.txt", "wb") as f: 
        pickle.dump(list(allguests), f)
# %%
#{series:index of last item}
reference = {1:23, 2:57, 3:92, 4:125, 5:159, 6:193, 7:227, 
8:269, 9:307, 10:341, 11:383, 12:423, 13:467, 14:511}


