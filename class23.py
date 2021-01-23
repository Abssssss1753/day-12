####  Calculate the total marks and find the grade #####
################################## Using Functions ##############################33
"""
def find_average_mark(marks):

    sum_of_marks=sum(marks)
    total_marks=len(marks)
    average_marks=sum_of_marks/total_marks
    return average_marks

def compute_grade(grade):

    if average_marks >= 80:
        grade="A"
    elif average_marks >= 60:
        grade="B"
    elif average_marks >= 50:
        grade="C"
    else:
        grade="F"
    return grade

marks = [55,64,75,80,65]
average_marks=find_average_mark(marks)
print("Average of your marks",average_marks)

grade = compute_grade(average_marks)
print("your grade is",grade)
"""


"""################################### add_number using FUNCTION ###################
def add_numbers(a,b):
    result = a+b
    return result
print("Enter first number")
num1=int(input())
print("Enter second number")
num2=int(input())

result = add_numbers(num1,num2)
print("Addition of two number is",result)

###################################### mul_number using FUNCTION ############################
def mul_numbers(a,b):
    result = a*b
    return result
print("Enter first number")
num1=int(input())
print("Enter second number")
num2=int(input())

result = mul_numbers(num1,num2)
print("Multiplication of two number is ",result)

"""
