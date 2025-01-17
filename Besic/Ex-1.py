# We check in a patient named jhon smith
# He is 20 years old
# He is a new patient

name = "Jhon Smith"
age = int(20)
new_patient = True

print("we check in a patient named: " + name,
    "Age is: " + str(age) + "years Old",
    "He is a new patient" if new_patient else "He is not a new patient")