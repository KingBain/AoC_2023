import re


gamePattern = r'^Card\s+(?P<ID>\d+):\s+(?P<WinningNumbers>[\d\s]+)\s+\|\s+(?P<MyNumbers>[\d\s]+)$'


total = 0

with open("data.txt") as file:
    for item in file:

        #exampleGame = "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        exampleGame = item 
        matches = re.finditer(gamePattern, exampleGame)

        for match in matches:
            id = match.group('ID') 
            winningNumbers = match.group('WinningNumbers').split()
            myNumbers = match.group('MyNumbers').split()

            myWinningNumbers = list(set(winningNumbers).intersection(set(myNumbers)))

            if myWinningNumbers:
                score = 2 ** (len(myWinningNumbers)-1)
            else:
                score = 0

            total += score
print(total)