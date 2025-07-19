marks = float(input("Enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks < 50:
    print("Fail")
elif marks < 70:
    print("Satisfactory")
elif marks < 80:
    print("Good")
elif marks < 90:
    print("Very good")
else:
    print("Excellent")
