import pandas as pd
import numpy as np 

def atomcat_preprocess_dm1(df):
   
    #df = df[df['m_stage'].astype(int)] 
    #Only keep patients with no baseline metastases (M stage = 0)
    #df['m_stage'] = df['m_stage'].apply(pd.to_numeric, errors='coerce', downcast='integer')
    df = df[df['m_stage'] == 0]
    
    #Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=['rt_technique'])
    for i in range(len(df)):
        if df.iloc[i]['rt_technique'] <= 1:
            df.at[df.index[i],'rt_technique'] = 0
        else:
            df.at[df.index[i],'rt_technique'] = 1
   
    #Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = np.where((df['age'] >= 50) & (df['age'] <= 69), 1, 0)
    df['age70plus'] = np.where(df['age'] >= 70, 1, 0)
   
    #Age: converting to age squared
    df['agesquared'] = df['age']**2
   
    #Chemotherapy regimen: create dummy variables
    df['chemo_cat1'] = np.where(df['chemo_cat'] == 1, 1, 0)
    df['chemo_cat2'] = np.where(df['chemo_cat'] == 2, 1, 0)
    df['chemo_cat3'] = np.where(df['chemo_cat'] == 3, 1, 0)
   
    #Categorical GTV: create dummy variables
    df['gtv_cat1'] = np.where(df['gtv_cat'] == 1, 1, 0)
    df['gtv_cat2'] = np.where(df['gtv_cat'] == 2, 1, 0)
    df['gtv_cat3'] = np.where(df['gtv_cat'] == 3, 1, 0)
    df['gtv_cat4'] = np.where(df['gtv_cat'] == 4, 1, 0)
   
    print("atomcat_preprocess")
    return df

