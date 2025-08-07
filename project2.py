def nearestmultiple(num):
    if num>=4:
        near=num+(4-(num%4))
    else:
        near=4
    return near
def lose():
    print("\n\nYOU LOSE")
    print("Better luck next time!")
    exit(0)
#cheak consecutive
def check(xyz):
    i=1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!=1:
            return False
        i=i+1
    return True
#start game
def start1():
    xyz=[]
    last=0
    while True:
        print("Enter 'F' to take first chance.")
        print("Enter 'S' to take second chance.")
        chance=input('> ')
        if chance=="F":
            while True:
                if last==20:
                    lose()
                else:
                    print("\n Your Turn")
                    print("\n\nHow many number you wish to enter")
                    inp=int(input('> '))
                    if inp>0 and inp<=3:
                        comp=4-inp
                    else:
                        print("wrong input.You are disqualified from game!")
                        lose()

                    i,j=1,1
                    print("Now enter the values")
                    while i<=inp:
                        a=input('> ')
                        a=int(a)
                        xyz.append(a)
                        i=i+1

                    last=xyz[-1]

                    if check(xyz)==True:
                        if last==21:
                            lose()
                        else:
                            while j<=comp:
                                xyz.append(last+j)
                                j=j+1
                            print("order of index after computer's turn is: ")
                            print(xyz)
                            last=xyz[-1]
                    else:
                        print("You did not input consecutive integer.")
                        lose()
        # player takes the second chance
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                #"Computer's turn"
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print ("Order of inputs after computer's turn is:")
                print (xyz)
                if xyz[-1] == 20:
                    lose()
                    
                else:
                    print ("\nYour turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print ("Enter your values")
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i = i + 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        # print (xyz)
                        near = nearestmultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print ("\nYou did not input consecutive integers.")
                        # print ("You are disqualified from the game.")
                        lose()
            print("\n\n Congrtulation!")
            print("You won.")
            exit(0)
        else:
            print("wrong choice")
game=True
while game==True:
    print("Player 2 is computer")
    print("Do you want to play the 21 number game?(Yes/No)")
    ans=input("> ")
    if ans=='Yes':
        start1()
    else:
        print("Do you want to quit?(Yes/No)")
        answer=input("> ")
        if answer=='Yes':
            print('You are quiting...')
            exit(0)
        elif answer=='No':
            print("Continue...")
        else:
            print("Wrong answer")



