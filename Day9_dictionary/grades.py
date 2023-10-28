student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: add the grades to student_grades

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Accetable"
    else:
        student_grades[key] = "Fail"



#dont chaghe bellow

print(student_grades)