import pandas as pd
import numpy as np

# Create a DataFrame

d = {  # Creating a dict for dataframe
    'StudentName': ['Harrison', 'Jake', 'Jake', 'Hayley'],
    'Score': [64, 68, 61, 86]}

df = pd.DataFrame(d)  # converting dict to dataframe
# Keys get converted to column names and values to column values
# get grade by adding a column to the dataframe and apply np.where(), similar to a nested if

df['Grade'] = np.where((df.Score < 60),
                       'F', np.where((df.Score >= 60) & (df.Score <= 69),
                                     'D', np.where((df.Score >= 70) & (df.Score <= 79),
                                                   'C', np.where((df.Score >= 80) & (df.Score <= 89),
                                                                 'B', np.where((df.Score >= 90) & (df.Score <= 100),
                                                                               'A', 'No Marks')))))
print(df)

# T_marks = 1100
# data = {}
# while True:
#     ask = input("What do you want? ")
#     if ask == "y":
#         name = input("Enter your name: ")
#         marks = int(input("Enter marks: "))
#         data[name] = marks
#     elif ask == "print":
#         for (key,value) in data.items():
#             percentage =(value / T_marks) * 100
#             print(key,"::",value)
#             if percentage >= 90:
#                 print("Passed with A grade")
#             elif 90 > percentage >= 70:
#                 print("Passed with B grade")
#             elif 70 > percentage >= 60:
#                 print("Passed with C grade")
#             elif 60 > percentage >= 50:
#                 print("passed with D Grade")
#             else:
#                 print("You failed")
#     else:
#         print("Your work has ended")
#         break

# student = []
# student_1=[]
# score = []
# copy = []
# loop = True
# yes = ["YES","yes","y","Y"]
# while loop:
#     Name = input("Name : ")
#     Score = int(input("Score : "))
#     student.append(Name)
#     score.append(Score)
#     copy.append(Score)
#     Enter_more = input("Write YES or Y or y or yes to add more names: ")
#     if Enter_more in yes:
#         continue
#     else:
#         break
# score.sort()
# score.reverse()
# sum = 0
# for i in range(len(score)):
#     index = score[i]
#     student_1.append(student[copy.index(index)])
#     sum+=score[i]
#     score[i] = student[i]
# print("Average Score is "+str(float(sum/len(score))))
# print("Highest Score is Scored by  "+str(student_1[0]))
# print("Lowest Score is Scored by "+str(student_1[len(student_1)-1]))
