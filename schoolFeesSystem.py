import statistics

adminsLog = {'admin':'admin1','admin1':'admin1'}

feesList = {'School Fees':92,'PTA':23,'Exam Fees':45}

studList=['Sherif','Halik','Hanan','Akram']

schFees = {}
pta = {}
exam = {}

def newStudent():
    nameToAdd = input('Name: ')
    if nameToAdd in studList:
        print('Student already exit')
    else:
        studList.append(nameToAdd)

def createFees():
    feesName = input('Fees name: ')
    feeAmount = input('Fees Amount: ')
    if feesName in feesList:
        print('Fee already exist in the system')
    else:
        feesList[feesName]=feeAmount
def editFees():
    feeToEdit = input('Enter fee name to edit: ')
    newAmount = input('New fee amount: ')

    if feeToEdit in feesList:
        feesList[feeToEdit]=newAmount
    else:
        print('Fees not found, Please Contact administrator')

def takeFees():
    feeType = input('Enter fee type: ')
    if feeType in feesList:
        studName = input('Enter Student name: ')
        if studName in studList:
            amount=input('Enter amount: ')
            if feeType == 'School Fees':
                originalAmount = feesList[feeType]
                if float(amount)>originalAmount:
                    print('You cannot more than the original amount')
                else:
                    schFees[studName]=amount
            elif feeType == 'PTA':
                originalAmount = feesList[feeType]
                if float(amount)>originalAmount:
                    print('You cannot more than the original amount')
                else:
                    pta[studName]=amount
            elif feeType == 'Exam Fees':
                originalAmount = feesList[feeType]
                if float(amount)>originalAmount:
                    print('You cannot more than the original amount')
                else:
                    exam[studName]=amount
            else:
                print('nothing is changed')
        else:
            print('Student Not Found')
    else:
        print('Fee type does not exist')
def main():
    print('''
    Welcome to Fees Management System

    [1] - Enter New Student
    [2] - Create New Fees
    [3] - Edit Fees
    [4] - Take Fees payment
    [5] - Logout
    
    ''')

    option = input('What would you like to do today? (Enter a number) ')
    if option == '1':
        newStudent()
        print(studList)
    elif option =='2':
        createFees()
        print(feesList)
    elif option =='3':
        editFees()
        print(feesList)
    elif option =='4':
        takeFees()
        print(schFees)
        print(pta)
        print(exam)
    else:
        exit()


login = input('Username: ')
password = input('Password: ')

if login in adminsLog:
    if adminsLog[login] ==  password:
        print('Welcome, ',login)
        main()
    else:
        print('Invalid Password, Please try again')
else:
    print('Invalid Username, Please try again')
