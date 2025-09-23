#working with variables

    # Assigning Data
student_name = "mona"
student_age = 20
student_gpa = 9.5
student_passed = True

# Retrieve Data
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)

# Get Identity / Memory Address
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))

# Get Type Of Data
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))

# In python a variable can change during the execution 
dynamic_data = 10
print(type(dynamic_data))
dynamic_data = "10"
print(type(dynamic_data))
dynamic_data = 10.0
print(type(dynamic_data))
dynamic_data = True
print(type(dynamic_data))

# Python memory model

a = 10
print(id(a))
b = 20
print(id(b))
c = 10
print(id(c))

# Note : 