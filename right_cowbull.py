import random
def cow_bull():
    list1=[0,1,2,3,4,5,6,7,8,9]
    i=0
    secret_list=[]
    bull=[]
    cow=[]
    while i < 5:
        random_number = random.choice(list1)
        if random_number not in secret_list:
            secret_list.append(random_number)
            i=i+1
    print(secret_list,"ye secret list hain")
    total_chances=10
    count_of_chances=0
    while count_of_chances<=total_chances:
        number=int(input("guess a number"))
        position=int(input("guess the position"))
        if (number in secret_list) and (secret_list.index(number) == position):
            bull.insert(position,number)
            print("Bull-This number is corret secret number and right position",bull)
        elif (number in secret_list):
            if (secret_list.index(number) != position):
                cow.append(number)
            print("Cow, This is correct numbers but wrong position you can reuse it",cow)
        else:
            print("this number is not in secret list")
        count_of_chances+=1 
        print("chances that you used",total_chances-count_of_chances)
        if secret_list==bull:
            print("you win the game")
            break
    else:
        print("you lose the game")
    while True:
        again=input("you want to play again yes or no:=")
        if again=="yes":
            cow_bull()
        else:
            break
    # print(secret_list,"ye secret list hain")

cow_bull()
