import random;
min_number = 1
max_number = 6

throw = "yes"

while throw == "yes" or throw == "y":
    print("how many dices you want to throw")
    a = int(input())
    print("lets see your outcomes")
    for i in range(0,a):
        outcome = random.randint(min_number,max_number)
        print("the number on die",i,"is",outcome)
    throw = input("do you want to throw again then press Y or press n")