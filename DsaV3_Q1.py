
month =["January","February","March","April","May"]
expense =[2200,2350,2600,2130,2190]

#11. In Feb, how many dollars you spent extra compare to January?

print("expense of febrauary over jan ", expense[1]-expense[0])
#2. Find out your total expense in first quarter (first three months) of the year.
print("expnese of the first quarter is : ",expense[0]+expense[1]+expense[2])
#3. Find out if you spent exactly 2000 dollars in any month
print("Amount spent exaclty 2000 in any month : ",2000 in expense)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

month.insert(5,"June")
expense.insert(5,1980)

print(month)
print(expense)

#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

print("refund for april budget ",expense[3]-200)
