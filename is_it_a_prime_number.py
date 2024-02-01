n = int(input("check this number:  "))



def prime_checker(number):
    if number % 2 == 0 or number % 3 == 0:
        if number == 2 or number == 3:
            print("this is a primal number")
        else:
            print("this is not a primal number")
        
    elif number == 1:
        print("this is not a primal number")
    else:
        print("this is a primal number")


prime_checker(number = n)

