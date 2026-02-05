

# prompts the greeting

greeting = input("Greeting : ")
greeting = greeting.lower().strip()

# check for hello
if "hello" in greeting:
    print("$0")

# check for h started word
elif greeting[0] =="h":
    print("$20")

# others
else:
    print("$100")

