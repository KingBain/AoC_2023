import re

total = 0
gameRoster = {}
gameIDPattern = r'^Game (\d+):'
colourAndNumberPattern = r'(?P<number>\d+) (?P<color>\w+)'

with open("data.txt") as file:
  for item in file:

    gameRound = item
    gameID = int((re.search(gameIDPattern, gameRound)).group(1))

    matches = re.finditer(colourAndNumberPattern, gameRound)
    max = {
        "red" : 0,
        "green" : 0,
        "blue" : 0 
    }
    for match in matches:
        number = match.group('number')
        color = match.group('color')

        if int(number) > int(max[color]):
            max[color] = int(number)

    total += max["red"] * max["blue"] * max["green"]
    print(max)   
print(total)