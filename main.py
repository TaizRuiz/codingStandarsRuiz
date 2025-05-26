class student:
    def __init__(s, id, name):
        if not name or str(name).strip == "":
            print("name not entered")
        if not id or str(id).strip == "":
            print("id not entered")
        s.id = id
        s.name = name
        s.grades = []
        s.is_passed = ""
        s.honor = ""

    def add_grades(self, g):
        if (isinstance(g, (int, float))) and (0 <= g <= 100):
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
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

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

    def determine_pass_or_fail(self):
        if (self.calc_average(self.grades) >= 60):
            self.is_passed = "Passed"
        else:
            self.is_passed = "Failed"

    def startrun():
        a = student("x", "")
        a.addGrades(100)
        a.addGrades("Fifty")  # broken
        a.calcaverage()
        a.checkHonor()
        a.deleteGrade(5)  # IndexError
        a.report()
    startrun()
