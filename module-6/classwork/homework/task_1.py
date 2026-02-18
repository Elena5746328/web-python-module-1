basketball_players =[
    (1, "Майкл Джордан", 198),
    (2, "Леброн Джеймс", 206),
    (3, "Коби Брайант", 198)
]

new_id = basketball_players[-1][0] + 1
basketball_players.append((new_id, "Шакил О'Нил", 216))
print(basketball_players)

i = 0
while i < len(basketball_players):
    if basketball_players[i][0] == 1:
        basketball_players.pop(i)
        break
    i += 1
print(basketball_players)

for p in basketball_players:
    if "Леброн" in p[1]:
        print(p)

i = 0
while i < len(basketball_players):
    if basketball_players[i][0] == 2:
        basketball_players[i] = (2, "Леброн Рэймонд", 208)
        break
    i += 1
print(basketball_players)
