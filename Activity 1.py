med_cause = input("Did you have any medical emergencies? ")
atten = int(input("enter the attendance of the student."))

if med_cause == "Yes":
    print ("You are allowed in.")
else:
    if atten>=75: 
        print ("You are allowed in.")
    else: 
        print ("You can't come in.")
    