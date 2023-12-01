from word2number import w2n
total = 0
numberWords = ["one", "two","three","four","five", "six", "seven", "eight", "nine"]

def returnFirstNum (targetString):
    totalLength = len(targetString)
    startIndex = 0
    searchWindow = 0
    
    for i in range(0, totalLength, 1):
        searchSlot = targetString[startIndex:searchWindow]
        #search for whole words
        for number in numberWords:
            if searchSlot.find(number) != -1:
                return str(w2n.word_to_num(number))

        #search for integer strings 
        if (targetString[searchWindow].isdigit()):
            return targetString[searchWindow]

        searchWindow+=1

def returnLastNum (targetString):
    totalLength = len(targetString)
    startIndex = 0
    searchWindow = 1
    
    for i in range(0, totalLength, 1):

        searchSlot = targetString[totalLength-searchWindow:totalLength]
        #search for whole words
        for number in numberWords:
            if searchSlot.find(number) != -1:
                return str(w2n.word_to_num(number))

        #search for integer strings 
        for char in searchSlot:
            if (char.isdigit()):
                return char

        searchWindow+=1


#print (returnLastNum("4nineeightseven2"))

with open("data.txt") as file:
    for line in file:
        line =line.strip()
        print("interation " + line)
        first=returnFirstNum(line)
        last=returnLastNum(line)
        print(first+last)
        total += int(first+last)
        
        #print (returnFirstNum(line))
        #print (returnLastNum(line))

print(total)