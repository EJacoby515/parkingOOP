import time
class ParkingGarage:

    def __init__(self, parkingSpace):
        self.tickets = list(range(1, parkingSpace + 1))
        self.parking_spots = list(range(1, parkingSpace + 1))
        self.current_ticket = {}



    def takeTicket(self):
        while True:
            take_tik = input("Wanna park here? Take a ticket\n($20 flat rate up to 24hrs): ('y'/'n')")
            if take_tik.lower() == 'y':
                parking_spot = self.parking_spots.pop(0)
                self.current_ticket = {"ticket_number": self.tickets.pop(0), "paid": False}
                print("Here's your ticket, enjoy your day!")
                print(f"You pulled Ticket Number : {self.current_ticket['ticket_number']}")
                print(f"Available parking spaces:", len(self.parking_spots))
                print(f"Remaining Tickets:, {len(self.tickets)}")

                self.leaveGarage()

            elif take_tik.lower() == 'n':
                print("Have a nice day, good luck parking someplace else.")
                print("Available parking spaces:", len(self.parking_spots))
                print("Remaining Tickets:", len(self.tickets))
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
            self.current_ticket['paid'] = True
            self.parking_spots.append(0)  
            self.tickets.append(self.current_ticket["ticket_number"])
            print("Available parking spaces:", len(self.parking_spots))
            print("Remaining Tickets:", len(self.tickets))
        elif pFP.lower() == 'g':
            print("Please go pay at the gate, Thank you")
            time.sleep(1)
            payGate = input("Did you pay at the gate?: ('y'/'n'): \n")
            if payGate.lower() == 'y':
                time.sleep(1)
                print('Thank you! Have a great day!')
                print("Ticket Number:", str(self.current_ticket["ticket_number"]))
                print("===========================")
                print("===========================")
                print("END OF DAY COUNT")
                self.current_ticket['paid'] = True
                self.parking_spots.append(0)
                self.tickets.append(self.current_ticket["ticket_number"])
                print("Remaining parking spaces:", len(self.parking_spots))
                print("Remaining Tickets:", len(self.tickets))
            elif payGate.lower() == 'n':
                self.leaveGarage()
            else:
                print("Invalid option, try again")



parking_Machine = ParkingGarage(parkingSpace=200)

parking_Machine.takeTicket()

