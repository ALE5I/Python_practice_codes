import random

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']
sim = ['°','!','#','$','%','&','/','(',')','=','?','¡','*','_',':',';',',','.','-','+','+','¿','|']

def pass_gen(size):

    pwd =[]
    array = 0

    for x in range (size):
        #I used the following range so the password has more letters than numbers and more numbers than simbols,
        # this means that it has a 50% chance of been a letter, 30% of been a number an 20% of been a simbol
        array = random.randint(1,10)
        if (array <= 5):
            pwd.append(abc[random.randint(0, len(abc)-1)])

        elif (array <= 8):
            pwd.append(num[random.randint(0, len(num)-1)])

        elif (array <= 10):
            pwd.append(sim[random.randint(0, len(sim)-1)])

    pwd = ''.join(pwd)
    return pwd


if __name__=='__main__':
    size = int(input("Please select the size of your new password: "))
    print(pass_gen(size))