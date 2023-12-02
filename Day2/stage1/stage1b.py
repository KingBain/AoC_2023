import re

limit = {
    "red" : 12,
    "green" : 13,
    "blue" : 14 
}

gameRoster = {}
gameIDPattern = r'^Game (\d+):'
colourAndNumberPattern = r'(?P<number>\d+) (?P<color>\w+)'
gameRoundPattern = r'\d+\s(?:\w+,\s\d+\s)+\w+'


with open("data.txt") as file:
    for item in file:

        #process game string    
        #gameString = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        gameString = item
        #get game ID
        gameID = int((re.search(gameIDPattern, gameString)).group(1))

        #print(gameID)

        roundNumber = 0
        #roundPossible = {}
        possible = True

        #chop into rounds
        for match in re.finditer(gameRoundPattern, gameString):
            roundScore = { 
                "red" : 0,
                "green" : 0,
                "blue" : 0 
            }
            round_text = match.group(0)
            #print("Round " + str(roundNumber))

            #chop into colour and colour number
            results = re.finditer(colourAndNumberPattern, round_text)
            
            #build round score 
            for result in results:
                number = result.group('number')
                color = result.group('color')
                roundScore[color] += int(number)
                #print(f"Number: {number}, Color: {color}")
            
            
            #does bround break the round limits ?
            if not all(roundScore[color] <= limit[color] for color in roundScore):
                possible = False
            
            roundNumber +=1

        if possible:
            gameRoster[gameID]=possible

        
total = 0
for key in gameRoster.keys():
    total += key

print("Sum of keys:", total)