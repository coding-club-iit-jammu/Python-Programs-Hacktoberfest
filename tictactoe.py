def a1(c):
    if l1[1]==' ':
        l1[1]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def a2(c):
    if l1[2]==' ':
        l1[2]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def a3(c):
    if l1[3]==' ':
        l1[3]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def b1(c):
    if l2[1]==' ':
        l2[1]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def b2(c):
    if l2[2]==' ':
        l2[2]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def b3(c):
    if l2[3]==' ':
        l2[3]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def c1(c):
    if l3[1]==' ':
        l3[1]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def c2(c):
    if l3[2]==' ':
        l3[2]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def c3(c):
    if l3[3]==' ':
        l3[3]=c
    else:
        print("Oops! That cell was already filled so if user vs user : you missed your turn or if user vs comp : game terminated")
def fault():
    global winner
    print("You entered a cell that does not exist so if user vs user : you missed your turn or if user vs comp : game terminated")
    winner="-"

def userinput():
    global usercoord,uchar
    usercoord = input("Enter row name and column name for user eg. a1,b3,c2 etc. : ")
    if usercoord == "a1":
        a1(uchar)
    elif usercoord == "a2":
        a2(uchar)
    elif usercoord == "a3":
        a3(uchar)
    elif usercoord == "b1":
        b1(uchar)
    elif usercoord == "b2":
        b2(uchar)
    elif usercoord == "b3":
        b3(uchar)
    elif usercoord == "c1":
        c1(uchar)
    elif usercoord == "c2":
        c2(uchar)
    elif usercoord == "c3":
        c3(uchar)
    else:
        fault()
def printres():
    global r1,l1,l2,l3
    print(r1)
    print(l1[0] + "|" + l1[1] + "|" + l1[2] + "|" + l1[3] + "|")
    print(l2[0] + "|" + l2[1] + "|" + l2[2] + "|" + l2[3] + "|")
    print(l3[0] + "|" + l3[1] + "|" + l3[2] + "|" + l3[3] + "|")

def vsu():
    global l1,l2,l3,winner,uchar1,uchar2,usercoord1,usercoord2
    l1 = r2.split('|')
    l2 = r3.split('|')
    l3 = r4.split('|')
    print("You chose another USER as your opponent. All the best to both of you!! User 1 starts.")
    uchar1=input("What symbol does user 1 choose (x/o) ?: ")
    if uchar1=="x":
        uchar2="o"
    else:
        uchar2="x"
    count=1
    user1coord = input("Enter row name and column name for user 1 eg. a1,b3,c2 etc. : ")
    if user1coord == "a1":
        a1(uchar1)
    elif user1coord == "a2":
        a2(uchar1)
    elif user1coord == "a3":
        a3(uchar1)
    elif user1coord == "b1":
        b1(uchar1)
    elif user1coord == "b2":
        b2(uchar1)
    elif user1coord == "b3":
        b3(uchar1)
    elif user1coord == "c1":
        c1(uchar1)
    elif user1coord == "c2":
        c2(uchar1)
    elif user1coord == "c3":
        c3(uchar1)
    else:
        fault()
    printres()
    while count <= 4 :
        user2coord = input("Enter row name and column name for user 2 eg. a1,b3,c2 etc. : ")
        if user2coord == "a1":
            a1(uchar2)
        elif user2coord == "a2":
            a2(uchar2)
        elif user2coord == "a3":
            a3(uchar2)
        elif user2coord == "b1":
            b1(uchar2)
        elif user2coord == "b2":
            b2(uchar2)
        elif user2coord == "b3":
            b3(uchar2)
        elif user2coord == "c1":
            c1(uchar2)
        elif user2coord == "c2":
            c2(uchar2)
        elif user2coord == "c3":
            c3(uchar2)
        else:
            fault()
        if (l1[1] == uchar2 and l1[2] == uchar2 and l1[3] == uchar2) or (
                l2[1] == uchar2 and l2[2] == uchar2 and l2[3] == uchar2) or (
                l3[1] == uchar2 and l3[2] == uchar2 and l3[3] == uchar2) or (
                l1[1] == uchar2 and l2[1] == uchar2 and l3[1] == uchar2) or (
                l1[2] == uchar2 and l2[2] == uchar2 and l3[2] == uchar2) or (
                l1[3] == uchar2 and l2[3] == uchar2 and l3[3] == uchar2) or (
                l1[1] == uchar2 and l2[2] == uchar2 and l3[3] == uchar2) or (
                l1[3] == uchar2 and l2[2] == uchar2 and l3[1] == uchar2):
            winner = "USER2"
            print()
            print("CONGRATS, USER 2 WINS.")
            break
        printres()
        user1coord=input("Enter row name and column name for user 1 eg. a1,b3,c2 etc. : ")
        if user1coord == "a1":
            a1(uchar1)
        elif user1coord == "a2":
            a2(uchar1)
        elif user1coord == "a3":
            a3(uchar1)
        elif user1coord == "b1":
            b1(uchar1)
        elif user1coord == "b2":
            b2(uchar1)
        elif user1coord == "b3":
            b3(uchar1)
        elif user1coord == "c1":
            c1(uchar1)
        elif user1coord == "c2":
            c2(uchar1)
        elif user1coord == "c3":
            c3(uchar1)
        else:
            fault()
        printres()
        if (l1[1]==uchar1 and l1[2]==uchar1 and l1[3]==uchar1) or (l2[1]==uchar1 and l2[2]==uchar1 and l2[3]==uchar1) or (l3[1]==uchar1 and l3[2]==uchar1 and l3[3]==uchar1) or (l1[1]==uchar1 and l2[1]==uchar1 and l3[1]==uchar1) or (l1[2]==uchar1 and l2[2]==uchar1 and l3[2]==uchar1) or (l1[3]==uchar1 and l2[3]==uchar1 and l3[3]==uchar1) or (l1[1]==uchar1 and l2[2]==uchar1 and l3[3]==uchar1) or (l1[3]==uchar1 and l2[2]==uchar1 and l3[1]==uchar1):
            winner="USER1"
            print()
            print("CONGRATS, USER 1 WINS.")
            break
        count += 1

