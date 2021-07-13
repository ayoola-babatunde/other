# %%

copied = """14x01	24 December 2020	Joe Lycett and Ruth Madeley	Jo Brand and Joe Swash	2–3
14x02	8 January 2021	Richard Osman and Lou Sanders	Les Dennis and Alice Levine	2–4
14x03	15 January 2021	Chris McCausland and Laura Whitmore	Maisie Adam and Stephen Hendry	3–2
14x04	22 January 2021	Raj Bisram and Gemma Cairney	Sophie Hermann and Josh Widdicombe	4–2
14x05	29 January 2021	Miles Jupp and Samantha Morton	Sarah Hadland and Bob Mortimer	2–4
14x06	1 February 2021	Sara Barron and Claudia Winkleman	The Rev. Kate Bottley and Ed Gamble	1–4
14x07	8 February 2021	Nicola Coughlan and Dan Walker	Mr. Motivator and Sara Pascoe	4–1
14x08	15 February 2021	Joel Dommett and AJ Odudu	Alex Horne and Sindhu Vee	5–0
14x09	22 February 2021	Roisin Conaty and Roman Kemp	Maya Jama and Dr. Xand van Tulleken	5–1
14x10	1 March 2021	Alex Jones and Martin Lewis	Anna Maxwell Martin and Johnny Vegas	1–5"""

each = copied.split("\n")
# %%
total = ""
for x in each: 
    p1 = divide(x)
    total = total + p1

from pandas.io.clipboard import copy 
copy(total)



# %%
def divide(wikirow): 

    wiki = wikirow

    details = wiki.split("\t")

    series, episode = details[0].split('x')
    series, episode = int(series), int(episode)

    date = details[1]

    david1, david2  = details[2].split(' and ')
    lee1, lee2  = details[3].split(' and ')

    david1 = f"[[{david1}]]"
    david2 = f"[[{david2}]]"
    lee1 = f"[[{lee1}]]"
    lee2 = f"[[{lee2}]]"

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
    return p1

# %%

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

