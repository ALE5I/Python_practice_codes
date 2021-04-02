
def is_prime(number):
    aux = 0

    if number == 1:
        return "It is"
    else:
        for x in range (2, number):
            if number % x == 0:
                return "It's not"
        return "It is"
                


if __name__ == '__main__':
    
    while True:
        number = int(input('Select number: '))
        print(is_prime(number))

