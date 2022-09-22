import add
import orders
import exit
import cancel
#AIM:to order,cancel order,display order and giving order 
print("=== WELCOME TO FLAWLESS COFFEES ===")
def options():
    print("1. Buy Meal")
    print("2. Show Ordered Meals")
    print("3. Cancel Meal")
    print("0. If Finished Ordering")
    print("------------------")
options()
menu =int(input("Choose menu> "))#users request
#while loop to repeat the loop
while True:
    #to add drink
    if menu==1:#to display types of drink
        print('A.Espresso \nB.Fresh Brewed Coffee \nC.Tea \nD.MENU')
        print("------------------")
        x=input('Choose menu> ')
        #to display all available drinks in that type
        if x=='A':
            add.A()
            
        if x=='B':
            add.B()
        
        if x=='C':
            add.C()
            
        if x=='D':
            print('Menu')
            options()
            menu =int(input("Choose menu> "))#users request
            add.D()
            
    elif menu==2:
        orders.orders()
        print('Menu')
        options()
        menu =int(input("Choose menu> "))#users request
        
    elif menu==3:
        cancel.remove()
        print('Menu')
        options()
        menu =int(input("Choose menu> "))#users request
   
   
    elif menu==0:
        exit.exit()
        break
        
    else:
        print('Please Enter From Asked Number')
        options()
        
        