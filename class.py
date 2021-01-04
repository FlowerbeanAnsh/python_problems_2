class student:
    no_of_the_exams= 5
    pass


    def printdetails(self):
        return f"Name is {self.name} \n roll NO is {self.rollno} \n section is {self.section} \n university is {self.university}"


rohan = student()
sohan= student()

rohan.name= "ROHAN KUMAR"
rohan.rollno= "12"
rohan.section= "1"
rohan.university="GLA university"

sohan.name =" SOHAN RAJPUT"
sohan.rollno= "22"
sohan.section= "4"
sohan.university="GLA university"

print(sohan.printdetails())
print(rohan.printdetails())




