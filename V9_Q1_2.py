india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

n=input("enter a city_1 name  : ")
m=input("enter a city_2 name  : ")

if n in india and m in india:
    print("both belong to india")
elif n in pakistan and m in pakistan:
    print("both belong to pakistan")
elif n in bangladesh and m in bangladesh:
    print("both belong to bangladesh")
else:
    print("They don't belong to same country.")
