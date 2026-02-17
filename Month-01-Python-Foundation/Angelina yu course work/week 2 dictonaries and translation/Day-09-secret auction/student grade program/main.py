student_scores = {
    "Noor" : 90,
    "sarah" : 85,
    "ali" : 78,
    "mohamed" : 92,
    "aarav" : 45,
}
student_grades = {}


for student in student_scores :
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "good"
    elif score> 50:
        student_grades[student]  ="Needs to improve"
    else:
        student_grades[student] = "Fail"
    

print(student_grades)       
    


