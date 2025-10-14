number = float(input("Enter a number: "))
binary = 0  
while number > 0:
    remainder = number % 2       
    binary =remainder + binary  
    number = number // 2
print("Binary number:", binary)
