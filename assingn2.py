#Checking process for flight travel

def Ticket_checking():
    Ticket_checking=input("Is the Ticket is valid?:")
    if Ticket_checking=='yes':
            print("Your ticket is valid and go to Covid19 checking")
            Covid19_checking()
    else:
            print("Sorry your ticket is invalid")
def Covid19_checking():
    Covid19_checking=input("Is the person have Covid19 Positive?:")
    if Covid19_checking=='yes':
        print("Sorry you have Covid19 Positive and u r not allowed to travel ")
    else:
        print("All good!! you have Covid19 Negative and go to check the Inegration process")
        Inegration_checking()
def Inegration_checking():
    Inegration_checking=input("Is the full Inegration process were completed successfully?:")
    if Inegration_checking=='yes':
        print("Your successfully passed in Inegration process  go to the Bag weight process")
        Bagweight_checking()
    else:
        print("You have some issues in your passport or visa or any case filed in your name so u r not elligle ")
def Bagweight_checking():
    Bagweight_checking=int(input("Enter the Bag weight:"))
    if Bagweight_checking>=20:
        print("your are not allowed to carry a things upto 20KG so pls withdraw somethings")
    else:
        print("Your things are under the weight of 20kg so you can carry your things withyou")
        Boardingpass_checking()
def Boardingpass_checking():
    print("All the verifications are done \n **Have a nice journey!!!**")
Ticket_checking()