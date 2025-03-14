print("You have 2 options: ")
print ("1. A car")
print ("2. A bike")

choice = int(input("Select your ride."))

if (choice == 1):
    print ("What kind of car?")
    print ("1. Sudan")
    print ("2. SUV")
    ride =  int(input("Choose your car?"))
    if (ride == 1):
      print ("You have chosen a Sudan.")
    else:
      print ("You've chosen a SUV.")
elif (choice == 2 ):
   print ("What kind of bike?")
   print ("1. A scooter")
   print ("2. A motorbike")
   ride2 = int(input("Choose your bike."))
   if (ride2 == 1):
      print ("You have choosen a scooter.")
   else:
      print ("You've choosen a motorbike.")
else:
   print ("Invalid answer!")