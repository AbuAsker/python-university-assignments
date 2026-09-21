#Setting values
Subjects = []
Total_Subjects_Grades = []
Subjects_Grades = []
Final_Grade = []


#Getting the number of Courses
Number_Courses = (input("Enter the number of Courses you have: ,Exp:(5)"))
while not Number_Courses.isdigit(): #Error Handling by determining data type
    print("The Input is incorrect, Please Enter a digit number")
    Number_Courses = (input("Enter the number of Courses you have: ,Exp:(5)"))

#Getting the Courses names
Number_Courses = int(Number_Courses)
for i in range(Number_Courses):
    Course_Input = input(f"Enter course NO.{i+1} name and the total grade, Exp(Math,200): ")
    Subject, Total_Grade = [x.strip() for x in Course_Input.split(",")]
    Subjects.append(Subject)
    Total_Subjects_Grades.append(eval(Total_Grade))

#Getting the grades from the user
for i in range(len(Subjects)):
         Subject_Grade = input(f"Enter your grade for {Subjects[i]} Subject as a number: exp:(80) ")
         while not Subject_Grade.isdigit() or int(Subject_Grade) > Total_Subjects_Grades[i]: #Error Handling
          if not Subject_Grade.isdigit():
           print("The Input is incorrect, Please Enter a digit number")
          else:
           print(f"Grade cannot exceed the total mark ({Total_Subjects_Grades[i]})")
          Subject_Grade = input(f"Enter your grade for {Subjects[i]} Subject as a number: exp:(80) ")
         Subjects_Grades.append(eval(Subject_Grade))

#Calculating the grades for each subject
for i in range(len(Subjects)):
    if ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 95:
        Final_Grade.append("A+")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 90:
        Final_Grade.append("A")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 85:
            Final_Grade.append("B+")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 80:
            Final_Grade.append("B")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 75:
            Final_Grade.append("C+")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 70:
            Final_Grade.append("C")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 65:
            Final_Grade.append("D+")
    elif ((Subjects_Grades[i] / Total_Subjects_Grades[i]) * 100) >= 60:
            Final_Grade.append("D")
    else :
           Final_Grade.append("F")

#Calculating the total grade
Total_Term_Grade = (sum(Subjects_Grades) / sum(Total_Subjects_Grades)) * 100
if Total_Term_Grade >= 95:
      Final_Term_Grade = "A+"
elif Total_Term_Grade >= 90:
      Final_Term_Grade = "A"
elif Total_Term_Grade >= 85:
      Final_Term_Grade = "B+"
elif Total_Term_Grade >= 80:
      Final_Term_Grade = "B"
elif Total_Term_Grade >= 75:
      Final_Term_Grade = "C+"
elif Total_Term_Grade >= 70:
      Final_Term_Grade = "C"
elif Total_Term_Grade >= 65:
      Final_Term_Grade = "D+"
elif Total_Term_Grade >= 60:
      Final_Term_Grade = "D"
else :
      Final_Term_Grade = "Fail"

#Printing Results For each subject
for i in range(len(Subjects)):
      print("Grade For", Subjects[i], ":", Final_Grade[i], "(", Subjects_Grades[i], "/", Total_Subjects_Grades[i], ")")

#Printing the total grade
if Final_Term_Grade == "Fail":
     print("Overall, Mark = (", sum(Subjects_Grades), "/", sum(Total_Subjects_Grades), ") Grade= ", Final_Term_Grade)
else :
      print("Overall, Mark = (", sum(Subjects_Grades), "/", sum(Total_Subjects_Grades), ") Grade= ", Final_Term_Grade, "(", round(Total_Term_Grade,2), "%)")
