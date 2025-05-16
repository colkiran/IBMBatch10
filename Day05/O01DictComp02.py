
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")
print("-" * 60)

print(f"Sachin :{players['sachin']}")
print("-" * 60)

print(f"Sachin :{sum(players['sachin'])}")
print("-" * 60)

scores = {k :sum(v) for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 60)

scores = [player for player in players.keys()]
print(f"scores :{scores}")
print("-" * 60)

scores = [runs for runs in players.values()]
print(f"scores :{scores}")
print("-" * 60)

# average of runs
def avg(runs):
    av = sum(runs) / len(runs)
    return av

scores = [(k, avg(runs)) for k, runs in players.items()]
print(f"scores :{scores}")
print("-" * 60)

scores = [(k, sum(runs) / len(runs)) for k, runs in players.items()]
print(f"scores :{scores}")
print("-" * 60)

scores = [runs for runs in players.values()]
print(f"scores :{scores}")
print("-" * 60)

# [for i in range(x), for j in range(y)]
scores = [run for runs in players.values() for run in runs]
print(f"scores :{scores}")
print("-" * 60)

scores = [run for runs in players.values() for run in runs if run >= 200]
print(f"scores :{scores}")
print("-" * 60)

scoresGT200 = {name :[scr for scr in score if scr >= 200]
               for name, score in players.items()}
print(f'scores greater than 200 :{scoresGT200}')







print("\n" * 10)
print("-" * 60)
Student = {
    "name": "pratibha",
    "Score": {
        "chem": 23,
        "physics": 45,
        "Maths": 67
    },
    "Grade_Code": {
        "java": "A",
        "Python": "A++"

    }
}

print(f"Student :{Student}")
print("-" * 60)
print(f"Student['Score] :{Student['Score']}")
print("-" * 60)
print(f"Student['Score']['maths'] :{Student['Score']['Maths']}")