def atomcat_preprocess_dm2(df):
    
    # Only keep patients with no baseline metastases (M stage = 0)
    #df['m_stage'] = df['m_stage'].apply(pd.to_numeric, errors='coerce', downcast='integer')
    df = df[df['m_stage'] == 0]
    
    # Performance status: complete-case analysis
    df = df.dropna(subset=['perf_status'])
    # Performance status: create dummy variables
    df['perf_status1'] = df['perf_status'].apply(lambda x: 1 if x == 1 else 0)
    df['perf_status234'] = df['perf_status'].apply(lambda x: 1 if x > 1 else 0)
    
    # Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=['rt_technique'])
    df['rt_technique'] = df['rt_technique'].apply(lambda x: 0 if x <= 1 else 1)
    
    # Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = df['age'].apply(lambda x: 1 if x >= 50 and x <= 69 else 0)
    df['age70plus'] = df['age'].apply(lambda x: 1 if x >= 70 else 0)
    
    # Age: converting to age squared
    df['agesquared'] = df['age'].apply(lambda x: x ** 2)
    
    # Chemotherapy regimen: create dummy variables
    df['chemo_cat1'] = df['chemo_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['chemo_cat2'] = df['chemo_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['chemo_cat3'] = df['chemo_cat'].apply(lambda x: 1 if x == 3 else 0)
    
    # Categorical GTV: create dummy variables
    df['gtv_cat1'] = df['gtv_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['gtv_cat2'] = df['gtv_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['gtv_cat3'] = df['gtv_cat'].apply(lambda x: 1 if x == 3 else 0)
    df['gtv_cat4'] = df['gtv_cat'].apply(lambda x: 1 if x == 4 else 0)
    
    print("atomcat_preprocess")
    return df

def atomcat_preprocess_dm3(df):

    #df['m_stage'] = df['m_stage'].apply(pd.to_numeric, errors='coerce', downcast='integer')
    # Only keep patients with no baseline metastases (M stage = 0)
    df = df[df['m_stage'] == 0]
    
    # GTV: complete-case analysis
    df = df[df['pr_tumour_gtv'] != 62.0273]
    df = df[~df['pr_tumour_gtv'].isna()]
    
    # Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df[~df['rt_technique'].isna()]
    df['rt_technique'] = df['rt_technique'].apply(lambda x: 0 if x <= 1 else 1)
    
    # Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = df['age'].apply(lambda x: 1 if x >= 50 and x <= 69 else 0)
    df['age70plus'] = df['age'].apply(lambda x: 1 if x >= 70 else 0)
    
    # Age: converting to age squared
    df['agesquared'] = df['age'].apply(lambda x: x**2)
    
    # Chemotherapy regimen: create dummy variables
    df['chemo_cat1'] = df['chemo_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['chemo_cat2'] = df['chemo_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['chemo_cat3'] = df['chemo_cat'].apply(lambda x: 1 if x == 3 else 0)
    
    # Categorical GTV: create dummy variables
    df['gtv_cat1'] = df['gtv_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['gtv_cat2'] = df['gtv_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['gtv_cat3'] = df['gtv_cat'].apply(lambda x: 1 if x == 3 else 0)
    df['gtv_cat4'] = df['gtv_cat'].apply(lambda x: 1 if x == 4 else 0)
    
    print('atomcat_preprocess')
    return df

def atomcat_preprocess_os_lrc1(df):
    
    #Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=['rt_technique'])
    df['rt_technique'] = df['rt_technique'].apply(lambda x: 0 if x <= 1 else 1)
    
    #Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = df['age'].apply(lambda x: 1 if (x >= 50) and (x <= 69) else 0)
    df['age70plus'] = df['age'].apply(lambda x: 1 if x >= 70 else 0)
    
    #Age: converting to age squared
    df['agesquared'] = df['age'].apply(lambda x: x ** 2)
    
    #Chemotherapy regimen: create dummy variables
    df['chemo_cat1'] = df['chemo_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['chemo_cat2'] = df['chemo_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['chemo_cat3'] = df['chemo_cat'].apply(lambda x: 1 if x == 3 else 0)
    
    #Categorical GTV: create dummy variables
    df['gtv_cat1'] = df['gtv_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['gtv_cat2'] = df['gtv_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['gtv_cat3'] = df['gtv_cat'].apply(lambda x: 1 if x == 3 else 0)
    df['gtv_cat4'] = df['gtv_cat'].apply(lambda x: 1 if x == 4 else 0)
    
    print("atomcat_preprocess")
    return df

def atomcat_preprocess_os_lrc2(df):
      
    # Performance status: complete-case analysis
    df = df.dropna(subset=["perf_status"])

    # Performance status: create dummy variables
    df["perf_status1"] = df["perf_status"].apply(lambda x: 1 if x == 1 else 0)
    df["perf_status234"] = df["perf_status"].apply(lambda x: 1 if x > 1 else 0)

    # Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=["rt_technique"])
    df["rt_technique"] = df["rt_technique"].apply(lambda x: 0 if x <= 1 else 1)

    # Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df["age50to69"] = df["age"].apply(lambda x: 1 if x >= 50 and x <= 69 else 0)
    df["age70plus"] = df["age"].apply(lambda x: 1 if x >= 70 else 0)

    # Age: converting to age squared
    df["agesquared"] = df["age"].apply(lambda x: x ** 2)

    # Chemotherapy regimen: create dummy variables
    df["chemo_cat1"] = df["chemo_cat"].apply(lambda x: 1 if x == 1 else 0)
    df["chemo_cat2"] = df["chemo_cat"].apply(lambda x: 1 if x == 2 else 0)
    df["chemo_cat3"] = df["chemo_cat"].apply(lambda x: 1 if x == 3 else 0)

    # Categorical GTV: create dummy variables
    df["gtv_cat1"] = df["gtv_cat"].apply(lambda x: 1 if x == 1 else 0)
    df["gtv_cat2"] = df["gtv_cat"].apply(lambda x: 1 if x == 2 else 0)
    df["gtv_cat3"] = df["gtv_cat"].apply(lambda x: 1 if x == 3 else 0)
    df["gtv_cat4"] = df["gtv_cat"].apply(lambda x: 1 if x == 4 else 0)

    print("atomcat_preprocess")
    return df

def atomcat_preprocess_os_lrc3(df):
    # GTV: complete-case analysis
    df = df[df['pr_tumour_gtv'] != 62.0273]
    df = df.dropna(subset=['pr_tumour_gtv'])
    
    # Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=['rt_technique'])
    df['rt_technique'] = df['rt_technique'].apply(lambda x: 0 if x <= 1 else 1)
    
    # Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = df['age'].apply(lambda x: 1 if 50 <= x <= 69 else 0)
    df['age70plus'] = df['age'].apply(lambda x: 1 if x >= 70 else 0)
    
    # Age: converting to age squared
    df['agesquared'] = df['age'].apply(lambda x: x**2)
    
    # Chemotherapy regimen: create dummy variables
    df['chemo_cat1'] = df['chemo_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['chemo_cat2'] = df['chemo_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['chemo_cat3'] = df['chemo_cat'].apply(lambda x: 1 if x == 3 else 0)
    
    # Categorical GTV: create dummy variables
    df['gtv_cat1'] = df['gtv_cat'].apply(lambda x: 1 if x == 1 else 0)
    df['gtv_cat2'] = df['gtv_cat'].apply(lambda x: 1 if x == 2 else 0)
    df['gtv_cat3'] = df['gtv_cat'].apply(lambda x: 1 if x == 3 else 0)
    df['gtv_cat4'] = df['gtv_cat'].apply(lambda x: 1 if x == 4 else 0)
    
    print("atomcat_preprocess")
    return df

def atomcat_preprocess_os_lrc4(df):
    
    # Completed treatment: complete-case analysis
    df = df.dropna(subset=['compl_treatement'])
    df = df[df['compl_treatement'] != 'NA']
    
    # Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=['rt_technique'])
    df.loc[df['rt_technique'] <= 1, 'rt_technique'] = 0
    df.loc[df['rt_technique'] > 1, 'rt_technique'] = 1
    
    # Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = np.where((df['age'] >= 50) & (df['age'] <= 69), 1, 0)
    df['age70plus'] = np.where(df['age'] >= 70, 1, 0)
    
    # Age: converting to age squared
    df['agesquared'] = df['age'] ** 2
    
    # Chemotherapy regimen: create dummy variables
    df['chemo_cat1'] = np.where(df['chemo_cat'] == 1, 1, 0)
    df['chemo_cat2'] = np.where(df['chemo_cat'] == 2, 1, 0)
    df['chemo_cat3'] = np.where(df['chemo_cat'] == 3, 1, 0)
    
    # Categorical GTV: create dummy variables
    df['gtv_cat1'] = np.where(df['gtv_cat'] == 1, 1, 0)
    df['gtv_cat2'] = np.where(df['gtv_cat'] == 2, 1, 0)
    df['gtv_cat3'] = np.where(df['gtv_cat'] == 3, 1, 0)
    df['gtv_cat4'] = np.where(df['gtv_cat'] == 4, 1, 0)
    
    return df

'''def atomcat_preprocess_os_lrc5(df):
    
    # Overall treatment time: complete-case analysis
    df = df.dropna(subset=['overall_treatment_time'])
    df = df[df['overall_treatment_time'] != 'NA']
    
    # Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
    df = df.dropna(subset=['rt_technique'])
    df['rt_technique'] = df['rt_technique'].apply(lambda x: 0 if x <= 1 else 1)
    
    # Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
    df['age50to69'] = np.where((df['age'] >= 50) & (df['age'] <= 69), 1, 0)
    df['age70plus'] = np.where(df['age'] >= 70, 1, 0)
    
    # Age: converting to age squared
    df['agesquared'] = df['age'] ** 2
    
    # Chemotherapy regimen: create dummy variables
    df = pd.concat([df, pd.get_dummies(df['chemo_cat'], prefix='chemo_cat')], axis=1)
    
    # Categorical GTV: create dummy variables
    df = pd.concat([df, pd.get_dummies(df['gtv_cat'], prefix='gtv_cat')], axis=1)
    
    return df'''

def atomcat_preprocess_os_lrc5(df):
  
  #Overall treatment time: complete-case analysis
  df = df.dropna(subset=['overall_treatment_time'])
  df = df[df['overall_treatment_time'] != 'NA']
  
  #Radiotherapy technique: converting to IMRT/VMAT vs 3D conformal
  df = df.dropna(subset=['rt_technique'])
  df['rt_technique'] = np.where(df['rt_technique'] <= 1, 0, 1)
  
  #Age: converting to cutoff: 50-69 vs <50 and 70+ vs <50
  df['age50to69'] = np.where((df['age'] >= 50) & (df['age'] <= 69), 1, 0)
  df['age70plus'] = np.where(df['age'] >= 70, 1, 0)
  
  #Age: converting to age squared
  df['agesquared'] = df['age'] ** 2
  
  #Chemotherapy regimen: create dummy variables
  df['chemo_cat1'] = np.where(df['chemo_cat'] == 1, 1, 0)
  df['chemo_cat2'] = np.where(df['chemo_cat'] == 2, 1, 0)
  df['chemo_cat3'] = np.where(df['chemo_cat'] == 3, 1, 0)
  
  #Categorical GTV: create dummy variables
  df['gtv_cat1'] = np.where(df['gtv_cat'] == 1, 1, 0)
  df['gtv_cat2'] = np.where(df['gtv_cat'] == 2, 1, 0)
  df['gtv_cat3'] = np.where(df['gtv_cat'] == 3, 1, 0)
  df['gtv_cat4'] = np.where(df['gtv_cat'] == 4, 1, 0)
  
  return df



'''def check_datatypes(data):
    for col in data.columns:
        if data[cols] is str:
            if cols in ['pr_tumour_gtv','perf_status','compl_treatement','overall_treatment_time']:
                data[cols] = data[cols].astype(float)
            elif cols in ['age','sex','t_stage','m_stage','gtv_cat','chemo_cat','rt_technique','dm_status','dm_fup']:
                data[cols] = data[cols].astype(int)
            else:
                print("Nothing to convert")
        else:
            print("Nothing to convert")'''


#if data[col].isnull().values.any() is True:
                 #   print("NaN Values")
                #else:
                 #   data[col] = pd.to_numeric(data[col], errors='coerce')
                  #  data[col] = data[col].astype("Int64")


 #if data[col].isnull().values.any() is True:
                 #   print("NaN Values")
                #else:
                 #   data[col] = pd.to_numeric(data[col], errors='coerce')
                  #  data[col] = data[col].astype(float)


def check_datatypes(data):
    for col in data.columns:
        if data[col].dtype=='object':
            if col in ['pr_tumour_gtv', 'perf_status', 'compl_treatement', 'overall_treatment_time']:
                data[col] = data[col].apply(pd.to_numeric, errors='coerce', downcast='float')
            elif col in ['age', 'sex', 't_stage', 'm_stage', 'gtv_cat', 'chemo_cat', 'rt_technique', 'dm_status', 'dm_fup']:
                data[col] = data[col].apply(pd.to_numeric, errors='coerce', downcast='integer')  
            else:
                print(f"No datatype conversion required for column {col}")
        else:
            print(f"No datatype conversion required for column {col}")


def apply_filter_atomcat(data, filter):

    print("Filtering Scripts")

    if isinstance(filter,str) == False:
        filter=str(filter)

    check_datatypes(data)

    if filter == "1":
        print("Filter 1")
        filter_data = atomcat_preprocess_dm1(data)
    elif filter == "2":
        print("Filter 2")
        filter_data = atomcat_preprocess_dm2(data)
    elif filter == "3":
        print("Filter 3")
        filter_data = atomcat_preprocess_dm3(data)
    elif filter == "4":
        print("Filter 4")
        filter_data = atomcat_preprocess_os_lrc1(data)
    elif filter == "5":
        print("Filter 5")
        filter_data = atomcat_preprocess_os_lrc2(data)
    elif filter == "6":
        print("Filter 6")
        filter_data = atomcat_preprocess_os_lrc3(data)
    elif filter == "7":
        print("Filter 7")
        filter_data = atomcat_preprocess_os_lrc4(data)
    elif filter == "8":
        print("Filter 8")
        filter_data = atomcat_preprocess_os_lrc5(data)
    else:
        print("No Filter")
        filter_data=data

    return filter_data