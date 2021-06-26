total = ""

for x in range(9): 

    wiki = input("Paste: ")

    details = wiki.split("	")

    series, episode = details[0].split('x')
    series, episode = int(series), int(episode)

    date = details[1]

    david1, david2  = details[2].split(' and ')
    lee1, lee2  = details[3].split(' and ')

    david1 = f"[[{david1}]]"
    david2 = f"[[{david2}]]"
    lee1 = f"[[{lee1}]]"
    lee2 = f"[[{lee2}]]"

    liar = input("Liar: ")
    if liar == "d1": 
        david1 = f"'''{david1}'''"
    elif liar == "d2": 
        david2 = f"'''{david2}'''"
    elif liar == "l1": 
        lee1 = f"'''{lee1}'''"
    elif liar == "l2": 
        lee2 = f"'''{lee2}'''"

    d_score, l_score = details[4].split('–')
    d_score, l_score = int(d_score), int(l_score)

    if d_score == l_score: 
        colour = "ffffdd"
    elif d_score > l_score: 
        colour = "#ffdddd"
    else: 
        colour = "ddffdd"

    p1 = f"""
|- bgcolor="{colour}"
| {{{{Code|{series}|{episode}}}}}
| {date}
| {david1} and {david2}
| {d_score}-{l_score}
| {lee1} and {lee2}
"""

    total = total + p1 

from pandas.io.clipboard import copy 
copy(total)

