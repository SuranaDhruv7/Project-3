print("Welcome to the Student Data Organizer ! \n")
student_list = []
is_on=True
while is_on:
    choice= int(input("\nSelect an option:\n 1. Add Student \n 2. Display All Student \n 3. Update Student Information \n 4. Delete Student \n 5. Display Subjects offered \n 6. Exit \n Enter your Choice: "))
    if choice == 1:
        print("\nEnter student details:\n")
        student_ID = int(input("Student ID : "))
        name = input("Name : ")
        age  = int(input("Age : "))
        grade = input("Grade : ")
        dob = (input("Date of Birth (YYYY-MM-DD) : "))
        subjects = input("Subjects (comma seprated ) : ")
        student_list.append({'Students_ID': student_ID,'Name':name,'Age':age,'Grade':grade,'Subjects':set(subjects.split(',')),'Date of Birth':(dob,)})
        print("\n Student added successfully !")

    elif choice == 2:
        if student_list:
            print("\n-------Display All Students-------\n ")
            for i in student_list:
                for j,k in i.items():
                    print(f"{j}:{k} | ",end = " ")
                print()
        else:
            print("No such records found ! ")

    elif choice == 3:
        ID = int(input("\nEnter the student ID which you want to update: "))
        for i in student_list:
            if ID == i['Students_ID']:
                detail = input("\nEnter the student detail which you want to update: ")
                if detail == 'Students_ID':
                    print("\nYou can't update the student id !")
                elif detail == 'Name':
                    new_name=input("Enter the New name :").title()
                    i[detail]=new_name
                    print("\n You have updated the Name successfully ! ")
                elif detail == 'Age':
                    new_age=int(input("Enter the New age :"))
                    i[detail]=new_age
                    print("\n You have updated the Age successfully ! ")
                elif detail == 'Grade':
                    new_grade=input("Enter the New grade :").title()
                    i[detail]=new_grade
                    print("\nYou have updated the grade successfully ! ")
                elif detail == 'Date of Birth (YYYY-MM-DD)':
                    print("\nYou can't update the Date of Birth !")
                elif detail =='Subjects (comma seprated )':
                    new_subject = input("Enter the new subject (comma seprated ) : ").title()
                    i[detail]=new_subject
                    print("\nSubjects updated successfully !")
            else:
                print("\nYou have entered the wrong syntax ! ")

    elif choice == 4:
        ID = int(input("\nEnter the student ID you want to delete: "))
        for i in student_list:
            if ID == i['Students_ID']:
                confirm = input(f"Are you sure you want to delete the student {student_ID}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    student_list.remove(i)  
                    print(f"\nStudent with ID {ID} has been deleted successfully!")
                else:
                    print("\nDeletion canceled.")
                break
            else:
                print("\nYou have entered wrong output !")

    elif choice == 5:
        ID = int(input("\nEnter the student ID you want to check the subject : "))
        for i in student_list:
            if ID == i['Students_ID']:
                if 'Subjects' in i and i['Subjects']:
                    print("\n The subject for the student are : ")
                    for subject in i['Subjects']:
                        print(f"- {subject}")
                else:
                    print("\nNo subjects are assigned to this student.")
    elif choice == 6:
        print("\nExiting the program. Goodbye! ")
        is_on=False
    else:
        print("\nYOU HAVE ENTERED A WRONG INPUT:  ")
        is_on=False
