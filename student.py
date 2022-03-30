# Write a program to ask a student for their
# percentage mark and convert this to a grade.
score=float(input("Please, enter your score:  "))
target_grade=input("Please enter your target grade:  ")

if score >= 90 and score <= 100:
    print("Your grade is 'A'.")
elif score >= 80:
    print("Your grade is 'B'.")
elif score >= 70:
    print("Your grade is 'C'.")
elif score >=60:
    print("Your grade is 'D'.")
elif score >= 50:
    print("Your grade is 'E'.")
elif score <= 49 and score >= 0:
    print("Your grade is 'F'.")
else :
    print("Invalid grade. Please insert grade between 0-100")

# score_a_range=([90],[100])
# score_b_range=([80],[89])
# score_c_range=([70],[79])
# score_d_range=([60],[69])
# score_e_range=([50],[59])

# if target_grade == "A":
#
#     print("Your grade is 'A'.")
# elif target_grade >= 80:
#     print("Your grade is 'B'.")
# elif target_grade >= 70:
#     print("Your grade is 'C'.")
# elif target_grade >= 60:
#     print("Your grade is 'D'.")
# elif target_grade >= 50:
#     print("Your grade is 'E'.")
# elif target_grade <= 49 and target_grade >= 0:
#     print("Your grade is 'F'.")
# else:
#     print("Invalid grade. Please inser grade between 0-100")


