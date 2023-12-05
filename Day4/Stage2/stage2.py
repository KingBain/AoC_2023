import re

gamePattern = r'^Card\s+(?P<ID>\d+):\s+(?P<WinningNumbers>[\d\s]+)\s+\|\s+(?P<MyNumbers>[\d\s]+)$'
gameList = {}

total = 0

with open("data.txt") as file:
    for item in file:
        exampleGame = item 
        matches = re.finditer(gamePattern, exampleGame)

        for match in matches:
            id = int(match.group('ID')) 
            winningNumbers = match.group('WinningNumbers').split()
            myNumbers = match.group('MyNumbers').split()
            myWinningNumbers = list(set(winningNumbers).intersection(set(myNumbers)))

            if myWinningNumbers:
                                # wins    #copies           
                gameList[id] = [len(myWinningNumbers),1]
            else:
                gameList[id] = [0,1]


#print(gameList) 

total = 0
for i in range(1, len(gameList)+1, +1):   
    print("card " + str(i))
    currentCardWins = gameList[i][0]
    currentCardCopies = gameList[i][1]
    total += currentCardCopies
    #print("Copied of this card " + str(currentCardCopies))
    for c in range(0,currentCardCopies,+1):
        for x in range(1,currentCardWins+1,+1 ):
            nextCard = (x+i)
            gameList[nextCard][1] += 1
            #print("Boost card by 1, card ID " + str(nextCard))
#print(gameList) 
print(total)