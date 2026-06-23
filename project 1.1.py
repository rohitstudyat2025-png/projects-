'''
import pickle

attendance = {}

with open("attendance.dat", "wb") as f:
    pickle.dump(attendance, f)

print("File created")
'''
import pickle
from datetime import datetime

file_name = "attendance.dat"

with open(file_name , "rb") as f:
    attendance = pickle.load(f)

while True:
    print("\n----- Attendance System -----")
    print("1) In Time.")
    print("2) Out Time.")
    print("3) View Records.")
    print("4) Exit.")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        batch = input("Enter Batch Name: ")
        sign = input("Enter Signature: ")

        attendance[name] = {
            "Batch": batch,
            "In Time": datetime.now().strftime("%H:%M:%S"),
            "In Sign": sign,
            "Out Time": "",
            "Out Sign": ""
        }

        with open(file_name, "wb") as f:
            pickle.dump(attendance, f)

        print("In Time Recorded Successfully!")

    elif choice == "2":
        name = input("Enter Student Name: ")

        if name in attendance:
            attendance[name]["Out Time"] = datetime.now().strftime("%H:%M:%S")
            attendance[name]["Out Sign"] = input("Enter Signature: ")

            with open(file_name, "wb") as f:
                pickle.dump(attendance, f)

            print("Out Time Recorded Successfully!")
        else:
            print("Student Record Not Found!")

    elif choice == "3":
        print("\nAttendance Records")

        for name in attendance:
            print("\nStudent Name:", name)
            print("Batch:", attendance[name]["Batch"])
            print("In Time:", attendance[name]["In Time"])
            print("In Sign:", attendance[name]["In Sign"])
            print("Out Time:", attendance[name]["Out Time"])
            print("Out Sign:", attendance[name]["Out Sign"])

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")
