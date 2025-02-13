import os 
import pandas as pd
import json
import math
from sksurv.metrics import concordance_index_censored
from collections import ChainMap

def c_index(data,betas,time_col,censor_col):
    #data = pd.read_csv("filter_data.csv", index_col=0)
    print("ci", data.head())
    print(data.shape)
    #print(censor_col)
    data[str(censor_col)] = data[str(censor_col)].astype('bool')
    #print(data[censor_col])
    data["lp"] = ""
    lp_list=[]

    mean_dict = {}
    val_dict = {}
    lp_val = {}
    betas=dict(ChainMap(*betas))    
    #print(betas)
    #calculate linear predictor
    lp = 0
    for i, j in data.iterrows():
        for key in betas:
            val_dict[key] = j[key]
            lp_val[key] = (val_dict[key]*betas[key])
        lp = sum(lp_val.values())
        exp_lp = math.exp(lp)
        lp_list.append(exp_lp)
    
    data['lp']=lp_list

    #calculate concordance index
    result = concordance_index_censored(data[censor_col], data[time_col], data["lp"])

    cindex = result[0]
            
    return cindex