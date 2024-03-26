india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

n=input("enter a city name and find out the country : ")

if n in india:
    print("you belong to india")
elif n in pakistan:
    print("you belong to pakistan")
elif n in bangladesh:
    print("you belong to bangladesh")
else:
    print("not found...")
