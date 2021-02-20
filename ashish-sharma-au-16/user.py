from parking_lot_managment import ParkingLot


class user:

    def __init__(self):
        self.obj = ParkingLot()

    def Create_Parking(self):
        User_Input = list(input("Create a parking lot :").split())
        size = int(User_Input[1])
        self.obj.CreateParkingLot(size)

    def display(self):

        temp = "True"

        while temp == "True":
            User_Input = input()
            if User_Input == "exit":
                temp = "False"
                break
            else:
                self.obj.display(User_Input)
