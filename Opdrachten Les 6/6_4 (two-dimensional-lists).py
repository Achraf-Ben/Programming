studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
from statistics import mean

def gemiddelde_per_student(studentencijfers):
    antw = []
    for lijstNummer in range(len(studentencijfers)):
        student = studentencijfers[lijstNummer]
    for student in studentencijfers:
        gemiddeldeStudent = sum(student) / len(student)
        antw.append(gemiddeldeStudent)
    return antw

def gemiddelde_van_alle_student(studentencijfers):
    x = gemiddelde_per_student(studentencijfers)
    antw = mean(x)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_student(studentencijfers))