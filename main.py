contact ={}
#add a contact
def add_contact():
    name=input("enter your name:")
    number=int(input("enter your number:"))
    if name in contact :
        print('name already exists')
    else:
        contact[name]=number
        print ('contact added')
    
def remove_contact():
    name=input("enter the name to be removed:")
    if name not in contact :
        print("name does not exist")
    else:
        del contact[name]
        print ('contact removed')

def update_contact():
    name=input("enter the name to be updated:")
    number=int(input("enter the number to be updated:"))
    if name not in contact :
        print("name does not exist")
    else:
        contact[name]=number
        print ('contact updated')
    
def display_contact():
    print("contact:",contact)
   
print('------------welcome to phonebook--------------')
print('1.add contact')
print('2.remove contact')
print('3.update contact')
print('4.display contact')
print('5.exit')
while True:
    choice=int(input('Enter your choice'))
    if choice==1:
        add_contact()
    elif choice==2:
        remove_contact()
    elif choice==3:
        update_contact()
    elif choice==4:
        display_contact()
    elif choice==5:
        print('thank you for using the app!!')
        break
    else:
        print ('invalid option')
