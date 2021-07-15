#%%
import json

    
    
#%%
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
srinput = int(input("Series: "))
epinput = int(input("Episode: "))
totinput = f'{srinput:02d}x{epinput:02d}'

wiki = f'{totinput}\t{library[totinput]}'

details = wiki.split("	")

series, episode = details[0].split('x')
series, episode = int(series), int(episode)

date = details[1]

david1, david2  = details[2].split(' and ')
lee1, lee2  = details[3].split(' and ')

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


p1 = f"""
{{{{Infobox episode
|overall = 
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
The '''''' episode of the '''tenth series''' was first broadcast on {date}. It's the - overall episode of ''[[Would I Lie To You?]]''.
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
|1st appearance
|- bgcolor="E1E8EF"
|{david2}
|1st appearance
|- bgcolor="ffffdd"
| rowspan="2" |Lee's team
|{lee1}
|1st appearance
|- bgcolor="ffffdd"
|{lee2}
|1st appearance
|}}
"""

p3 = f"""
===Home Truths===

*'''{david1}:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{david2}:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{lee1}:''' "." – {{{{True}}}} {{{{Lie}}}}
*'''{lee2}:''' "." – {{{{True}}}} {{{{Lie}}}}

===This is My...===

*This week's guest: ''' '''
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
print(final)

