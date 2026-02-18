

def main():

    vowel = ["a", "e", "i", "o", "u"]
    tweet = input("Input: ")
    tweet = tweet.lower()

    for c in tweet:
        if c in vowel:
          tweet   =  tweet.replace(c, "")
    
    print(tweet)

    
main()