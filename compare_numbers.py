x = float(input("Enter a nuumber(such as 3.5 or 4.5): "))
y = float(input("Enter a second number: "))

if x == y:
    print(" both number are same")
else:
    if x > y:
        print("first number is greater ")
    else:
        print("first number is smaller")
    if -0.01>x-y and x-y<0.01:
        print ("The numbers are closer")
    if x == y+1 or x == y-1 :
        print("the numbers are one apart")
    if x > 0 and y > 0 or x <0 and y < 0 :
        print("The numbers have same sign")
    else:
        print("The numbers have different sign")