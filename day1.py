def calci(): #this is defining function called calci
    print("nidhi's day 1 project")
    print("choose operation")
    print("1.  add")
    print("2.  sub")
    print("3.  multiply")
    print("4.  divide")
    userinterface = input("enter what operation you would like my calci to perform (1,2,3,4)")
    #whatever the user selcts is stored in userinterface
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number of your choice"))
# float will help us to convert the input sting into decimal so thsat we can handle them as well.
    if userinterface == '1':
      print(f"result:{num1} + {num2}= {num1+num2}")
    elif userinterface == '2':
       print(f"result: {num1} - {num2} ={num1-num2}")
    elif userinterface == '3':
       print(f"result: {num1} * {num2} = {num1*num2}")
    elif userinterface == '4':
        if num2 != 0:
           print(f"result: {num1} / {num2} = {num1/num2}")
        else:
           print("error: division by zero leads to not defined")
           #print(f) is used to add variables or experessions inside a string if it were just a string to be printed then only print(...)
    else:
       print("invalid input")
calci() #this is function calling