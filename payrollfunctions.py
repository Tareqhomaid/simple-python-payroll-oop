from classes import *
import random
import files
import datetime

file = files.dirs()  # data samples for employee
mngrfiles = files.mngrdir()  # data samples for manager
red = '\033[31;1m'  # coloring red
re = '\033[m'  # reset coloring
employees = {j: Employee(*[random.choice(file[i]) for i in file.keys()]) for j in range(1, 10)}
managers = {j: Manager(*[random.choice(mngrfiles[i]) for i in mngrfiles.keys()]) for j in range(1, 3)}


def salarymod(ch,add):#manager function to edit salary
    if ch == "add":
        setnew = int(input("How much you want to add? "))
        Manager.AddSalary(employees[add],setnew)
    elif ch == "del":
        Manager.DeleteSalary(employees[add])
    elif ch == "edit":
        setnew = int(input("How much you want to add? "))
        Manager.EditSalary(employees[add],setnew)
    else:
        print("Wrong Choice")


def mngr():
    choices = {
        "1": Manager.veiwemp(managers[1], employees),
        "2": Manager.GiveRise,
        "3": salarymod
    }
    while True:

        print(f"""
    ***************************************************
    *           {red}Payroll System{re}                        *
    *                                                 *
    *                                                 *
    *	            Welcome {red}Manager{re}         		  *
    *					                        	  *
    *            here's what you can do :             *
    *  {red}*Write the function's number to use it*{re}        *
    *					                        	  *
    *    1 : view all employees                       *
    *    2 : Give a pay rise to an employee           *
    *	 3 : salary modification			          *
    *	        	AND			                  	  *
    *    4 : To exit to main menu                     *
    *                                                 *
    ***************************************************""")
        option = input(red + "\nChoose a function : " + re)
        if option in choices:
            if option == "1":
                for i in choices[option]:
                    print(i)
            elif option == "2":

                empnum = int(input("what is the number of the employee you want to give a rise? "))
                print(f"You chose the employee number {empnum}, and his name is:{employees[empnum].FirstName} his current salary is : {employees[empnum].salary }")
                rise = int(input("Enter the amount to add: "))
                Manager.GiveRise(employees[empnum],rise)
                print(f"the new salary for {employees[empnum].FirstName} is {employees[empnum].salary}")

            elif option == "3":
                add = int(input("Enter the number for the employee you want: "))
                print(f"You chose the employee number {add}, and his name is:{employees[add].FirstName} his current salary is : {employees[add].salary}")
                ch = input("Write what you want to do: (add, del, edit) ")
                salarymod(ch, add)
                print(f"the new salary for {employees[add].FirstName} is {employees[add].salary}")

        elif option == "4":
            break
        else:
            print(f"{red}Wrong choice{re}")

def emp():
    choices = {
        "1": employees,
        "2": Employee.CheckIn,
        "3": Employee.ChekOut,
        "4": Employee.Withdraw,
        "5": Employee.EditPersonalDetails
    }
    num = int(input("\nwhats your employee number?"))
    while True:

        print(f"""
    ***************************************************
    *           {red}Payroll System{re}                        *
    *                                                 *
    *                                                 *
    *	         Welcome {red}Employee{re}      	              *
    *					                        	  *
    *            here's what you can do :             *
    *  {red}*Write the function's number to use it*{re}        *
    *					                        	  *
    *    1 : whoami?                                  *
    *    2 : check in                                 *
    *	 3 : check out			                      *
    *	 4 : Withdraw your salary                  	  *
    *    5 : edit personal details                    *
    *               AND                               *
    *    0 : To exit to the main menu                 *
    *                                                 *
    ***************************************************""")

        option = input(red + "\nChoose a function : " + re)
        if option in choices:
            if option == "1":
                i = vars(choices[option][num])
                for j in i.keys():
                    print(j, i[j])

            elif option == "2":
                now = datetime.datetime.now().time()
                choices[option](employees[num],1, now)
                print(f"you checked in {len(employees[num].attendance)} times this month")
                print(f"you came late {len(employees[num].late)} times this month, you salary is {employees[num].salary}")

            elif option == "3":
                now = datetime.datetime.now().time()
                choices[option](employees[num], 1, now)
                print(f"you checked out {len(employees[num].out)} times this month")
                print(f"you wen out overtime {len(employees[num].overtime)} times this month, you salary is {employees[num].salary}")

            elif option == "4":
                amnt = int(input("Enter the amount you want withdraw: "))
                print(choices[option](employees[num],amnt))
                print(f"The left of your salary is: {employees[num].salaryleft}")

            elif option == "5":
                fname = input("Your new First Name: ")
                lname = input("Your new Last Name: ")
                email = input("Your new Email: ")
                phone = input("Your new phone: ")
                passwd = input("Your new Password: ")
                choices[option](employees[num], fname, lname, email, phone, passwd)

        elif option == "0":
            break

        else:
            print(f"{red}Wrong choice{re}")

def dprtmnt():
    choices = {
        "1": Department.AssignEmp,
        "2": Department.MakeDeductions,
        "3": Department.MakeAllowance
    }
    n = int(input("Enter your number: "))
    department = Department(employees[n].EmpId, employees[n].EmpDepartment, employees[n].FirstName)

    while True:

        print(f"""
        ***************************************************
        *           {red}Payroll System{re}                        *
        *                                                 *
        *                                                 *
        *	            Welcome {red}Department{re}         		  *
        *					                        	  *
        *            here's what you can do :             *
        *  {red}*Write the function's number to use it*{re}        *
        *					                        	  *
        *    1 : assign new employee                      *
        *    2 : Make Deductions                          *
        *	 3 : Make Allowance			                  *
        *	        	AND			                  	  *
        *    4 : To exit to main menu                     *
        *                                                 *
        ***************************************************""")
        option = input(red + "\nChoose a function : " + re)
        if option in choices:
            if option == "1":
                print("Please Enter the new employee's details separated by space in the same order:")
                new = input("First Name, Last Name, Email, Phone, Pass, ID, jt, dep, ban, salary:")
                new = new.split(" ")
                newemp = len(employees)+1
                employees[newemp] = choices[option](department,*[i for i in new])
                print(vars(employees[newemp]))
            elif option == "2":

                empnum = int(input("what is the number of the employee you want to deduce from? "))
                print(f"You chose the employee number {empnum}, and his name is:{employees[empnum].FirstName} his current salary is : {employees[empnum].salary }")
                deduce = int(input("Enter the amount to deduce: "))
                choices[option](employees[empnum], deduce)
                print(f"the new salary for {employees[empnum].FirstName} is {employees[empnum].salary}")

            elif option == "3":
                empnum = int(input("what is the number of the employee you want to give an allownce? "))
                print(
                    f"You chose the employee number {empnum}, and his name is:{employees[empnum].FirstName} his current salary is : {employees[empnum].salary}")
                rise = int(input("Enter the amount to add: "))
                choices[option](employees[empnum], rise)
                print(f"the new salary for {employees[empnum].FirstName} is {employees[empnum].salary}")

        elif option == "4":
            break
        else:
            print("Invalid Input!")
