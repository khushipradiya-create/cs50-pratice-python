
x, y, z  =  (input("Expression: ").split(" "))

x = float(x)
z = float(z)

# print(type(x))
# print(type(z))

match y :

    case "+" :
         print(f"{(x +  z) :.1f}")

    case "-" :
         print(f"{(x -  z) :.1f}")

    case "/" :
         if(z == 0):
            print("cannot be divide by zero")    
         else :
            print(f"{(x /  z) :.1f}")

    case "*" :
         print(f"{(x *  z) :.1f}")

    
        
