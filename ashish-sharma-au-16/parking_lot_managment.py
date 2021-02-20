class ParkingLot():

    def __init__(self):
        self.slots = list()

    def CreateParkingLot(self, size):

        for slot in range(size):
            self.slots.append([slot + 1])

        print(f"Created a parking lot with {size} slots")

    def display(self, Information):

        info = list(Information.split())

        if info[0] == 'park' and len(info) == 3:
            temp = "False"

            for i in range(len(self.slots)):
                if len(self.slots[i]) == 1:
                    self.slots[i].append(info[1])
                    self.slots[i].append(info[2])
                    print(f"Allocated slot number: {self.slots[i][0]}")
                    temp = "True"
                    break
            if temp == "False":
                print("Parking lot is full, Sorry For Inconvinience")

        elif info[0] == "leave":
            res = (self.slots[int(info[1])-1])
            if len(res) > 1:
                while len(res) != 1:
                    res.pop(1)
                print(f"Slot no {info[1]} is free")
            else:
                print(f"Slot no {info[1]} was already empty")

        elif info[0] == "status":
            print("Slot No. Registration No Colour ")
            for i in self.slots:
                if len(i) == 3:
                    for j in i:
                        print(j, end=" ")
                    print()

        elif info[0] == "registration_numbers_for_cars_with_colour":
            if len(info) == 2:
                car_colour = info[1]
                arr = list()
                for i in range(len(self.slots)):
                    if car_colour in self.slots[i]:
                        arr.append(self.slots[i][1])

                for j in arr:
                    if j == arr[-1]:
                        print(j)
                    else:
                        print(j, end=(","))

        elif info[0] == "slot_numbers_for_cars_with_colour":
            if len(info) == 2:

                car_colour = info[1]
                arr = []
                for i in range(len(self.slots)):
                    if car_colour in self.slots[i]:
                        arr.append(self.slots[i][0])
                    else:
                        print("not found")

                for j in arr:
                    if j == arr[-1]:
                        print(j)
                    else:
                        print(j, end=(","))

        elif info[0] == "slot_number_for_registration_number":
            if len(info) == 2:
                for i in range(len(self.slots)):
                    if info[1] in self.slots[i]:
                        print(self.slots[i][0])
                        break
                else:
                    print("Not Found")
