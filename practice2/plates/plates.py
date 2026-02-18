

# vanity lisence plate requirements

"""
. all plate must start with 2 letters 
. it can contain max 6 or min 2 letters(numbers and letters)
. number cann't start with zero and number cann't be used in the middle of the plate
. “No periods, spaces, or punctuation marks are allowed.”

"""

def main():
    plate = input("Plate : ").upper()
    if(is_valid(plate)):
        print("Valid")
    else :
        print("Invalid")

    
def is_valid(s):

    # can contain max 6 and min 2 letters
    if len(s)>2 or len(s)<6:
        return False
    # all plate must start with 2 letters
    if not s[:2].isalpha() :
        return False
    # no, periods, spaces, punctuation marks
    if not s.isalnum():
        return False
    

# number cann't start with zero and number cann't be used in the middle of the plate
# here variable state are used 
    number_started = False

    for char in s :
        if char.isdigit():
            # check for first number
            if not number_started:
                if char == "0":
                    return False
                
            number_started = True

        # if number started and nondigit value appear return false and when number is not start this if block will not execute
        else :
            if number_started :
                return False
     
    return True
                 

main()


            