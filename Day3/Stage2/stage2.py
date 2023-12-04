
import numpy as np
import re

gridLeftLimit =0 
gridTopLimit = 0
digitPattern = r'\d+'
symbolPattern = r'[^0-9.]'
gears= {}
parts = {}

#build grid
grid = np.genfromtxt("data.txt", dtype=str, delimiter=1,comments=None)

#max limit positions
gridRightLimit = grid.shape[0] - 1
gridBottomLimit =grid.shape[1] - 1

rowNum = 0
numberBuilder = ""

total = 0


enginePart = False
for row in grid:
    
    #print("Row: " + str(rowNum))
    colNum = 0

    for col in row:
        #print(col)
        
        #check if number 
        if col.isnumeric():
            numberBuilder += col

            #search for adjacent symbol
            for dx in [-1, 0, 1]:

                if dx+rowNum <= gridRightLimit and dx+rowNum >= gridLeftLimit:
                    for dy in [-1, 0, 1]:
                        if dy+colNum <= gridBottomLimit and dy+colNum >= gridTopLimit:
                            if re.search(symbolPattern,grid[rowNum+dx][colNum+dy]):
                                enginePart = True
                                symbolXY = str(rowNum+dx) +  "_" + str(colNum+dy) 
        
        else:
            #captured whole number
            if numberBuilder:

                if enginePart:
                    total += int(numberBuilder)
                    if not symbolXY in parts:
                        parts[symbolXY] = int(numberBuilder)
                    else:
                        gears[symbolXY] = parts[symbolXY] * int(numberBuilder)
                    enginePart = False
            numberBuilder = ""
        colNum += 1
    rowNum += 1


#print(total)
print(sum(gears.values()))
