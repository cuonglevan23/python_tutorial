teams = ['Lakers', 'Warriors', 'Celtics', 'Bulls', 'Heat']
math_scores = [95, 85, 75, 90, 80]

teams.insert(2, 'Nets')
math_scores.insert(2, 88)
teams.remove('Bulls')
math_scores.remove(75)
# teams.clear()
# teams.pop()
teams.sort()
print(teams)
math_scores.sort()
print(math_scores)
math_scores.reverse()
print(math_scores)
print(teams.index('Warriors'))
print(teams.count('Lakers'))

teams_2 = teams.copy()
print(teams_2)