
exp =[2200,2350,2600,2130,2190]

#1
print("Dollar spend extra in february than January :",exp[1]-exp[0])

#2
print("first quarter expense :",exp[0]+exp[1]+exp[2])

#3
print("spent 2000 in any month :", 2000 in exp)

#4
exp.append(1980)
print("expenses at the end of the june :",exp)
print("expenses of the june :",exp[-1])

#5
exp[3] = exp[3]-200
print("expenses after 200 return in April :",exp)
