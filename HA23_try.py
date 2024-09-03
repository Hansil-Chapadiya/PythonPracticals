while True:
    try:
       q = input("Do you want to Quit (y or n):")
       if q == 'n' or q == 'N':
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))
            s = num1 + num2
            print(s)
       elif q == 'y' or q == 'Y':
            break
    except Exception as e:
        print(e)
        print("Enter Proper value")