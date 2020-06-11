
filename = "details.csv"
file = open(filename,"w",encoding = 'utf-8')
file.write("DEPARTMNET,ROLL NUMBER,REGISTER NUMBER,YEAR OF PASSING,PHONE NUMBER\n")
class Student:
    title_list = ["Dapartment","Roll number","Register number","Year of passing","Phone number"]
    def __init__(self,department):
        self.department_name = department    
        self.students_detail = {}
        self.total_students = 0
    def insert_student(self):
        '''Insert new Student in a Dictionary'''
        student_name = input("Enter Student name --> ").lower()
        if student_name not in self.students_detail:
            department = input("Enter Student Department --> ")
            roll_number = input("Enter Student Roll Number --> ")
            register_number = Student.get_reg_no()
            year_of_passing = Student.get_year_pass()
            phone_number = Student.get_ph_no()
            self.students_detail[student_name] = [department,roll_number,register_number,year_of_passing,phone_number]
            self.total_students += 1
            file.write(department.replace(",","|") + "," + roll_number.replace(",","|") + "," + str(register_number) + "," + str(year_of_passing) + "," + str(phone_number))
        else:
            print("Student name is already inserted")    
    def display_student(self):
        '''Display given student Details'''
        student_name = input("Enter Student name --> ").lower()
        if student_name in self.students_detail:
            print(f"Student {student_name} details are :")
            for title,detail in zip(self.title_list,self.students_detail[student_name]):
                print(f"{title} : {detail}")
        else:
            print(f"Given {student_name}  not registered!!!")
            next_student = input("Enter 1 to check another Student else press any key --> ")
            if  next_student == '1':
                self.display_student()
            else:
                print("Thank you !!!")
    def delete_student(self):
        '''Delete given student detail''' 
        student_name = input("Enter Student name --> ").lower()
        if student_name in self.students_detail:
            del self.students_detail[student_name]
            print(f"Student {student_name} details are successfully deleted")
        else:
            print(f"Student {student_name} is not registered")
    def update_student(self):
        '''updae student details'''
        student_name = input("Enter Student name --> ").lower()
        if student_name in self.students_detail:
            index = int(input("To update Enter 0 for Department|1 for Roll number|2 for Register number --> "))
            detail = input(f"Enter updating detail for {self.title_list[index]} --> ")
            self.students_detail[student_name][index] = detail       
            print("Details are Successfully updated")
        else:
            print(f"Given Student {student_name} is not registered!!!")
            next_student = input("Enter 1 to check another Student else press any key --> ")
            if  next_student == '1':
                self.update_student()
            else:
                print("Thank you !!!")  
    def no_of_students(self):
        '''Get total number of student'''
        print(f"Total students are : {self.total_students}")  
    @staticmethod
    def get_reg_no():
        try:
            register_number = int(input("Enter Student Register Number --> "))
            valid_reg_no = register_number
        except Exception:
            print(Exception,"\n Try again!!!")
            valid_reg_no = Student.get_reg_no()
        return valid_reg_no
    @staticmethod
    def get_year_pass():
        year = input("Enter Student year of passing --> ")
        valid_year = 0
        if len(year) == 4 and year.isdigit() and int(year[:2])<25:
            valid_year = int(year)
        else:
            print("Invalid year try again!!!")
            valid_year = Student.get_year_pass()
        return valid_year             
    @staticmethod
    def get_ph_no():
        phone = input("Enter Student Phone Number --> ")
        valid_phone = 0
        if len(phone) == 10 and phone.isdigit():
            valid_phone = phone
        else:
            print("Invalid phone number try again!!!")
            valid_phone = Student.get_ph_no()    
        return valid_phone
def find_department(available_department,department_name):
    for department in available_department:
        if department.department_name == department_name:
            return department
    return False        

def main():
    '''Main function'''
    print("Enter --- Create | Insert | Update | Delete | Display | Total Student | Quit")
    choice = input("Enter Choice --> ").lower()
    available_department = []
    inserted_department = []
    while True:
        if choice == 'create':
            department_name = input("Enter dapartment name --> ")
            if (department_name not in inserted_department):
                department = Student(department_name)
                available_department.append(department)
                print(f"{department_name} Department is Successfully created")
            else:
                print(f"{department_name} Department is already created ")    
            choice = input("Enter Choice --> ").lower()
            
        elif choice == 'insert':
            department_name = input("Enter department name to insert student details --> ")
            department = find_department(available_department,department_name)
            if department:
                department.insert_student()
            else:
                print("The given department is not registered !!!")    
            choice = input("Enter Choice --> ").lower()
        elif choice == 'update':
            department_name = input("Enter department name to update student details --> ")
            department = find_department(available_department,department_name)
            if department:
                department.update_student()
            else:
                print("The given department is not registered !!!")    
            choice = input("Enter Choice --> ").lower()
        elif choice == 'delete':
            department_name = input("Enter department name to delete student details --> ")
            department = find_department(available_department,department_name)
            if department:
                department.delete_student()
            else:
                print("The given department is not registered !!!")    
            choice = input("Enter Choice --> ").lower()
        elif choice == 'display':
            department_name = input("Enter department name to display student details --> ")
            department = find_department(available_department,department_name)
            if department:
                department.display_student()
            else:
                print("The given department is not registered !!!")    
            choice = input("Enter Choice --> ").lower()
        elif choice == "total student":
            department_name = input("Enter department name to display student length details --> ")
            department = find_department(available_department,department_name)
            if department:
                department.no_of_students()
            else:
                print("The given department is not registered !!!")    
            choice = input("Enter Choice --> ").lower()    
        elif choice == 'quit':
            print("Student class is closed \n Thank you")
            break
        else:
            print("Invalid choice!!! Enter a valid choice")
            choice = input("Enter Choice --> ").lower()
main()
file.close()

