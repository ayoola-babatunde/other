#%%
import json
import pickle
from itertools import chain
from collections import Counter
from num2words import num2words as n2w
    
#%%
#Convert tables of series to dict
#{S07x07: Date\tDavid_team\tLee_team\tScore\n}
try: 
    with open("library.json") as jsonfile: 
        library = json.load(jsonfile) 
except FileNotFoundError: 
    library = {}
    with open("pastseries.txt", 'r') as f: 
        for line in f: 
            try: 
                key, value = line.split('\t', maxsplit=1)
                library[key] = value
            except ValueError: 
                continue
    del library['Episode']
    jsonfile = json.dumps(library)
    f = open("library.json", "w")
    f.write(jsonfile)
    f.close()

#%%
#Convert dict to sequential list of all guests

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

#%%
#Manual all guests list reference
#{series:index of last item}
reference = {1:23, 2:57, 3:92, 4:125, 5:159, 6:193, 7:227, 
8:269, 9:307, 10:345, 11:383, 12:423, 13:467, 14:511}

#%%
#Input
srinput = int(input("Series: "))
epinput = int(input("Episode: "))
overallinput = int(input("Overall: "))

#Get series details in library
totinput = f'{srinput:02d}x{epinput:02d}'

wiki = f'{totinput}\t{library[totinput]}'

#Process details
details = wiki.split("	")

series, episode = srinput, epinput

date = details[1]

#guests
david1, david2  = details[2].split(' and ')
lee1, lee2  = details[3].split(' and ')

#score
d_score, l_score = details[4].split('â€“')
d_score, l_score = int(d_score), int(l_score)

if d_score == l_score: 
    result = "Draw"
    lresult = f"It was a draw, {d_score} points to {l_score} points"
    p5 = "[[Category:Episodes which ended in a draw]]"
elif d_score > l_score: 
    result = "David's team won"
    lresult = f"David's team defeated Lee's team by {d_score} points to {l_score}"
    p5 = "[[Category:Episodes won by David's team]]"
else: 
    result = "Lee's team won"
    lresult = f"Lee's team defeated David's team by {l_score} points to {d_score}"
    p5 = "[[Category:Episodes won by Lee's team]]"

#%%
#Appearances
n_allguests = allguests[:reference[series]+1]
counts = Counter(n_allguests)

#%%
p1 = f"""
{{{{Infobox episode
|overall = {overallinput}
|series = {series}
|episode = {episode}
|airdate = {date}
|David1 = {david1}
|David2 = {david2}
|Lee1 = {lee1}
|Lee2 = {lee2}
|result = {result}
|previous = [[Series {series}, Episode {episode-1}]]
|next = [[Series {series}, Episode {episode+1}]]}}}}
The '''{n2w(episode, ordinal=True)}''' episode of the '''{n2w(series, ordinal=True)} series''' was first broadcast on {date}. It's the {n2w(overallinput, ordinal=True)} overall episode of ''[[Would I Lie To You?]]''.
"""

p2 = f"""
==Guests==
{{| class="wikitable" border="1" width="40%"
|- bgcolor="cccccc"
!Team
!Guest
!Appearance #
|- bgcolor="E1E8EF"
| rowspan="2" |David's team
|{david1}
|{n2w(counts[david1], to="ordinal_num")} appearance
|- bgcolor="E1E8EF"
|{david2}
|{n2w(counts[david2], to="ordinal_num")} appearance
|- bgcolor="ffffdd"
| rowspan="2" |Lee's team
|{lee1}
|{n2w(counts[lee1], to="ordinal_num")} appearance
|- bgcolor="ffffdd"
|{lee2}
|{n2w(counts[lee2], to="ordinal_num")} appearance
|}}
"""

p3 = f"""
===Home Truths===

*'''{david1}:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{david2}:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{lee1}:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{lee2}:''' "." – {{{{True}}}} {{{{Lie}}}}

===This is My...===

*This week's guest: ''''''
*Connections
**'''{david2}:''' . – {{{{True}}}} {{{{Lie}}}}
**'''{david1}:''' . – {{{{True}}}} {{{{Lie}}}}
**'''David Mitchell:''' . – {{{{True}}}} {{{{Lie}}}}

**'''{lee2}:''' . – {{{{True}}}} {{{{Lie}}}}
**'''{lee1}:''' . – {{{{True}}}} {{{{Lie}}}}
**'''Lee Mack:''' . – {{{{True}}}} {{{{Lie}}}}

===Quick-Fire Lies===

*'''David Mitchell:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''Lee Mack:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{david1}:''' . – {{{{True}}}} {{{{Lie}}}}
*'''{david2}:''' . – {{{{True}}}} {{{{Lie}}}}
*'''{lee1}:''' . – {{{{True}}}} {{{{Lie}}}}
*'''{lee2}:''' . – {{{{True}}}} {{{{Lie}}}}

===Quotes===

{{{{QuoteBox||}}}}
{{{{QuoteBox||}}}}
{{{{QuoteBox||}}}}

==Final Scores==

{lresult}. 
"""


p4 = f"""
{{{{S{series} episodes}}}}
[[Category:Series {series} episodes]]
[[Category:Episodes]]
"""
final = p1 + p2 + p3 + p4 + p5

from pandas.io.clipboard import copy 
copy(final)


# %%
