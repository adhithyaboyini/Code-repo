while True:
    x = float(input("Enter your First digit : "))
    y = float(input("Enter your Second digit : "))
    
    print("Addition = 1 ")
    print("Subtraction = 2")
    print("Multiplication = 3")
    print("Division = 4")
    print("Exit = 5")
    op = int(input("enter your operation code : "))
    
    if op == 1:
        result = x + y
        print("Result : ",result)
        
    elif op == 2:
        result = x - y 
        print("Result :",result)
        
    elif op == 3:
        result = x * y 
        print("Result : ",result)
        
    elif op == 4:
        if y == 0:
            print("Divison by zero is not allowed")
        else:  
          result = x/y
          print("Result : ",result)
        
    elif op == 5:
        print("Thanks you Using The Calculator, Have a nice day✌️ - √A")
        break
        
    else:
        print("invalid choice, please try again")
        
    print("_-_-_--_-_-__-_-_--_-_--_-_-_-_--_--_-_-_-_--_-_-_-_")
