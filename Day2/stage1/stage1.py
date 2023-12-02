import re

limit = {
    "red" : 12,
    "green" : 13,
    "blue" : 14 
}

gameRoster = {}
gameIDPattern = r'^Game (\d+):'
colourAndNumberPattern = r'(?P<number>\d+) (?P<color>\w+)'


with open("data.txt") as file:
  for item in file:

    gameRound = item
    gameID = int((re.search(gameIDPattern, gameRound)).group(1))

    game = { 
        "red" : 0,
        "green" : 0,
        "blue" : 0 
        }

    matches = re.finditer(colourAndNumberPattern, gameRound)

    for match in matches:
        number = match.group('number')
        color = match.group('color')

        game[color] += int(number)
        #print(f"Number: {number}, Color: {color}")

    for key in game.keys():
        print("Colour " + key + ": " + str(game[key]))

    if all(game[color] <= limit[color] for color in game):
        # All colors meet their respective limits
        print("All colors meet their limits.")
        gameRoster[gameID]=game
        
    else:
        # At least one color doesn't meet its limit
        print("Not all colors meet their limits.")

total = 0
for key in gameRoster.keys():
    total += key

print("Sum of keys:", total)