sugar_level = int(input("enter you fasting sugar level :"))

if sugar_level >=80 and sugar_level <=100:
    print("low sugar level")
elif sugar_level >=100:
    print("high sugar level")
else:
    print("too low sugar level eat some sugar.")
