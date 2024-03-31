def area(a,b,shape="triangle"):
    
    if shape=="triangle":
        area=1/2*(a*b) 
    elif shape=="rectangle":
        area=a*b 
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None
    return area


triangle = area(10,20,"triangle")
print(triangle)
