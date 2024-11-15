import pandas as pd
import main_functions

df=pd.read_excel("student_data.xlsx", engine="openpyxl")

initial_ques=input("\nDo want to have a 'Meal' or want to chack the 'Balanace'?\n").title()
if initial_ques=="Balance":
    main_functions.check_balance()
else:
    print("\nHello, Welcome to the Veg Mess\n")
    input_name=input("\nEnter your name here:\n").title()
    input_enrollment=input("\nEnter your enrollment number here.\n").upper()

    if input_name not in df["Name"].values or input_enrollment not in df["Enrollment"].values:
        reg_que=input("\nYou are not registered in this mess already.\nDo you want to register?\n").title()
        if reg_que == "No":
            print("\nSorry, but you are not allowed to eat in this mess.\nThank You\n")
        else:
            main_functions.new_registration()

    else:
        df.loc[df["Enrollment"]==input_enrollment, "Attendence"]+=1
        df.loc[df["Enrollment"]==input_enrollment, "Balance Remaining (in Rs)"]=(27000-((df.loc[df["Enrollment"]==input_enrollment, "Attendence"])*150))
        df.to_excel("student_data.xlsx", sheet_name="Sheet1", index=False)
        print("\nYour attendence is done for today.\nPlease take the palte.\n")

    balance_req=input("\nDo you want to check the balance?\n").title()
    if balance_req=="Yes":
        main_functions.check_balance()
    else:
        print("\nThank You\n")
