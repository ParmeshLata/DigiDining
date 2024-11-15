
# **DigiDining**  

## **Overview**  
The Digital Mess Management System is a Python-based application designed to streamline and digitize mess operations. It leverages student data to manage meal access, ensuring a seamless and secure process for both registered and unregistered users.  

## **Features**  
- **Student Authentication**: Welcomes registered students to access mess facilities.  
- **Registration System**: Allows unregistered students to sign up for mess services.  
- **Password Protection**: Ensures all user interactions are secure and confidential.  
- **User-Friendly Interface**: Simplifies operations for mess staff and students.  
- **Proper Data Management**: Manages the data of stuents like their attendence, balance remaining and much more.

## **How It Works**  
1. A student enters their credentials.  
2. The system checks if the student is already registered.  
   - If registered, the student is welcomed to enjoy their meal.  
   - If not registered, the system prompts for new registration.  
3. The attendence is done after the proper identification of student.
4. The charge is deducted after the attendece is done.
5. The balance is updated with every attendece.
6. All data and interactions are protected with password security.  

## **Installation**  
1. **Prerequisites**:  
   - Python 3.x installed on your machine.  
   - Required Pandas Python library  (install using `pip install pandas`).  
   - Required Excel connectivity.
     
2. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-repo/digital-mess-management.git  
   cd digidining  
   ```  

3. **Run the Application**:  
   ```bash  
   python main_workplace.py  
   ```  

## **Usage**  
- Run the file in IDE and follow the on-screen instructions.  
- Enter your student details to log in or register as needed.  
- Ensure you have your password handy for authentication.  

## **Folder Structure**  
```
digital-mess-management/  
│  
├── main_workplace.py                 # Main application file  
├── student_data.xlsx                 # Excel database (contains student's data)  
├── main_functions.py                 # Module containing functions and helpers   
├── README.md                         # This file  
└── requirement.txt                   # List of required Python libraries  
```  

## **Technologies Used**  
- **Python**: Core programming language.  
- **Microsoft Excel**: For data storage.  
- **Any IDE**: To run the program file. 

## **Contact**  
For any queries or feedback, feel free to contact:  
- **Email**: lataayush6@gmail.com  
- **GitHub**: https://github.com/ParmeshLata
