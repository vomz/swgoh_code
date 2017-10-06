import pandas as pd
import numpy as np
from scipy.stats import f


def mlr(data,dependent_variable=None):
    dataframed=df_check(data,dependent_variable)    
    y=dataframed[0]
    ind_vars=dataframed[1]
    
    
    
    
def df_check(data,dependent_variable):
#==============================================================================
# data : must be a DataFrame or Dictionary
# dependent_variable : is the column/key name of the vector containing the data
#                      otherwise it defaults the column in position 0
#==============================================================================
    dict={}
    df=pd.DataFrame()
    ds=pd.Series()
    if type(data) == type(dict) or type(data) == type(df) or type(data) == type(ds):
        pass
    else:
        raise TypeError("This calculation requires the data to be in a dict, pandas DataFrame or pandas Series")
    data=pd.DataFrame(data)
    if type(dependent_variable)==str:
        y=pd.DataFrame(data[dependent_variable],index=np.arange(1,len(data)+1))
        ind_var_names=data.keys().drop(dependent_variable)
        ind_vars=data[ind_var_names]
    else:
        raise ValueError("dependent_variable must the name of the dependent variable in string format.")
    
    
    return y,ind_vars


def beta_calc(y,ind_vars):
#==============================================================================
# beta_hat = (X'X)**-1 * X'Y
#==============================================================================        
    coefficients=y
    #creating first column of all 1s    
    fc=1
    fc=[fc]*len(y)
    
    X=pd.DataFrame(fc,columns=['b0'])
    
    X=pd.concat([X,ind_vars],axis=1,join='inner')
    
    X_trans = X.transpose()
    
    Y = coefficients
    
    X_trans_X = X_trans.dot(X)
    
    X_trans_Y = X_trans.dot(Y)
    
    X_trans_X_inverse = pd.DataFrame(np.linalg.pinv(X_trans_X.values),X_trans_X.columns,X_trans_X.index)
    
    betas = X_trans_X_inverse.dot(X_trans_Y)

    return betas
        

def qtrans(ts,q):
    #moving average
    name='q'+str(q)
    ts=pd.DataFrame(ts)
    qdata=ts.rolling(window=q,min_periods=q).mean().dropna()
    qdata=qdata.rename(columns={qdata.columns[0]:name})
    qdata=qdata[:len(qdata)-1]
    #combined=pd.concat([ts,qdata],axis=1,join='inner')
    ts=ts[q:]
    x=[]
    y=[]
    for i in ts.values:
        y.append(i)
    for i in qdata.values:
        x.append(i)
    ts=y
    qdata=x    
    
    return pd.DataFrame(ts),pd.DataFrame(qdata)


def ptrans(ts,p):
    name='q'+str(p)
    #lags
    ts=pd.DataFrame(ts)
    pdata=ts.shift(p).dropna()
    pdata=pdata.rename(columns={pdata.columns[0]:name})    
    ts=ts[p:]
    x=[]
    y=[]
    for i in ts.values:
        y.append(i)
    for i in pdata.values:
        x.append(i)
    ts=y
    pdata=x    
    
    return pd.DataFrame(ts),pd.DataFrame(pdata)    
    
    
    
    return pdata














def sum_product(y,*args):
    
    sum_product = y*args
    
    return sum_product.sum()

def sum_sq(x):
    
    sum_sq=x**2
    
    return sum_sq.sum()

def simple_linear_model(x,y):
    
    m=slope(x,y)
    
    b=intercept(x,y) 
    
    return m,b
    
def yhats(x,y):
    
    formula=simple_linear_model(x,y)
    
    m=formula[0]
    b=formula[1]
    
    mx=x*m
    yhat=mx+b
    return yhat

def calc_ssr(x,y):
    yhat=yhats(x,y)
    ybar=np.array(y).mean()
    
    diff=(yhat-ybar)
    ssr=(diff**2).sum()
    return ssr

    
def calc_sst(y):
    y=np.array(y)
    ybar=y.mean()
    
    diff=(y-ybar)
    sst=(diff**2).sum()
    
    return sst
    
def rsquare(x,y):
    ssr=calc_ssr(x,y)
    sst=calc_sst(y)
    
    r2=ssr/sst
    
    return r2

def rsquare_adj(x,y):
    r2=rsquare(x,y)
    N=len(x)
    p=1
    
    r2a=1-((1-r2)*(N-1))/(N-p-1)
    
    return r2a

def fstat(x,y):
    ssr=calc_ssr(x,y)
    sst=calc_sst(y)
    sse=sst-ssr
    tdf=len(x)-1
    mdf=1
    edf=tdf-mdf
    
    unex_var=sse/edf
    
    fstatistic=ssr/unex_var
    
    p=1-f.cdf(fstatistic,1,edf)
    
    return fstatistic,p
    
def regression(x,y):
    x=np.array(x)
    y=np.array(y)
    model=simple_linear_model(x,y)
    m=model[0]
    b=model[1]
    ssr=calc_ssr(x,y)
    sst=calc_sst(y)
    sse=sst-ssr
    obs=len(x)
    tdf=len(x)-1
    mdf=1
    edf=tdf-mdf
    r2=rsquare(x,y)
    r2a=rsquare_adj(x,y)
    unex_var=sse/edf
    F=fstat(x,y)[0]
    pf=fstat(x,y)[1]
    
    print("R**2: %4.4f" % r2)
    print("Adjusted R**2: %4.3f" % r2a)
    print("Number of Observations: %d" % obs)
    print("SSR: %4.3f" % ssr)
    print("SSE: %4.3f" % sse)
    print("SST: %4.3f" % sst)
    print("Unexplained Variance: %4.3f" % unex_var)
    print("F: %4.3f" % F)
    print("F p-value: %4.8f" % pf)
    print("Intercept: %4.3f" % b)
    print("Slope: %4.3f" % m)
                                                
    
    
#    x,y plot
#    ymean plot
#    yhat plot
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    