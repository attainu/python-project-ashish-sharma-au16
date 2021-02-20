from parking_lot_managment import ParkingLot


class File:

    def __init__(self):

        self.obj = ParkingLot()

    def Create_Parking(self, capacity):
        user_input = list(capacity.split())
        size = int(user_input[1])
        self.obj.CreateParkingLot(size)

    def display(self, capacity):

        User_Input = capacity

        self.obj.display(User_Input)
