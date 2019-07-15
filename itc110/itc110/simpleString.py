# get user's first and last names

first = input("Please enter your first name : ")
last = input("Please enter your last name : ")

#concatenate first initial with 7 chars of last name
uname = first[0] + last[:7]
print(uname.lower())
