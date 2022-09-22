import pandas as pd
import numpy as np
#function orders is created
df=pd.read_csv('order.csv')
data=dict([(i,a) for i, a in zip(df.Name,df.Price)])
def orders():
    print('Your Order Is Presented Please Check:')
    df=pd.read_csv('order.csv')
    data=dict([(i,a) for i, a in zip(df.Name,df.Price)])
    keys, values = zip(*data.items())
    order_no=np.random.randint(1000,9999,1)
    F=len(keys)
    df=pd.DataFrame({'order_no':[order_no]*F,'Name':keys,'Price':values})
    print(df)
    df=df.to_csv('bill.csv',index=False)