# prime number check
def prime():

    num = int(input('Enter numner pls:'))

    flag = False

    if num!=0:
        for i in range(2, num):
            if num%i == 0:
                flag = True
                break
    if flag:
        print(f"{num} is not a prime")
    else:
        print(f"{num} is prime")

prime()