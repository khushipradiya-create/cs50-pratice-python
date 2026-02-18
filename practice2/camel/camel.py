
# camelCase - > snake_case

def main():
    camelCase = input("camleCase : ")

    for c in camelCase:
        if c.isupper():
           new_c = "_" + c.lower()
           camelCase =  camelCase.replace(c, new_c)
           
          

    print("snake_case :",camelCase)


main()