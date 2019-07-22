# word counter.
#   write a program that counts the number of words in a sentence entered by the user.

def main():
    print("This is a Word Counter Program")

    # get input
    words = input("Type a sentence: ")

    # count words
    splitWords = words.split(" ")
    numWords = len(splitWords)
    
    # output of wordcount number
    print("The number of words in your sentence is: ", numWords)

main()
