class student:
    grade = 10
    name = "Lynette"
    age = 13
    school = "B.H.J.S"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("I am in Grade", self.grade)

    def personal(self):
        print("My age is", self.age)
        print("My school is", self.school)
ob = student()
ob.introduction()
ob.details()
ob.personal()
            
