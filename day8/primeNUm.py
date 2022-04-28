n = int(input("enter number: "))


def prime_number(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("prime")
    else:
        print("not prime")


prime_number(number=n)
