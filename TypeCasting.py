# Typecasting = the process of converting a variable from one data type to another
# str(), int), float(), bool()

first_name="Priyanshu Bandyopadhyay"
age=25
gpa=9.06
is_indian=True

print(f"GPA is {gpa} and type of GPA is {type(gpa)}")
newGpa=int(gpa) # truncates the decimal part
print(f"GPA is {newGpa} and type of GPA is {type(newGpa)}")

a1=1
b1=0
c1=""
a2=bool(a1)
b2=bool(b1)
c2=bool(c1)
print(a2) # True
print(b2) # False
print(c2) # False