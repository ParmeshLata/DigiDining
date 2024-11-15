import pandas as pd
df=pd.read_excel("student_data.xlsx", engine="openpyxl")
df_len=len(df)

## NEW REBISTRATION
def new_registration():
    reg_name=input("\nEnter your name here for registration.\n").title()
    df.loc[df_len, "Name"]=reg_name
    reg_enrollment=input("\nEnter your enrollment number here.\n").upper()
    df.loc[df_len, "Enrollment"]=reg_enrollment
    reg_gender=input("\nEnter your gender.\n").title()
    df.loc[df_len, "Gender"]=reg_gender
    reg_number=input("\nEnter your contact number.\n")
    df.loc[df_len, "Contact Number"]=reg_number
    reg_hostel=input("\nEnter your hostel name.\n").title()
    df.loc[df_len, "Hostel Name"]=reg_hostel
    reg_room=input("\nEnter your room number.\n")
    df.loc[df_len, "Room Number"]=reg_room
    df.loc[df_len, "Submitted Amount (in Rs)"]=(27000)
    df.loc[df_len, "Attendence"]=(0)
    reg_password=input("\nCreate your own password.\n")
    df.loc[df["Enrollment"]==reg_enrollment, "Password"]=reg_password
    df.to_excel("student_data.xlsx", sheet_name="Sheet1", index=False)
    df.loc[df_len, "Attendence"]+=1
    df.loc[df["Enrollment"]==reg_enrollment, "Balance Remaining (in Rs)"]=(27000-(df.loc[df["Enrollment"]==reg_enrollment, "Attendence"]*150))
    df.to_excel("student_data.xlsx", sheet_name="Sheet1", index=False)
    print("\nYour registration to this mess is done.\nYour attendance is done for today.\nPlease take the plate.\n")


## CHECKING THE BALANCE
def check_balance():
    i=1
    name_check=input("\nEnter your full name here.\n").title()
    enrollment_check=input("\nEnter your enrollment number\n").upper()
    password_check=input("\nEnter your password here.\n")
    correct_password=df.loc[df["Enrollment"]==enrollment_check, "Password"].values
    while password_check!=correct_password and i<3:
        print(f"\nWrong password.\nYou have got {3-i} more chances.\n")
        i+=1
        password_check=input("\nEnter your password here.\n")
    if password_check==correct_password:
        attendence=(df.loc[df["Enrollment"]==enrollment_check, "Attendence"].values)
        balance=(df.loc[df["Enrollment"]==enrollment_check, "Balance Remaining (in Rs)"].values)
        print(f"\nYour attendence is {attendence}.\nYour remaining balance is Rs {balance}.\n")
    else:
        print("\nYou have exceeded the maximum limit of the trials.\n")