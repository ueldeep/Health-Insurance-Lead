import os as os
import pandas as pd


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def columns_profile(df, columns_dic ,columns=None, sep='_', print_unique_values=True, num_values=5):
    if columns == None:
        column_list = df.columns
    else:
        column_list = columns

    for col in column_list:
        datatype = df[col].dtypes
        unique_values = df[col].unique()
        number_unique_values = len(unique_values)
        print(f'{style.BLUE}{col}({style.RED}{datatype}{style.BLUE}), No. unique values:{style.BLACK}{number_unique_values}')
        if print_unique_values == True:
            print(f'\t{style.BLACK}{unique_values[:num_values]}')
        if sep != None:
            print(sep*50)
        


columns_dic = {'Numeric':[],
         'Datetime':[],
         'Timedelta':[],
         'Categorical':[],
         'String':[],
          'y':[]} 

def convert_datatype(df, columns_dic):
    #convert number columns
    for col in columns_dic['Numeric']:
        if df[col].dtypes == 'object':
            df[col] = pd.to_numeric(df[col],errors='coerce')
    #convert datetime columns
    for col in columns_dic['Datetime']:
        if df[col].dtypes == 'object':
            df[col] = pd.to_datetime(df[col],errors='coerce')
    #convert timedelta columns
    for col in columns_dic['Timedelta']:
        if df[col].dtypes == 'object':
            df[col] = pd.to_timedelta(df[col],errors='coerce')

def count_rows_null_values(df):
    row_null_count = pd.Series(index=df.index,data=np.array(range(df.shape[0])))
    for i in range(df.shape[0]):
        row_null_count[i]=df.loc[i].isnull().sum()
    return row_null_count

def get_email_provider(email):
    return email.split('@')[1]

def map_hours(x):
    if x in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
        return 'morning'
    elif x in [13,14,15,16]:
        return 'afternoon'
    else:
        return 'evening'
    
def map_seasons(x, hemisphere='Northern'):
    ret_val = None
    if hemisphere == 'Northern':
        if x in [12,1,2]:
            ret_val = 'Winter'
        elif x in [3,4,5]:
            ret_val = 'Spring'
        elif x in [6,7,8]:
            ret_val = 'Summer'
        else :
            ret_val = 'Autumn'
    elif hemisphere == 'Southern':
        if x in [12,1,2]:
            ret_val = 'Summer'
        elif x in [3,4,5]:
            ret_val = 'Autumn'
        elif x in [6,7,8]:
            ret_val = 'Winter'
        else :
            ret_val = 'Sprint'
    return ret_val