def vcomp():
    global l1,l2,l3,winner,uchar,cchar,usercoord
    l1 = r2.split('|')
    l2 = r3.split('|')
    l3 = r4.split('|')
    print("You chose COMPUTER as your opponent.It has been unbeatable yet so ALL THE BEST !!")
    uchar = input("What symbol does user choose (x/o) ?: ")
    if uchar == "x":
        cchar = "o"
    else:
        cchar = "x"
    ans1=input("Who plays first (comp/user)? : ")
    if ans1=="comp":
        l1[1]=cchar
        printres()
        userinput()
        printres()
        if l1[2]==uchar:
            l3[1]=cchar
            printres()
            userinput()
            printres()
            if l2[1] != uchar:
                l2[1]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l3[3]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins as two win paths open")
        elif l2[1]==uchar:
            l1[3]=cchar
            printres()
            userinput()
            printres()
            if l1[2] != uchar:
                l1[2]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l3[3]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins as two win paths open")
        elif l1[3]==uchar:
            l3[1]=cchar
            printres()
            userinput()
            printres()
            if l2[1] != uchar:
                l2[1]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l3[3]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins as two win paths open")
        elif l3[1]==uchar:
            l1[3]=cchar
            printres()
            userinput()
            printres()
            if l1[2] != uchar:
                l1[2]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l3[3]=cchar
                printres()
                print()
                winner="COMP"
                print("COMPUTER wins as two win paths open")
        elif l2[3] == uchar:
            l1[3] = cchar
            printres()
            userinput()
            printres()
            if l1[2] != uchar:
                l1[2] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l3[1] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins as two win paths open")
        elif l3[2] == uchar:
            l1[3] = cchar
            printres()
            userinput()
            printres()
            if l1[2] != uchar:
                l1[2] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l3[1] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins as two win paths open")
        elif l3[3] == uchar:
            l3[1] = cchar
            printres()
            userinput()
            printres()
            if l2[1] != uchar:
                l2[1] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l1[3] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins as two win paths open")
        elif l2[2] == uchar:
            l3[1] = cchar
            printres()
            userinput()
            printres()
            if l2[1] != uchar:
                l2[1] = cchar
                printres()
                print()
                winner = "COMP"
                print("COMPUTER wins. You've got to be attentive!")
            else:
                l2[3] = cchar
                printres()
                userinput()
                printres()
                if l3[2]==uchar or l3[3]==uchar :
                    l1[2]=cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3]!=uchar:
                        l1[3]=cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        print("Game TIED. Well done")
                        winner="X"
                elif l1[2]==uchar or l1[3]==uchar:
                    l3[2]=cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3]!=uchar:
                        l3[3]=cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        print("Game TIED. Well done")
                        winner ="X"
                else:
                    pass
        else:
            pass

    elif ans1=="user":
        userinput()
        printres()
        if l1[1]==uchar:
            l2[2]=cchar
            printres()
            userinput()
            printres()
            if l1[2]== uchar:
                l1[3]=cchar
                printres()
                userinput()
                printres()
                if l3[1]!=uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[1]==uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[3]==uchar:
                l1[2] = cchar
                printres()
                userinput()
                printres()
                if l3[2] != uchar:
                    l3[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[1]==uchar:
                l2[1] = cchar
                printres()
                userinput()
                printres()
                if l2[3] != uchar:
                    l2[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[3]==uchar:
                l3[2] = cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] != uchar:
                        l3[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[3]==uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2]==uchar:
                        l3[3]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[3]==uchar:
                        l3[2]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[2]==uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l3[2]==uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            else:
                pass
        elif l1[3]==uchar:
            l2[2] = cchar
            printres()
            userinput()
            printres()
            if l1[2] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] != uchar:
                        l2[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[3] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[1] == uchar:
                l1[2] = cchar
                printres()
                userinput()
                printres()
                if l3[2] != uchar:
                    l3[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[3] == uchar:
                l2[3] = cchar
                printres()
                userinput()
                printres()
                if l2[1] != uchar:
                    l2[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[1] == uchar:
                l3[2] = cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] != uchar:
                        l3[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[2] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] == uchar:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[1] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] == uchar:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[1] == uchar:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            else:
                pass
        elif l3[1]==uchar:
            l2[2] = cchar
            printres()
            userinput()
            printres()
            if l2[1] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] != uchar:
                        l1[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[2] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[1] == uchar:
                l2[1] = cchar
                printres()
                userinput()
                printres()
                if l2[3] != uchar:
                    l2[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[3] == uchar:
                l3[2] = cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[3] == uchar:
                l3[2] = cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] != uchar:
                        l3[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[2] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[3] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] == uchar:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[3] == uchar:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            else:
                pass
        elif l3[3] == uchar:
            l2[2] = cchar
            printres()
            userinput()
            printres()
            if l2[3] == uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] != uchar:
                        l1[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[2] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] != uchar:
                        l2[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[1] == uchar:
                l2[1] = cchar
                printres()
                userinput()
                printres()
                if l2[3] != uchar:
                    l2[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] != uchar:
                        l3[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[1] == uchar:
                l3[2] = cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[3] == uchar:
                l2[3] = cchar
                printres()
                userinput()
                printres()
                if l2[1] != uchar:
                    l2[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[2] == uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[1] == uchar:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        l1[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[1] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] == uchar:
                        l1[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[1] == uchar:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            else:
                pass
        elif l2[2]==uchar:
            l1[1] = cchar
            printres()
            userinput()
            printres()
            if l1[2] == uchar:
                l3[2] = cchar
                printres()
                userinput()
                printres()
                if l1[3]==uchar:
                    l3[1]=cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins as two win paths open")
                elif l2[3]==uchar:
                    l2[1]=cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] != uchar:
                        l3[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                elif l3[3]==uchar:
                    l3[1]=cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] != uchar:
                        l2[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                elif l3[1]==uchar:
                    l1[3]=cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1]==uchar:
                        l2[3]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3]==uchar:
                        l2[1]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[3]==uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
                elif l2[1]==uchar:
                    l2[3]=cchar
                    printres()
                    winner = "X"
                    print("Game TIED. Well done")
                else:
                    pass
            elif l1[3]==uchar:
                l3[1]= cchar
                printres()
                userinput()
                printres()
                if l2[1] != uchar:
                    l2[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER WINS. You've got to be attentive")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2]==uchar:
                        l3[2]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2]==uchar:
                        l1[2]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[3]==uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[3]==uchar:
                l2[1]=cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER WINS. You've got to be attentive")
                else:
                    l1[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] == uchar:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        l1[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER WINS. You've got to be attentive")
            elif l3[3]==uchar:
                l1[3]=cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER WINS. You've got to be attentive")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[1]==uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l3[2]==uchar:
                l1[2] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER WINS. You've got to be attentive")
                else:
                    l3[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        l2[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER WINS. You've got to be attentive")
            elif l3[1]==uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l1[2] != uchar:
                    l1[2] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER WINS. You've got to be attentive")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[3] == uchar:
                        winner ="X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[1]==uchar:
                l2[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] == uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins as two win paths open")
                elif l3[2] == uchar:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3] != uchar:
                        l1[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                elif l3[3] == uchar:
                    l1[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] != uchar:
                        l1[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                elif l1[3] == uchar:
                    l3[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] == uchar:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2] == uchar:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[3] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
                elif l1[2] == uchar:
                    l3[2] = cchar
                    printres()
                    winner = "X"
                    print("Game TIED. Well done")
                else:
                    pass
            else:
                pass
        elif l1[2]==uchar:
            l2[2]=cchar
            printres()
            userinput()
            printres()
            if l1[1]==uchar:
                l1[3]=cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1]=cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1]=cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[3]==uchar:
                l1[1]=cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] != uchar:
                        l2[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[1]==uchar:
                l1[1]=cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[3]=cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] != uchar:
                        l3[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[2]=cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[3]==uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] != uchar:
                        l3[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[1]==uchar:
                l1[1]=cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l3[3]==uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[1] == uchar:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        l1[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l3[2]==uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins as two way win paths")
            else:
                pass
        elif l2[1]==uchar:
            l2[2] = cchar
            printres()
            userinput()
            printres()
            if l3[1] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] != uchar:
                        l1[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[1] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[2] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] != uchar:
                        l3[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[2] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3] != uchar:
                        l1[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[3] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[1] == uchar:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[2] == uchar:
                        l1[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l1[3] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] == uchar:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[1] == uchar:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[3] == uchar:
                l1[1] = cchar
                printres()
                userinput()
                printres()
                if l3[3] != uchar:
                    l3[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins as two way win paths")
            else:
                pass
        elif l3[2]==uchar:
            l2[2] = cchar
            printres()
            userinput()
            printres()
            if l3[3] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[1] != uchar:
                        l2[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[1] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l2[3] != uchar:
                        l2[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[3] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3] != uchar:
                        l1[3] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l2[1] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[1] != uchar:
                        l1[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[3] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] == uchar:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        l3[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l1[1] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] == uchar:
                        l2[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[3] == uchar:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l2[1] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l1[2] == uchar:
                l3[1] = cchar
                printres()
                userinput()
                printres()
                if l1[3] != uchar:
                    l1[3] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins as two way win paths")
            else:
                pass
        elif l2[3] == uchar:
            l2[2] = cchar
            printres()
            userinput()
            printres()
            if l1[3] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[2] != uchar:
                        l3[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[3] == uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[2] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[2] != uchar:
                        l1[2] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[2] == uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[1] != uchar:
                        l1[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l3[2] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l1[3] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[1] != uchar:
                        l3[1] = cchar
                        printres()
                        print()
                        winner = "COMP"
                        print("COMPUTER wins. You've got to be attentive!")
                    else:
                        l2[1] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
            elif l1[1] == uchar:
                l1[3] = cchar
                printres()
                userinput()
                printres()
                if l3[1] != uchar:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l3[3] == uchar:
                        l3[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2] == uchar:
                        l3[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l3[1] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l2[1] = cchar
                    printres()
                    userinput()
                    printres()
                    if l1[3] == uchar:
                        l1[2] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l1[2] == uchar:
                        l1[3] = cchar
                        printres()
                        winner = "X"
                        print("Game TIED. Well done")
                    elif l3[2] == uchar:
                        winner = "X"
                        print("Game TIED. Well done")
                    else:
                        pass
            elif l2[1] == uchar:
                l3[3] = cchar
                printres()
                userinput()
                printres()
                if l1[1] != uchar:
                    l1[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins. You've got to be attentive!")
                else:
                    l3[1] = cchar
                    printres()
                    print()
                    winner = "COMP"
                    print("COMPUTER wins as two way win paths")
            else:
                pass
        else:
            pass
    else :
        print("Please enter a proper option.")

def game():
    print("WELCOME TO TIC-TAC-TOE GAME")
    global r1,r2,r3,r4,a
    r1 = "_|1|2|3|"
    r2 = "a| | | |"
    r3 = "b| | | |"
    r4 = "c| | | |"
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print()
    print("Options :")
    print("1. Person vs Person")
    print("2. Person vs Computer")
    print("How do you want to play ?")
    a=int(input("Enter your choice (1/2) : "))
    if a == 1:
        vsu()
    elif a == 2 :
        vcomp()
    else:
        print("PLease enter a proper choice (1/2).")

ans="yes"
r1=""
r2=""
r3=""
r4=""
l1=[]
l2=[]
l3=[]
uchar1=""
uchar2=""
user1coord=""
user2coord=""
winner=""
uchar=""
usercoord=""
cchar=""
a=0
while ans=="yes":
    game()
    if winner == ""  and a==1:
        print("Game TIED.Well done both")
    if (winner == "" or winner =="-") and a==2:
        print("Game TERMINATED")
    print()
    ans=input("Do you want to play again (yes/no) ?: ")
    print()
if (ans == "no"):
    print("Thank you for playing.Hope you enjoyed!!")
