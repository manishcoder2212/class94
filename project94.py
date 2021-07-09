def selectScreen():
    print("click 1 for home screen")
    print("click 2 for regester screen")
    print("click 3 for transaction screen")
    v=int (input('select the number'))

    if (v==1):
        screen1()
    elif(v==2):
        screen2()
    else:
        screen3()



def screen1():
    print("you are in the home Screen")
    
    
def screen2():
    print("you are in the regester Screen")

def screen3():
    print("you are in the Transaction Screen")

selectScreen()