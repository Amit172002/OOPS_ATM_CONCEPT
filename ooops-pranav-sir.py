class SBI:
    ROI = 0.07

    def __init__(self,Name,Contact,Aadhar,Pan,Gender,Bal,Pin):
        self.Name    = Name
        self.Contact = Contact
        self.Aadhar  = Aadhar
        self.Pan     = Pan
        self.Gender  = Gender
        self.Bal     = Bal
        self.Pin     = Pin

    def details(self):
        print(f'Name    : {self.Name}')
        print(f'Contact : {self.Contact}')
        print(f'Aadhar  : {self.Aadhar}')
        print(f'Pan     : {self.Pan}')
        print(f'Gender  : {self.Gender}')
        print(f'Bal     : {self.Bal}')

    def Withdraw(self):
        if self.CheckPin() == self.Pin:
            amount = int(input("Enter The Amount to withdraw : "))
            if self.Bal >= amount:
                self.Bal -=amount
                print("Withdraw Successfully.....")
                print(f'Available Balance : {self.Bal}')
            else:
                print("Insufficient Balance...")

        else:
            print("Invalid Pin")

    @staticmethod
    def CheckPin():
        return int(input("Enter Your 4-digit Pin"))
    def Deposite(self):
        amount = int(input("Enter The Amount to Deposite : "))
        self.Bal += amount
        print("Credited Successfully.....")
        print(f'Available Balance : {self.Bal}')

    def CheckBalance(self):
        if self.CheckPin() == self.Pin:
            print(f"YOur Available Balance : {self.Bal}")
        else:
            print("Invalid Pin")
        

    @classmethod
    def ChangeROI(cls):
        var = float(input("Enter the new ROI"))
        cls.ROI = var

    def changePin(self):
        oldpin = int(input("Enter Your Old Pin "))
        if self.Pin == oldpin:
            newpin = int(input("Enter Your New 4-digit Pin "))
            self.Pin = newpin
    
        

            
cust1 = SBI('Amit',7725046503 , 927985089458 , 'FXMPM2772P' , 'Male' , 10000,1234)
cust2 = SBI('Dhruva' , 7894561231, 985647899587 , 'ABCD2587Q' , 'Male',8000,5678)
print(cust1.Name)
cust1.details()
print()
print(cust2.Name)
cust2.details()
print()
cust2.Pan= 'DFGH2857P'
cust2.changePin()
cust2.CheckBalance()
cust2.Withdraw()
cust1.Deposite()

