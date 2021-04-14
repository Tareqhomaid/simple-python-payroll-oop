from payrollfunctions import *

red = '\033[31;1m' #coloring
re = '\033[m' #reset coloring
try:
    if __name__ == "__main__":
        scenario = {
        "1": mngr,
        "2": emp,
        "3": dprtmnt,
        }

        while True:
            print (f"""
        ***************************************************
        *    This is a simple payroll system using oop    *
        *    you can use it as a manager or employee      *
        *          thus you can use the methods           *
        *	    assigned to every one	  	              *
        *				             	                  *
        *  here you can choose who you want to be :       *
        * {red}*Write the scenario's number to use it*{re}	      *
        *		                        	              *
        *    1 : manager                                  *
        *    2 : employee                                 *
        *    3 : department		                          *
        *	        	AND	          	                  *
        *    4 : To exit the program                      *
        *                                                 *
        ***************************************************""")

            option = input(red + "\nChoose a scenario : " + re)
            if option in scenario:
                scenario[option]()

            elif option == "4":
                break
            else:

                print (f"{red}Wrong choice{re}")
except:
    raise Exception("somthing wrong happened!")


