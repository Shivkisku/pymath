class Student():
    id = 0
    name = ""
    gender = ""
    total = 0  # Fix: Change the type to integer
    per = 0

    def setData(self, id, name, gender, total, per):
        self.id = id
        self.name = name
        self.gender = gender
        self.total = total  # Fix: Change the type to integer
        self.per = per

    def showData(self):
        print("Id :", self.id)
        print("Name :", self.name)
        print("Gender :", self.gender)
        print("Total :", self.total)
        print("Percentage :", self.per)

s = Student()
s.setData(1, 'Shivnath Kisku', 'Male', 422, 84.44)
s.showData()
