import pickle
import os
from datetime import datetime

file_name = "attendance.dat"

# Load data if file exists
if os.path.exists(file_name):
    with open(file_name, "rb") as f:
        attendance = pickle.load(f)
else:
    attendance = {}

while True:
    print("\n----- Attendance System -----")
    print("1. In Time")
    print("2. Out Time")
    print("3. View Records")
    print("4. Exit")

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

        for name, details in attendance.items():
            print("\nStudent Name:", name)
            print("Batch:", details["Batch"])
            print("In Time:", details["In Time"])
            print("In Sign:", details["In Sign"])
            print("Out Time:", details["Out Time"])
            print("Out Sign:", details["Out Sign"])

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")
