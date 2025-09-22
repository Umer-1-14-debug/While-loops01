
while True:
    try:
        num=int(input("Enter a positive integer."))
        i=1
        if num<0:
            print("Enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input.")
total = 0
i = 1
while i<=num:
    total=total + 1
    i += 1
    print("\numSum = {}".format(total))