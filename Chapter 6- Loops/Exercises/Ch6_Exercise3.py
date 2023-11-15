while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 3:
        print("Your ticket is $10")
    elif age < 12:
        print("Your ticket is $20") 
    else:
        print("Your ticket is $25")
        
        