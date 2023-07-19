from datetime import datetime


class Donation:
    def __init__(self, name, dType, quantity, date):
        self.name = name
        if dType == 1:
            self.dType = "Money"
        elif dType == 2:
            self.dType = "Food"
        else:
            self.dType = "Clothes"
        self.quantity = quantity
        self.date = date


class DonationManager:
    def __init__(self):
        self.donations = []
        self.inventory = {"Money": 0, "Food": 0, "Clothes": 0}
        self.donors = {}

    def register(self, donation: Donation):
        self.donations.append(donation)
        if donation.name not in self.donors:
            self.donors[donation.name] = [0, 0, 0]

        if donation.name in self.donors:
            if donation.dType == "Money":
                print("added money: ", donation.quantity, " to ", donation.name)
                self.donors[donation.name][0] += donation.quantity
            elif donation.dType == "Food":
                print("added food: ", donation.quantity, " to ", donation.name)
                self.donors[donation.name][1] += donation.quantity
            else:
                print("added clothes: ", donation.quantity, " to ", donation.name)
                self.donors[donation.name][2] += donation.quantity

    def print_registration(self):
        donation = self.donations[-1]

        print("\nHere is your summarized registration: ")
        print("Date: ", donation.date)
        print("Donor: ", donation.name)
        print("Donation Type: ", donation.dType)

        if donation.dType == "Money":
            print("Quantity: $", donation.quantity)
        elif donation.dType == "Food":
            print("Quantity: ", donation.quantity, " lbs")
        else:
            print("Quantity: ", donation.quantity)

    # Print logs of donations
    def log_donations(self):
        print("Date               |       Donor       |    Donation    |    Amount    ")
        for donation in self.donations:
            if donation.dType == "Money":
                quantity = "$" + str(donation.quantity)
            elif donation.dType == "Food":
                quantity = str(donation.quantity) + " lbs"
            else:
                quantity = str(donation.quantity)

            print(donation.date, donation.name.center(19), donation.dType.center(16), quantity.center(14))

    # Give report
    def generate_report(self, report_type):
        if report_type == "inventory":
            self.get_inventory()
            for k, v in self.inventory.items():
                if k == "Money":
                    print("Money: $", v)
                elif k == "Food":
                    print("Food: ", v, " lbs")
                else:
                    print("Clothes: ", v)
        else:
            print("       Donor       |    Money    |    Food    |   Clothes   ")
            for k, v in self.donors.items():
                print(k.center(19),
                      ("$" + str(v[0])).center(13),
                      (str(v[1]) + " lbs").center(12),
                      str(v[2]).center(13))

    # Get current status of inventory
    def get_inventory(self):
        for donation in self.donations:
            self.inventory[donation.dType] += donation.quantity


def main():
    donation_manager = DonationManager()
    finished = False

    # Keep doing menu until user is finished using
    while not finished:
        ################################# Prompt #################################
        print("Hello, what would you like to do today? ")
        print("1. Register a donation")
        print("2. See donations")
        print("3. Get Report")

        # Input validation
        def get_user_choice():
            while True:
                choice = input("Please provide input number: ")

                if choice == "1" or choice == "2" or choice == "3":
                    return choice

                print("Please use input 1, 2, or 3 only")

        val = int(get_user_choice())

        ############################ Register Donation ############################
        """
        Donation Registration: A feature that allows the shelter staff to 
        record details of the donations, such as the donor's name, type of donation 
        (money, food, clothing, etc.), quantity or amount donated, and the date of 
        the donation.
        """
        if val == 1:
            print("\nGreat! You chose to register a donation!")
            print("Please fill in the form: ")
            dname = input("Donor Name: ")
            print("1. Money\n"
                  "2. Food\n"
                  "3. Clothing")

            dtype = int(input("Type of donation: "))

            if dtype == 1:
                quantity = input("Amount: $")
            elif dtype == 2:
                quantity = input("weight: ")
            else:
                quantity = input("number of clothing: ")

            # Add to donation list
            donation_manager.register(Donation(
                dname,
                dtype,
                int(quantity),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )

            # Print "receipt"
            donation_manager.print_registration()

        ############################## See Donations ##############################
        """
        Donation Distribution: A feature to log when and how much of the donations 
        are distributed, capturing the type of donation, quantity or amount 
        distributed, and the date of distribution.
        """
        if val == 2:
            print("\nGreat! You chose to see donations!")
            print("")
            donation_manager.log_donations()

        ############################## See Reports ##############################
        """
        Donation Reports: Your solution should have the capacity to generate two 
        types of reports: (1) An inventory report displaying the current status 
        of donations, grouped by type. (2) A donor report, summarizing the 
        total contributions received from each donor.
        """
        if val == 3:
            print("\nWhich would you like to see: \n"
                  "1. Inventory\n"
                  "2. Donor Report\n")
            report = int(input("I would like to see: "))

            if report == 1:
                print("\nGreat! You chose to see our inventory!")
                donation_manager.generate_report("inventory")
            else:
                print("\nGreat! You chose to see our donor report!")
                donation_manager.generate_report("donor")

        choice = input("\nAre you finished? (y/n): ")
        finished = True if choice == "y" else False

        print("\nThank you for using our service!\n"
              "Have a good day!")


if __name__ == "__main__":
    main()
