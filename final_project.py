import pandas as pd
import math as mt
from scipy.stats import norm


alpha = 0.05
z_score = norm.ppf(1-alpha/2)
df_cont=pd.read_csv('Final Project Results_Control.csv')
df_exp=pd.read_csv('Final Project Results_Experiment.csv')
df_base=pd.read_csv('Final Project Baseline Values.csv',header=None,index_col=0)

# Measuring Variability
samp = 5000
p0=df_base.loc['Click-through-probability on "Start free trial":',1]
p1=df_base.loc['Probability of enrolling, given click:',1]
p2=df_base.loc['Probability of payment, given click',1]
sigma_gross=mt.sqrt(p1*(1-p1)/(samp*p0))   
sigma_net=mt.sqrt(p2*(1-p2)/(samp*p0)) 
print(sigma_gross) 
print(sigma_net)  

# Sanity Checks 
def get_CIF_population(z_score,N_cont,N_Exp):
	SE = mt.sqrt(0.5*0.5/(N_cont+N_Exp))
	CIT_Low = round(0.5-z_score*SE,4)
	CIT_high = round(0.5+z_score*SE,4)
	observer_value=round(N_Exp/(N_cont+N_Exp),4)
	output ='The confidence interval is ' + '['+str(CIT_Low)+','+str(CIT_high)+']'\
	+ ', and the observered value is '+ str(observer_value)
	return (output)
	

def get_CIF_diff(z_score,X_cont,X_Exp,N_cont,N_Exp):
	pooled = (X_cont+X_Exp)/(N_cont+N_Exp)
	SE = mt.sqrt(pooled*(1-pooled)*(1/N_cont+1/N_Exp))
	CIT_Low = round(-z_score*SE,4)
	CIT_high = round(z_score*SE,4)
	observer_value =round(X_Exp/N_Exp-X_cont/N_cont,4)
	output ='The confidence interval is ' + '['+str(CIT_Low)+','+str(CIT_high)+']'\
	+ ', and the observered value is '+ str(observer_value)
	return (output)


num_clicks_cont = df_cont.loc[:,'Clicks'].sum()
num_clicks_exp=df_exp.loc[:,'Clicks'].sum()
print(get_CIF_population(z_score,num_clicks_cont,num_clicks_exp))
num_pages_cont=df_cont.loc[:,'Pageviews'].sum()
num_pages_exp=df_exp.loc[:,'Pageviews'].sum()
print(get_CIF_population(z_score,num_pages_cont,num_pages_exp))
print(get_CIF_diff(z_score,num_clicks_cont,num_clicks_exp,num_pages_cont,num_pages_exp))

# Effect Size Tests
def get_CIF_diff_Eva(z_score,X_cont,X_Exp,N_cont,N_Exp):
	pooled = (X_cont+X_Exp)/(N_cont+N_Exp)
	SE = mt.sqrt(pooled*(1-pooled)*(1/N_cont+1/N_Exp))
	observer_value =round(X_Exp/N_Exp-X_cont/N_cont,4)
	CIT_Low = round(observer_value-z_score*SE,4)
	CIT_high = round(observer_value+z_score*SE,4)
	output ='The confidence interval is ' + '['+str(CIT_Low)+','+str(CIT_high)+'].'
	return (output)

num_Enroll_cont = df_cont.loc[:,'Enrollments'].sum()
num_Enroll_exp = df_exp.loc[:,'Enrollments'].sum()
date_enroll=df_cont.loc[pd.notnull(df_cont.loc[:,'Enrollments'])].index.values
num_clicks_exp=df_exp.loc[date_enroll,'Clicks'].sum()
num_clicks_cont = df_cont.loc[date_enroll,'Clicks'].sum()
print(get_CIF_diff_Eva(z_score,num_Enroll_cont,num_Enroll_exp,num_clicks_cont,num_clicks_exp))
num_Pay_cont = df_cont.loc[:,'Payments'].sum()
num_Pay_exp = df_exp.loc[:,'Payments'].sum()
date_Pay=df_cont.loc[pd.notnull(df_cont.loc[:,'Payments'])].index.values
num_clicks_exp=df_exp.loc[date_Pay,'Clicks'].sum()
num_clicks_cont = df_cont.loc[date_Pay,'Clicks'].sum()
print(get_CIF_diff_Eva(z_score,num_Pay_cont,num_Pay_exp,num_clicks_cont,num_clicks_exp))

