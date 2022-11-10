'''
The record of a student (Name, Roll No., Marks in five subjects and percentage of
marks) is stored in the following list: stRecord = ['Raman','A-36',[56,98,99,72,69],78.8]
Write Python statements to retrieve the following information from the list stRecord.
a) Percentage of the student
b) Marks in the fifth subject
c) Maximum marks of the student
d) Roll no. of the student
e) Change the name of the student from ‘Raman’ to ‘Raghav’
'''

record = ['Raman','A-36',[56,98,99,72,69],78.8]
percentage = record[3]
marks = record[2]
max_marks = max(record[2])
roll_no = record[1]
record[0] = "Raghav"
name = record[0]

print(f"neme: {name}, Percentage: {percentage}, Max marks: {max_marks}, roll no: {roll_no}, marks: {marks}")


