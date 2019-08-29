import datetime
class Employee:

    def __init__(self, name, title):
        self.name = name
        self.job_title = title
        self.employment_start_date = None

    def hired(self):
        self.employment_start_date = datetime.datetime.now()


class Company:

    def __init__(self, business_name, address,industry):
        self.business_name = business_name
        self.address = address
        self.industry = industry
        self.employees = list()

    def hire(self, employee):
         self.employees.append(employee)
    def company_print(self):
        print(f'{self.business_name} is in the {self.industry} and has the following employees')
        self.emp()

    def emp(self):
        for employees in self.employees:
            print(f'*   {employees.name}')

AlexLLC = Company("Alex LLC", "Heaven", "WOW")
TylerInc = Company("Tyler Inc", "123 CoolGuy Ave", "Coke Drinking")

Matthew = Employee("Matthew", "computer Dude")
Tyler = Employee("Tyler", "Home DESTROYER")
Drew = Employee("Drew", "Cameraman")
Danny = Employee("Danny", "Janitor")
Alex = Employee("Alex", "CEO")

TylerInc.hire(Matthew)
TylerInc.hire(Drew)
AlexLLC.hire(Tyler)
AlexLLC.hire(Danny)
AlexLLC.hire(Alex)
TylerInc.company_print()
AlexLLC.company_print()