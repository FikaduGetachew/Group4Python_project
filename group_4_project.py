import sys

#Function use to register studentID,studentName,studentGpa,studentDep,studentGender
def register_student(info_List):   
   try:
      print("Registration form")
      num_students = int(input("Enter the number of students: "))
      for i in range(1, num_students + 1):
            info_List=[]
            with open("student_db.txt", 'r') as file:
                for line in file:
                    info_List.append(line.split(";"))
                st_id = input("Enter student id: ")
                for studentId in info_List:
                   while st_id== studentId[0]:
                     print("The ID is already exist enter new ID")
                     st_id = input("Enter student id: ")
                st_name = input("Enter student name: ")
                while st_name>='0'and st_name<='9':
                    print("enter the Correct  name")
                    st_name = input("Enter student name: ")
                st_gpa = input("Enter student GPA: ")
                while st_gpa >'4'or st_gpa<'0':
                    print("please enter the Correct  gpa")
                    st_gpa = input("Enter student gpa: ")
                st_dep = input("Enter the department: ")
                while  st_dep>='0'and st_dep<='9':
                    print("enter the Correct  department")
                    st_dep = input("Enter student department: ")
                st_gen = input("Enter student gender M or F: ")
                while st_gen not in['M','F'] or len(st_gen)!=1:
                    print("please enter the Correct  gender")
                    st_gen= input("Enter student gender: ")
                with open("student_db.txt", "a") as newfile:
                    newfile.write(f"{st_id};{st_name};{st_gpa};{st_dep};{st_gen}\n")
                    print("Registered successfully")
      file.close()
   except ValueError:
       print("Please enter valid number of student")
   except IOError:
       print("error accure while accessing file")
   except Exception as e:
       print("error",str(e))  
   finally:              
     menu()
     
def show_all(info_List):
   print("Student database:")
   print("*********All students found*********")
   try:
      
      with open("student_db.txt", 'r') as file:
         for line in file:
             student=line.split(";")
             if len(student)>=5:
                 
                 print(f" ID: {student[0]}\n Name: {student[1]}\n Gpa: {student[2]}\n Department: {student[3]}\n Gender: {student[4]}")
      print("*********All students found*********")       
   except FileNotFoundError:
     print("File not found")
   except Exception as e:
      print("error",e)
   menu()    
                 
  
#Function use search student we want to see
def search_student(info_List):
  try:
      found = False
      id_search = input("Enter student ID to search: ")
      with open("student_db.txt", 'r+') as file:
        for line in file:
            student= line.split(";")
            if student[0] == id_search:
                print("******** Student found ************")
                print(f"Name:{student[1]}\nGPA:{student[2]}\nDepartment:{student[3]}\nGender:{student[4]}")
                print("************************************")
                found = True
                break
      if not found:
         print("Student does not exist")
  except FileNotFoundError:
      print("File not found")
  except Exception as e:
      print("error",e)
  finally:              
     menu()
#Function use to update student gpa
def update_gpa(info_List):
  try:
     st_id = input("Enter student ID: ")
     updated = False
     lines = []
     with open("student_db.txt", 'r') as file:
        for line in file:
            student= line.split(";")
            if st_id == student[0]:
                new_gpa = input("Enter new student GPA: ")
                while new_gpa >'4'or new_gpa<'0' :
                        print("Please enter the Correct  gpa...")
                        new_gpa = input("Enter student gpa: ")       
                student[2]=new_gpa
                line=";".join(student)
                updated = True
                print(f"{student[1]} Gpa updated successfully! to {new_gpa}")
            lines.append(line)
     if not updated:
        print(f"Student with ID {st_id} not found.")
     else:
        with open("student_db.txt", 'w') as file:
            file.writelines(lines)
  except FileNotFoundError:
       print("File not found")
  except Exception as e:
       print("error",e) 
  finally:       
     menu()

#Function use to update  student name
def update_name(info_List):
   try:
     st_id = input("Enter student ID: ")
     updated = False
     lines = []
     with open("student_db.txt", 'r') as file:
        for line in file:
            student=line.split(";")
            if st_id == student[0]:
                new_name = input("Enter corrected New Name: ")
                line = f"{student[0]};{new_name};{student[2]};{student[3]};{student[4]}"
                updated = True
                print(f"Name of student with ID {st_id} updated successfully! to {new_name}")
            lines.append(line)
     if not updated:
        print(f"Student with ID {st_id} no found.")
     else:
        with open("student_db.txt", 'w') as file:
            file.writelines(lines)
   except FileNotFoundError:
        print("File not found")
   except Exception as e:
     print("error",e)
   finally:                
     menu()
#Function use to delete student from where we register
def delete_info(info_List):
   try:
     st_id = input("Enter student ID: ")
     deleted = False
     lines = []
     with open("student_db.txt", 'r') as file:
        for line in file:
            student=line.split(";")
            if st_id != student[0]:
                line=f"{student[0]};{student[1]};{student[2]};{student[3]};{student[4]}"
                lines.append(line)
            else:
                deleted=True
     if not deleted:
        print(f"Student with ID {st_id} not found.")
     else:
        with open("student_db.txt", 'w') as file:
            file.writelines(lines)
     print("student deleted successfully") 
   except FileNotFoundError:
     print("File not found")
   except Exception as e:
     print("error",e)
   finally:              
     menu()
#Function use to count and display total number of students
def count_students(info_List):
  try:
     count=0
     with open("student_db.txt","r") as file:
        for line in file:
            student=line.split(";")
            if len(student)>=5:
             print("*********All students***************")
             print(f" ID: {student[0]}\n Name: {student[1]}\n Gpa: {student[2]}\n Department: {student[3]}\n Gender: {student[4]}\n")
             print("************************************")
             count+=1
     print(f"Total number of students: {count}")
  except FileNotFoundError:
      print("File not found")
  except Exception as e:
      print("error",e)
  finally:        
     menu()
