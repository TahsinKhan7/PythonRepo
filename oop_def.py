
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Tahsin', '', '')
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_2.fullname())


##############
# emp_1.first = 'Tahsin'
# emp_1.last = 'Khan'
# emp_1.email = 'tahsin_k@live.co.uk'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test_k@live.co.uk'
# emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)
###########################
