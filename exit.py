import pandas as pd,numpy as np
#function is created 

def exit():
    print('-----Thank You For Ordering In Flawless Coffee-----')
    print('-----Visit Our cafe soon-----')
    print('Your Order Is Presented Please Check:')
    df=pd.read_csv('bill.csv')
    total=df.iat[-1,-1]
    #to create a dataframe ordered of ordered items and their price
    print('get upto 50% off')
    o=input('press 1. to apply offer>>')
    #to give offer on drink ordered
    if o=='1':
        #random value is generated between 0-50 using numpy
        off=int(np.random.randint(0,50,1))
        print('Got',off,'% off')
        #if something else is entered other than asked offer given would be zero
    else:
        off=0
    a=len(df.Name)
    c=df.iat[0,0]
    df.loc[a]=c,'offer%',off#to add new row offer
    t=total-(total*off/100)
    a=len(df.index)
    df.loc[a]=c,'New Total',t
    print(df)
    df=df.to_csv('daily_analysis.csv',index=False)
    
    r=int(input('PLEASE RATE OUR CAFE \n '))#to take users rating in cafe
    a=input('Please Write A Feedback Of Our Cafe #')#to ask user's feed back
    print('Thank you For Rating us')
    print('We Will Try To Upgrade Our Cafe Accourding To Your Feedback')