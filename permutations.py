import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta

returns = pd.read_csv('returns.csv')
returns.index = returns.Date.astype('datetime64[ns]')
returns.drop('Date', axis=1, inplace=True)

def permutation(df):
    permi=df.copy()
    df2=df.drop(['Representative','Party','House'],axis=1)
    columns=['ReportDate','TransactionDate','Ticker','Transaction','Amount','Range','Sentiment','Price','Low_End','High_End','Adjusted_Low_End','Adjusted_High_End','Running_Portfolio_Low_End','Running_Portfolio_High_End','Est_Portfolio_Value','Shares_High_End','Shares_Low_End','Variance']
    permi[columns]=pd.DataFrame(np.random.permutation(df2))
    return permi

def npermis(df, i):
    qr=[]
    for n in range(i):
        qr.append(permutation(df))
    return qr

def calculate_variance(row):
    ticker = row['Ticker']
    transaction_date = row['TransactionDate']
    
    # Find the index in returns corresponding to the TransactionDate
    index = transaction_date
    
    # Calculate variance for the next 3 months (90 days)
    end_index = transaction_date + relativedelta(months=3)
    variance = np.var(returns[ticker][index:end_index])
    
    return variance