#Function use to count total number of male and female student    
def count_students_gender(info_List):
   try:
      with open("student_db.txt", "r") as file:
        for line in file:
            student = line.strip().split(";")
            if len(student)>=5:
             info_List.append(student)

      malecount = 0
      femalecount = 0
      for student in info_List:
        if len(student)>=5:
         if student[4] == "M":
            malecount += 1
         elif student[4] == "F":
            femalecount += 1
      print(f"Total number of male students: {malecount}")
      print(f"Total number of female students: {femalecount}")
   except FileNotFoundError:
       print("File not found")
   except Exception as e:
       print("error",e)
   finally:            
     menu()
#Function use to display name and department of top scored student for each department
def top_scorer_department(info_List):
   try:
      with open("student_db.txt", "r") as file:
        st_dep = input("Enter the department: ")
        max_gpa = 0
        max_name = ""
        for line in file:
            student=line.split(";")
            if len(student)>=5:
             if student[3] == st_dep and float(student[2]) > max_gpa:
                max_gpa = float(student[2])
                max_name = student[1]
        print(f"Top scoring student in {st_dep} department: {max_name} with GPA {max_gpa}") 
   except FileNotFoundError:
      print("File not found") 
   except Exception as e:
      print("error",e)
   finally:          
     menu()
#Function use to display name and department of top scored female student for each department
def top_female_scorer_depatment(info_List):
   try:
     st_dep = input("Enter department: ")
     with open("student_db.txt", "r") as file:
        for line in file:
            student = line.strip().split(";")
            if len(student)>=5:
             info_List.append(student)

     max_gpa = 0
     max_name = ""
     for student in info_List:
        if len(student)>=5:
         if student[3] == st_dep and float(student[2]) > max_gpa and student[4] == "F":
            max_gpa = float(student[2])
            max_name = student[1]
    
     if max_name:
        print(f"Top scoring female student in {st_dep} department is: {max_name} with GPA {max_gpa}") 
     else:
        print(f"No female student found in the {st_dep} department.")
   except FileNotFoundError:
       print("File not found")
   except Exception as e:
       print("error",e)
   finally:              
     menu()
#Function List names of students who scored greater than a given Gpa
def gpa_threshold(info_list):
   try:
     with open("student_db.txt", "r") as file:
        st_gpa = input("Enter the gpa: ")
        for line in file:
            student=line.split(";")
            if len(student)>=4:
             if float(student[2]) > float(st_gpa) :
              print(f"Top scoring students that greater than {st_gpa} are {student[1]} from {student[3]} departement with gpa {student[2]}\n")
   except FileNotFoundError:
      print("File not found")
   except Exception as e:
      print("error",e)
   finally:                   
     menu()
#Function show frequent student names
def frequent_name(info_List):
   try:
     student_frequency={}
     with open("student_db.txt", "r") as file:
        for line in file:
            student=line.split(";")
            if len(student)>=2:
             if student[1] in student_frequency:
                student_frequency[student[1]] += 1
             else:
               student_frequency[student[1]] = 1
        for student[1],count in student_frequency.items():    
            print( f"{student[1]} is registered {count} times\n" )
   except FileNotFoundError:
      print("file not found")
   except Exception as e:
      print("error",e)
   finally:               
     menu()     
#Function show total number of students in each department
def students_per_department(info_List):
   try:
     student_frequency={}
     with open("student_db.txt", "r") as file:
        for line in file:
            student=line.split(";")
            if len(student)>=4:
             if student[3] in student_frequency:
              student_frequency[student[3]] += 1
             else:
               student_frequency[student[3]] = 1
        for student[3],count in student_frequency.items():    
          print( f"{student[3]} departement have {count} students\n" )
   except FileNotFoundError:
       print("file not found")
   except Exception as e:
      print("error",e)
   finally:               
     menu()  
        
       

# Function to display the menu and handle user choices
def menu():
    print("*************************************WELCOME TO STUDENT MANAGEMENT SYSTEM*************************************")
    print("select your choice")
    print("0. Registration")
    print("1. Search Student")
    print("2. Update Student Name")
    print("3. Update Student Gpa")
    print("4. Display All students")
    print("5. Delete Student Information")
    print("6. Total Number of Students ")
    print("7. Total Number of Students based on Gender ")
    print("8. Top Scoring Students ")
    print("9. Top Scoring Female Students ")
    print("10. Search Students based on GPA ")
    print("11. Display Frequent Student Name ")
    print("12. Display Student per Department ")
    print("13. EXIT")
    print("****************************************************************************************************")
    info_List=[]
    choice = int(input("\n Enter your choice: "))
    if choice==0:
        register_student(info_List)
    elif choice==1:
        search_student(info_List)
    elif choice==2:
        update_name(info_List)  
    elif choice==3:
        update_gpa(info_List)
    elif choice==4:
        show_all(info_List)
    elif choice==5:
        delete_info(info_List) 
    elif choice==6:
        count_students(info_List) 
    elif choice==7:
        count_students_gender(info_List)
    elif choice==8:
        top_scorer_department(info_List) 
    elif choice==9:
        top_female_scorer_depatment(info_List) 
    elif choice==10:
        gpa_threshold(info_List)
    elif choice==11:
        frequent_name(info_List) 
    elif choice==12:
        students_per_department(info_List)
    elif choice==13:
        sys.exit()
    else:
        print("invalid input")                                                          
    menu()   
# Function to close the System
def Exit():
    exit()     

if __name__ == "__main__":
    menu()
