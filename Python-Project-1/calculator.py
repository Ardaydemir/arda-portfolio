FirstNumber= int(input("Write first number:"))
SecondNumber= int(input("Write second number:"))
Operation= input("""Select an operation. (Addition: +, Subtraction: -, 
Multiplication: x, Division: /)""")

if Operation == "+":
    print ("Result: "+str(FirstNumber+SecondNumber))

elif Operation == "-":
     print ("Result: " + str(FirstNumber-SecondNumber))

elif Operation == "x":
     print ("Result: " + str(FirstNumber*SecondNumber))

elif Operation == "/":
     print ("Result: " + str(FirstNumber/SecondNumber))
