import datetime
now = datetime.datetime.now().time()
class Person:
    def __init__(self, FN, LN, Email, Phone, Pass):
        self.FirstName = FN
        self.LastName = LN
        self.Email = Email
        self.PhoneNum = Phone
        self._Password = Pass

    def EditPersonalDetails(self, FN, LN, Email, Phone, Pass):
        self.FirstName = FN
        self.LastName = LN
        self.Email = Email
        self.PhoneNum = Phone
        self._Password = Pass


class Employee(Person):
    def __init__(self, FN, LN, Email, Phone, Pass, ID, jt, dep, ban, salary=0):
        super().__init__(FN, LN, Email, Phone, Pass)
        self.EmpId = ID
        self.EmpDepartment = dep
        self.EmpJobTitle = jt
        self.BankAccNum = ban
        self.salary = float(salary)

        # salary variables for methods
        self.late = []
        self.attendance = []
        self.overtime = []
        self.out = []
        self.salaryleft = float(salary)

    def CheckIn(self, checkin=1, time = now):
        self.attendance.append(checkin)
        if time.hour > 8 and time.minute > 30:
            self.late.append(1)
            self.salary -= 10


        return self.attendance, self.late

    def ChekOut(self, checkout=1, time=now):
        self.out.append(checkout)
        if time.hour > 5 and time.minute > 00:
            self.overtime.append(1)
            self.salary += 10


    def Withdraw(self, amnt):
        if amnt > self.salary or amnt < 10:
            return "Invalid Value! "
        else:
            self.salaryleft = self.salary - amnt
            self.salary = self.salaryleft
            return "Sucess!"

class Manager(Person):

    def __init__(self, FN, LN, Email, Phone, Pass, ID, role):
        super().__init__(FN, LN, Email, Phone, Pass)
        self.ManID = ID
        self.Role = role
    def veiwemp(self,dic={}):
        names = []
        for i in dic.keys():
                names.append(dic[i].FirstName)
        return names

    def GiveRise(self, amount):
        self.salary += amount
        return self.salary

    def AddSalary(self, amount):
        self.salary = amount

    def DeleteSalary(self):
        self.salary = 0

    def EditSalary(self, new_value):
        self.salary = new_value


class Department:
    def __init__(self, ids, name, hod):
        self.DepID = ids
        self.DepName = name
        self.HeadOfDepartment = hod

    def AssignEmp(self, FN, LN, Email, Phone, Pass, ID, jt, dep, ban, salary):
        self.new_emp = Employee(FN, LN, Email, Phone, Pass, ID, jt, dep, ban, salary)
        return self.new_emp

    def MakeDeductions(self, amount):
        self.salary -= amount

    def MakeAllowance(self, amount):
        self.salary += amount


class Deductions:
    def __init__(self, amount1):
        self.DedAmount = amount1

    def __add__(self, ob):
        return self.DedAmount + ob.ALAmount


class Allowance:
    def __init__(self, amount2):
        self.ALAmount = amount2

    def __add__(self, ob):
        return self.ALAmount + ob.DedAmount


class TotalPay(Deductions, Allowance):
    def __init__(self, deduce, allow):
        super().__init__(allow)
        super().__init__(deduce)
        self.ALAmount = allow
        self.DedAmount = deduce

        self.Amount = self.Sum_Allow_Deduct(self.ALAmount, self.DedAmount)

    def __add__(self, obj):
        return self.Amount + obj.Amount

    def Sum_Allow_Deduct(self, allow, deduct):
        self.Amount = allow + deduct
        return self.Amount

