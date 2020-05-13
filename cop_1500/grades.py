def grade_avg(grade1:float, grade2:float , grade3:float) -> float :
    """take three parameters(grades one two and three) and return the average. grades should range from 0 to 100"""

    return (grade1 + grade2 + grade3) / 3

print (grade_avg(80, 90, 95))
print (grade_avg(80, 80, 80))
#print (grade_avg("A","B","C"))
#print(help(grade_avg))

#take four grades and return the average of the top three
import math
def top_avg(grade1:float, grade2:float , grade3:float, grade4:float) -> float:
    """input grade1, grade2, grade3, grade4, output average of top three"""
    a = min(grade1, grade2, grade3, grade4)

    return (grade1 + grade2 + grade3 + grade4 - a) / 3

print (top_avg(80, 80, 80, 80)) #80
print (top_avg(80, 85, 90, 95)) #90
print (top_avg(85, 90, 95, 80)) #90
print (top_avg(90, 95, 80, 85)) #90
print (top_avg(95, 80, 85, 90)) #90