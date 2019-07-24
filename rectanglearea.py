def main():
    l, w = input("Enter two values separated by a space: ")
    print(areaRec(l, w))

#function declaration
def areaRec(l, w):
    a = int(l) * int(w)
    return a
main()
