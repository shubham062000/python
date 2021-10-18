#This program for saving employee objects into the file(emp.data) in binary format
import pickle
class employee:
    def __init__(self,eno,ename,eprofile,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
        self.eprofile=eprofile
    def display(self):
        print('Employee Number: {}, Employee Name {},  Employee Profile {}, Employee salary {}, Employee Address {}'.format(eno,ename,eprofile,esal,eaddr))


file=open('emp.text','wb') # wb means write binary you can take ab because wb will override your data every time, Open file for writing, If file is not existing then it will create file,
while True:             # Infinite loop when user press no then only this loop will stop
    eno=int(input('Enter employee number:'))
    ename=input('Enter employee name:')
    eprofile=input('Enter Employee Profile:')
    esal=float(input('Enter employee salary:'))
    eaddr=input('Enter employee address:')
    e=employee(eno,ename,eprofile,esal,eaddr)
    pickle.dump(e,file)         # pickling employee objects in file
    option=input('Do you want to continue [Yes|No] OR Do you want to see employee objects press [see]:')
    if option.lower()=='no':
        break
    elif option.lower()=='see':
        e.display()
print('Multiple Employee objects serilized')