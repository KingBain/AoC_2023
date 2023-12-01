import re
#read file into for loop 

total = 0

with open("data.txt") as file:
  for item in file:
    #search/filter for numerals, probably a regex,
    #create new array 
    numbers = re.findall(r'\d', item)
    
    #find first and last digit, combine them into large int
    #print(int(numbers[0]+numbers[-1]))
    
    #sum all lines together
    total += int(numbers[0]+numbers[-1])

print (total)



#output sum 