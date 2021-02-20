from user import user
from input.input_process import File

if __name__ == "__main__":

    print("NOTE-: case sensitive")
    print("1. type [MANUAL] .\n 2.type [FILE] input file")
    interaction_with_user = input("write MANUAL or FILE to choose from them :")
    print()
    manual = user()
    auto = File()

    if interaction_with_user == "MANUAL":
        cnt = 0
        while cnt < 2:
            if cnt == 0:
                manual.Create_Parking()
                cnt += 1
            else:
                manual.display()
                cnt += 1        

    elif interaction_with_user == "FILE":
        print("file - S:\ashish-sharma-au-16\input\input_instruction.txt")
        file_address = input("file location please :")
        f = open(file_address, "r")
        cnt = 0
        for row in f:
            if cnt == 0:
                auto.Create_Parking(row)
                cnt += 1
            else:
                auto.display(row)
