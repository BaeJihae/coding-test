grade = {'A+':4.5, 'A0':4.0,'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

grade_sum = 0
total_grade_sum = 0

for _ in range(20):
    subject_grade = input().split()
    if subject_grade[2] == 'P':
        continue
    else:
        total_grade_sum += float(subject_grade[1])
        grade_sum += float(subject_grade[1]) * grade[subject_grade[2]]

print(grade_sum/total_grade_sum)