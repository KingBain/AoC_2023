import re

gameRoster = {}
gameIDPattern = r'^Game (\d+):'
colourAndNumberPattern = r'(?P<number>\d+) (?P<color>\w+)'
gameRoundPattern = r'\d+\s(?:\w+,\s\d+\s)+\w+'
total = 0 

#process game string
#gameString = item    
gameString = "Game 94: 14 red, 10 green; 15 red; 4 red; 4 green, 7 red, 1 blue; 6 red, 5 green; 1 red, 2 green"

#get game ID
gameID = int((re.search(gameIDPattern, gameString)).group(1))

max = {
    "red" : 0,
    "green" : 0,
    "blue" : 0 
}

#chop into rounds
for match in re.finditer(gameRoundPattern, gameString):
    round_text = match.group(0)
    print

    #chop into colour and colour number
    results = re.finditer(colourAndNumberPattern, round_text)
    
    #build round score 
    for result in results:
        number = result.group('number')
        color = result.group('color')
        
        if int(number) > int(max[color]):
            max[color] = int(number)
print(max)

    
#total += max["red"] * max["blue"] * max["green"]
    #print(str(total))
    

#print("Power Total: " + str(total))    