import pandas as pd
#function add is created

data={}
#to display all available drinks in that type
    
def A():#if this the selected type
    print('A.Espresso \n1.Latte :@95 \n2.Mocha :@100 \n3.Caramel Macchiato :@195 \
\n4.White Chocolate Mocha :@170 \n5.Americano :@115 \n6.BACK')
    print("------------------")
    A=int(input('Choose menu> '))
    #to select users orders
    if A==1:
        print('Ordered Latte :@95 ')
        a=int(input('QTY> '))#for qty of drink to buy
        A1='Latte'
        data[A1]=a*95#to add in dictionary
        print(data)
            
    if A==2:
        print('Ordered Mocha :@100 ')
        a=int(input('QTY> '))
        A2='Mocha'
        data[A2]=a*100
        print(data)
            
    if A==3:
        print('Ordered Caramel Macchiato :@195 ')
        a=int(input('QTY> '))
        A3='Caramel Macchiato'
        data[A3]=a*195
        print(data)
            
    if A==4:
        print('Ordered White Chocolate Mocha :@170 ')
        a=int(input('QTY> '))
        A4='White Chocolate Mocha'
        data[A4]=a*170
        print(data)
            
    if A==5:
        print('Ordered Americano :@115 ')
        a=int(input('QTY> '))
        A5='Americano'
        data[A5]=a*115
        print(data)
            
    if A==6:
        print('going BACK to menu')
        print(data)
        #if selected number is not displyed following will work
    else:
        print('PLEASE ENTER VALID NUMBER')
        print('  ')
    #if this the selected type
def B():
    print('B.Fresh Brewed Coffee \n1.Coffee Of The Day :@170 \n2.Cold Coffee :@65 \n3.BACK')
    print("------------------")
    B=int(input('Choose menu> '))
            
    if B==1:
        print('Ordered Coffee Of The Day :@170 ')
        a=int(input('QTY> '))
        B1='Coffee Of The Day'
        data[B1]=a*170
        print(data)
            
    if B==2:
        print('Ordered cold coffee :@65 ')
        a=int(input('QTY> '))
        B2='Cold Coffee'
        data[B2]=a*65
        print(data)
            
    if B==3:
        print('going BACK to menu')
        print(data)
    #if selected number is not displyed following will work
    else:
        print('PLEASE ENTER VALID NUMBER')
        print('  ')
#if this the selected type
def C():
    print('C.Tea \n1.Hot Tea :@40 \n2.Iced Tea :@50 \n3.Iced Tea Lemonade :@70 \
\n4.Green Tea :@50 \n5.Black Tea :@40 \n6.BACK')
    print("------------------")
    C=int(input('Choose menu> '))
        
    if C==1:
        print('Ordered Hot Tea :@40 ')
        a=int(input('QTY> '))
        C1='Hot Tea'
        data[C1]=a*40
        print(data)
            
    if C==2:
        print('Ordered Iced Tea :@50 ')
        a=int(input('QTY> '))
        C2='Iced Tea'
        data[C2]=a*50
        print(data)
            
    if C==3:
        print('Ordered Iced Tea Lemonade :@70 ')
        a=int(input('QTY> '))
        C3='Iced Tea Lemonade'
        data[C3]=a*70
        print(data)
            
    if C==4:
        print('Ordered Green Tea :@50 ')
        a=int(input('QTY> '))
        C4='Green Tea'
        data[C4]=a*50
        print(data)
            
    if C==5:
        print('Ordered Black Tea :@40 ')
        a=int(input('QTY> '))
        C5='Black Tea'
        data[C5]=a*40
        print(data)
            
    if C==6:
        print('going BACK to menu')
        print(data)
        #if selected number is not displyed following will work
    else:
        print('PLEASE ENTER VALID NUMBER')
        print('  ')


def D():
    keys, values = zip(*data.items())#to seperate from dictionary
    df=pd.DataFrame({'Name':keys,'Price':values})
    a=(len(keys))
    total=sum(values)
    df=pd.DataFrame({'Name':keys,'Price':values})
    df.at[a]='TOTAL',total
    df=df.to_csv('order.csv',index=False)
