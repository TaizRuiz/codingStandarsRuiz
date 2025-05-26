class Student:
    def __init__(self, id, name):
        if not name or str(name).strip() == "":
            print("name not entered")
        if not id or str(id).strip() == "":
            print("id not entered")
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = ""
        self.honor = False

    def add_grades(self, g):
        if (isinstance(g, (int, float))) and (0 <= g <= 100):
            self.grades.append(g)
        else:
            print(f"Invalid grade: {g}")

    def get_grades_letter(self, average):
        if 90 <= average <= 100:
            return "A"
        elif 80 <= average < 90:
            return "B"
        elif 60 <= average < 80:
            return "C"
        else:
            return "F"

    def calc_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = True
        else:
            self.honor = False

    def delete_grade(self, value_or_index):
        if isinstance(value_or_index, int):
            if 0 <= value_or_index < len(self.grades):
                del self.grades[value_or_index]
            else:
                print("Index out of range")
        else:
            try:
                self.grades.remove(value_or_index)
            except ValueError:
                print(f"Grade {value_or_index} not found in grades")

    def determine_pass_or_fail(self):
        if self.calc_average() >= 60:
            self.is_passed = "Passed"
        else:
            self.is_passed = "Failed"

    def report(self):
        self.determine_pass_or_fail()
        self.check_honor()
        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        avg = self.calc_average()
        print("Average grade: " + str(avg))
        print("Final Grade = " + self.get_grades_letter(avg))
        print("Pass or Fail = " + self.is_passed)
        print("Honor roll = " + str(self.honor))


def start_run():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # will print invalid grade message
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # will print index out of range
    a.report()


start_run()
