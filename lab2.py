import re
import mysql.connector
#database
def addToDataBase(emp):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
       password="1234",
       database="pythonEmployee"
    )
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY,fullname VARCHAR(255), email VARCHAR(255),salary INT(11),ownedmoney INT(11),is_manager BIT, workmood VARCHAR(255),sleepmood VARCHAR(255),healthRate VARCHAR(255))")
    sql = "INSERT INTO employees (fullname, email,salary,ownedmoney,is_manager,workmood,sleepmood,healthRate) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
    val = (emp.name,emp.email,emp.salary,emp.money,emp.is_manager,emp.workmood,emp.sleepmood,emp.healthRate)
    mycursor.execute(sql, val)
    mydb.commit()

def RetriveAllEmployees():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="pythonEmployee"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employees")
    myResult = mycursor.fetchall()
    for x in myResult:
        print(x)

def retriveOneEmployee(empId):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="pythonEmployee"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM employees WHERE id = " + empId +";"
    mycursor.execute(sql)
    myResult = mycursor.fetchall()
    for x in myResult:
        if x[5] == 0:
            print(x)
        else:
            print("id: ",x[0]," ,name: ",x[1]," ,email: ",x[2]," , is_manager: ",x[5]," ,sleep mode: ",x[6]," ,work mode: ",x[7]," ,health rate: ",x[8])

def fireEmployee(empId):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="pythonEmployee"
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM employees WHERE id = " + empId + ";"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Employee has been fired")


#validation 
#validation on salary
def validInSalary():
    salary = int(input("salary: "))
    while (salary < 1000 ):
        print("The salary must be equal or more than 1000, try again.")
        salary = int(input("salary: "))
    return salary

#check mail 
# for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
def checkMail():
    message = "Invalid Email" 
    while(message != "Valid Email"):
        email =input("email: ")
        if(re.search(regex, email)):
            message= "Valid Email"
            return email
        else:
            message = "Invalid Email"
            print("Invalid Email")

#validation on HealthRate
def validInHealthRate():
    message = "Invalid HealthRate" 
    healthRate = int(input("Health Rate: "))
    while(message != "valid HealthRate"):
        if healthRate < 0 or healthRate > 100:
            print("The healthRate is out of range, try again.")
            healthRate = int(input("Health Rate: "))
            message = "Invalid HealthRate" 
        else:
             message = "valid HealthRate"
    return healthRate

def IsManagerOrNot(status):
    is_manager = False
    if status == 1:
        is_manager = True
    elif status == 2:
        is_manager = False
    return  is_manager

#main Menu 
def menu():   
    print("[1] Add")
    print("[2] Display All Employee")
    print("[3] Display one Employee")
    print("[4] Fire Employee")
    print("[0] Exit the program.")  

def checkwantToHireOrNot(emp):
    status = input("Do you want to hire this employee [yes, No]")
    if status == "yes":
        office = Office("NewOffice")
        office.hire(emp)
    else:
        print("you don't hire this employee")

#submenu for data
def addNewData(postion):
    name = input("name: ")
    salary = int(validInSalary())
    healthRate = int(validInHealthRate())
    is_manager = IsManagerOrNot(postion)
    email = checkMail()
    sleepHours = int(input("sleepHours: "))
    items = int(input("items: "))
    workHours =  int(input("workHours: "))  
    meals =  int(input("No of meals: "))  
    emp=Employee(email,workHours,salary,is_manager,name,healthRate,sleepHours,items)
    emp.eat(meals)
    wantToHireEmployeeOrNot = checkwantToHireOrNot(emp)
    
    

def menuManager():
    addNewData(1)

def menuEmployee():
    addNewData(2)

#sub menu to choose Employee or Manager
def addData(option):
    if option == 1:
        menuManager()
    elif option == 2:
        menuEmployee()
    else:
        print("Invalid option.")

#print sub menu for Manager or Employee 
def menuForAdd():
    print("[1] Add manager") 
    print("[2] Add normal Employee")
    option = int(input("Please enter your option: "))
    addData(option)


def option1Add():
    menuForAdd()

#################### Class Person ##########################
class Person:
    #"This is a person class"
    def __init__(self, name, healthRate,sleepHours,money):
        self.name = name
        self.healthRate = healthRate
        self.money = money
        self.sleepHours = sleepHours

    def sleep(self,sleepHours):
        if hours == 7:
            self.sleepMood = "happy"
        elif hours > 7:
            self.sleepMood = "Lazy"
        elif hours < 7:
            self.sleepMood = "tired"
        print({sleepMood})
    
    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100 * self.healthRate
        elif meals == 2:
            self.healthRate = 75 * self.healthRate
        elif meals == 1:
            self.healthRate = 50 * self.healthRate
        print("Health Rate = {self.healthRate}")

    def buy(self, items):
        self.money = self.money - (10 * items)
        print("Money = {self.money}")

  
#############################################################################

############################## Class Employee ###############################
class Employee(Person):
    def __init__(self,email, workmood, salary,is_manager, name, healthRate, sleepmood,items):
        #self.id = id
        self.email = email
        self.workmood = workmood
        self.salary = salary
        self.is_manager = is_manager
        self.sleepmood = sleepmood
        self.items = items
        Person.__init__(self, name, healthRate,sleepmood,salary)

        def sendEmail(self,to,subject ,bodyreceiver_name):
            with open('target.txt','w') as out:
                line1 = "to:" + to 
                line2 = "subject: "+subject
                line3 = "bodyreceiver_name: " + bodyreceiver_name
                print("I'm going to write these to the file.")
                out.write('{}\n{}\n{}\n'.format(line1,line2,line3))
############################## Class Office ###############################
class Office:
    def __init__(self,name):
        self.name = name
    def get_all_employees(self):
        RetriveAllEmployees()
    def get_employee(self,empId):
        retriveOneEmployee(empId)
    def fire(self,empId):
        fireEmployee(empId)
    def hire(self,emp):
        addToDataBase(emp)
#############################################################################

def FireEmployee():
    office = Office("office1")
    empId = input("Enter Id of Employee= ")
    office.fire(empId)

def DisplayAllEmployee():
    office = Office("office1")
    office.get_all_employees()

def DisplayOneEmployee():
    office = Office("office1")
    empId = input("Enter Id of Employee= ")
    office.get_employee(empId)


# drive code 
menu()
option = input("Please enter your option: ")
while option != 'q':
    if option == "add":
        option1Add()
    elif option == "fire":
        FireEmployee()
    elif option == "display":
        DisplayAllEmployee()
    elif option == "employee":
        DisplayOneEmployee()
    else:
        print("Invalid option.")
    print()
    print("============================")    
    menu()
    option = input("Please enter your option: ")

print("Thank You for use this program.")







