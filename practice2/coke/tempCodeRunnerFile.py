
# coke =  50 cents
# machine only accepts : 5 , 10 , 25 cents
# this program keeps taking cents until it reaches the coke amount.

 


def main() :
    Amountdue = 50
    
    while (Amountdue > 0):
        print(f"Amount Due: {Amountdue}")
        cents =  int(input("Insert Coin: "))
        if cents == 25 or cents ==10 or cents ==5 : 
            Amountdue -= cents
        

    print(f"Change Owed : {abs(Amountdue)}")

main()
        