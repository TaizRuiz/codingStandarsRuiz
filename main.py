class student:
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.grades = []
        s.is_passed = "NO"
        s.honor = "?"

    def add_grades(self, g):
        if g >= 0 and g <= 100:
            self.grades.append(g)

    def get_grades_letter(average):
        if average >= 90 and average <= 100:
            return "A"
        elif average >= 80 and average <= 89:
            return "B"
        elif average >= 60 and average <= 69:
            return "C"
        else:
            return "F"

    def calc_average(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t/len(self.grades)
        return self.get_grades_letter(avg)

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)

    def startrun():
        a = student("x", "")
        a.addGrades(100)
        a.addGrades("Fifty")  # broken
        a.calcaverage()
        a.checkHonor()
        a.deleteGrade(5)  # IndexError
        a.report()
    startrun()
