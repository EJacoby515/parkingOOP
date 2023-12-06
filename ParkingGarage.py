import time
class ParkingGarage:

    def __init__(self, initial_park_space, initial_numb_tik):
        self.initial_park_space = initial_park_space
        self.initial_numb_tik = initial_numb_tik
        self.park_tik_numb = 0
        self.paid_tiks = []

    def takeTicket(self):
        while True:
            take_tik = input("Wanna park here? Take a ticket\n($20 flat rate up to 24hrs): ('y'/'n')")
            if take_tik.lower() == 'y':
                self.initial_park_space -= 1
                self.initial_numb_tik -= 1
                self.park_tik_numb += 1
                tickets.append(self.park_tik_numb)
                parking_spots.append(self.initial_park_space)
                print("Here's your ticket, enjoy your day!")
                print("Available parking spaces:", self.initial_park_space)
                print("Remaining Tickets:", self.initial_numb_tik)
                print("Ticket Number: OOP - {} - CT".format(str(self.park_tik_numb + 100)))
                current_ticket.update({"tik_num": self.park_tik_numb})
                print(current_ticket)
                self.leaveGarage()

            elif take_tik.lower() == 'n':
                print("Have a nice day, good luck parking someplace else.")
                print("Available parking spaces:", self.initial_park_space)
                print("Remaining Tickets:", self.initial_numb_tik)
                break
            else:
                print("Invalid option, try again")

    def leaveGarage(self):
        time.sleep(1)
        r2L = input("Are you ready to leave? : ('y'/'n')\n")
        if r2L.lower() == 'y':
            self.payForParking()
        elif r2L.lower() == 'n':
            print("Please let me know when you're ready to leave.")
            self.leaveGarage()
        else:
            print("Invalid option, try again")

    def payForParking(self):
        pFP = input("Do you want to pay at the payment Terminal or the Gate?:('t'/'g')\n")
        if pFP.lower() == 't':
            time.sleep(1)
            print("Thank you! I hope you have a wonderful day!")
            print("You have 15 minutes to leave the garage")
            self.paid_tiks.append(self.park_tik_numb)
            self.initial_park_space += 1  
            self.initial_numb_tik += 1
            print("Available parking spaces:", self.initial_park_space)
            print("Remaining Tickets:", self.initial_numb_tik)
        elif pFP.lower() == 'g':
            print("Please go pay at the gate, Thank you")
            time.sleep(1)
            payGate = input("Did you pay at the gate?: ('y'/'n'): \n")
            if payGate.lower() == 'y':
                time.sleep(1)
                print('Thank you! Have a great day!')
                print("Ticket Number:", str(self.park_tik_numb))
                print("===========================")
                print("===========================")
                print("END OF DAY COUNT")
                self.paid_tiks.append(self.park_tik_numb)
                self.initial_park_space += 1  
                self.initial_numb_tik += 1
                print("Remaining parking spaces:", self.initial_park_space)
                print("Remaining Tickets:", self.initial_numb_tik)
            elif payGate.lower() == 'n':
                self.leaveGarage()
            else:
                print("Invalid option, try again")
initial_park_space = 200
initial_numb_tik = 200

tickets = []
parking_spots = []
current_ticket = {
    "tik_num": ""
}

parking_Machine = ParkingGarage(initial_park_space, initial_numb_tik)

parking_Machine.takeTicket()

# print("Paid Tickets:", parking_Machine.paid_tiks)
