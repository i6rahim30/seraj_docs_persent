from department import Department
class Doctor :
    def __init__(self,name,department) :
        self.name = name
        self.department = Department(department)