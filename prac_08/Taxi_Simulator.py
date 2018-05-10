"""
Allow user to select taxi from a list of taxis, ride them and quit.
"""

def main():
    from prac_08.taxi import Taxi
    from prac_08.silver_service_taxi import SilverServiceTaxi

    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [prius, limo, hummer]
    total_bill = 0
    print("Let's drive!")

    is_running = True
    while is_running is True:
        user_input = get_input("q)uit, c)hoose taxi, d)rive")

        if user_input.lower() == "q":
            is_running = False
            print("Total trip cost: ${:.2f}".format(total_bill))
            print("Taxis are now: ")
            for taxi in taxis:
                print(taxi.__str__())

        elif user_input.lower() == "c":

            is_correct = False
            for index, taxi in enumerate(taxis):
                print("{} - {}".format(index, taxi.__str__()))

            while is_correct is False:
                user_input = get_input("Choose taxi.")
                try:
                    if int(user_input) < 0:
                        print("Invalid input")
                    elif int(user_input) >= len(taxis):
                        print("Invalid input")
                    else:
                        selected_taxi = taxis[int(user_input)]
                        print("Bill to date: ${:.2f}".format(total_bill))
                        is_correct = True

                except ValueError:
                    print("Invalid input")

        elif user_input.lower() == "d":

            is_correct = False

            while is_correct is False:
                user_input = get_input("Drive how far?")

                try:
                    if int(user_input) >= 0:
                        selected_taxi.drive(int(user_input))
                        total_bill = total_bill + selected_taxi.get_fare()
                        is_correct = True
                        print("Your {} trip cost you ${:.2f}".format(selected_taxi.name, selected_taxi.get_fare()))
                        print("Bill to date: ${:.2f}".format(total_bill))
                        selected_taxi.start_fare()

                    else:
                        print("Distance cannot be negative")

                except ValueError:
                    print("Invalid input")

                except UnboundLocalError:
                    is_correct = True
                    print("No taxi selected")

        else:
            print("Invalid input")


def get_input(prompt):
    print(prompt)
    user_input = input(">>> ")
    return user_input


main()
