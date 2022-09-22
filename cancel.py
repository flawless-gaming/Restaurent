import pandas as pd
#function remove is created

def remove():
    df=pd.read_csv('order.csv')
    df=df.iloc[:-1,:]
    data=dict([(i,a) for i, a in zip(df.Name,df.Price)])
    keys, values = zip(*data.items())
    total=sum(values)
    df=pd.DataFrame({'Name':keys,'price':values})
    a=(len(keys))
    df.at[a]='TOTAL',total
    print(df)
    p=input("Enter the Product to Remove=")
    #if product is in dictionary
    if p in data:
        data.pop(p)#to remove product
        print('Order of',p,'Canceled')
        if len(data)==0:
            x={'Name':['TOTAL'],
               'Price':[0]
               }
            df=pd.DataFrame(x)
        else:
            keys, values = zip(*data.items())
            total=sum(values)
            df=pd.DataFrame({'Name':keys,'price':values})
            a=(len(keys))
            df.at[a]='TOTAL',total
        print(df)
        df=df.to_csv('order.csv',index=False)
    else:
        print("No Product",p,"Available Add first")
