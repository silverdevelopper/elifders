class Student:
  
    def __init__(self,number,name,surname,birth_place,department,gpa): 
        self.number = number
        self.name = name
        self.surname = surname
        self.birth_place = birth_place
        self.department = department
        self.gpa = gpa
        
    def print_name(self):
        print(self.name)
        
    def print_surname(self):
        print(self.surname)
        
    def print_birth_pace(self):
        print(self.birth_place)
        
    def print_department(self):
        print( self.department)
        
    def print_gpa(self):
        print( self.gpa)

        
dat = ""
with open("students.dat") as fp:
    dat = fp.read()
line_list = dat.split("\n")

line_list = line_list[2:]
data = []  
for s in line_list:
    line = s.split(" ")
    line_data = []
    for x in line:
        if x != None and x != '':
            line_data.append(x)
    if len(line_data):
        data.append(line_data)

studens_dict = {}    

for student in data:
    s = Student(int(student[0]),student[1],student[2],student[3],student[4],student[5])
    studens_dict[student[0]] = s
    

    
for number in studens_dict:
    studens_dict[number].print_name()
    studens_dict[number].print_surname()
    studens_dict[number].print_birth_pace()
    studens_dict[number].print_department()
    #studens_dict[number].print_gpa()
    

    


    
            


