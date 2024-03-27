result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
add = 0

for i in result:
    if(i == "heads"):
        count = count+1
    else:
        add+=1
print("total number of heads. :",count)
print("total number of tails :", add)
