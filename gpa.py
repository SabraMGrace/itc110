# gpa.py
# Calculate which student had the highest grade.

class Student:
    
    # constructor
    def __init__(self, name, hours, gpoints):
        self.name = name
        self.hours = float(hours)
        self.gpoints = float(gpoints)

    # methods
    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getGPoints(self):
        return self.gpoints

    def gpa(self):
        return self.gpoints/self.hours

def makeStudent(infoStr):
    name, hours, gpoints = infoStr.split("\t")
    return Student(name, hours, gpoints)

def main():
    #open file for input
    filename = input("Enter file name: ")
    infile = open(filename, "r")

    best = makeStudent(infile.readline())

    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s

    infile.close()

    print("Best student: ", best.getName())
    print("hours: ", best.getHours())
    print("GPA", best.gpa())

main()
    
