x = open("findTheFlag.txt", "r")
start = 0
for y in x.readline():
     if y == str(1):        
       start += int(y)
print start