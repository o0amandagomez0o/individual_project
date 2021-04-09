#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from scipy import stats

#functions
#import wrangle as wr
#import explore as exp
#import model as mo


warnings.filterwarnings("ignore")

#evaluate
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.feature_selection import f_regression 
from statsmodels.formula.api import ols
import sklearn.preprocessing

#feature engineering
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# modeling methods
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures

'''
*------------------*
|                  |
|     ACQUIRE      |
|                  |
*------------------*
'''

def get_aac():
    """
    get_aac will :
    - read in Austin_Animal_Center_Intakes.csv & Austin_Animal_Center_Outcomes.csv
    return: right merged pandas dataframe
    """
    
    aac_intake = pd.read_csv('Austin_Animal_Center_Intakes.csv')
    
    aac_outcome = pd.read_csv('Austin_Animal_Center_Outcomes.csv')
    
    #df = pd.merge(aac_intake, aac_outcome, how='right')
    
    return pd.merge(aac_intake, aac_outcome, how='right')




    
'''
*------------------*
|                  |
|     PREPARE      |
|                  |
*------------------*
'''

def clean_aac(df):
    """
    
    """
    
    df = df.rename(columns={"Name": "name", "DateTime": "date", "MonthYear": "monthyear", "Animal ID": "animal_id", 
                       "Found Location": "found_loc", "Intake Type": "intake_type", "Intake Condition": "intake_cond", 
                       "Animal Type": "animal_type", "Sex upon Intake": "intake_sex", "Age upon Intake": "intake_age", 
                       "Breed": "breed", "Color": "color", "Date of Birth": "dob", "Outcome Type": "outcome_type", 
                       "Outcome Subtype": "outcome_subtype", "Sex upon Outcome": "outcome_sex", "Age upon Outcome": "outcome_age"})

    
    # remove time from `datetime` col  and convert dtype to date
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    dropcols = ['name', 'monthyear', 'found_loc', 'intake_type', 'intake_cond', 'intake_sex', 'intake_age', 'outcome_subtype']
    df = df.drop(columns= dropcols)
    
    # drop negative age observations
    df = df[(df.outcome_age != '-1 years') & (df.outcome_age != '-2 years') & (df.outcome_age != '-3 years')]
    
    # drop blank outcome_type observations
    df = df[(df.outcome_type).isin(df.outcome_type.dropna())]
    
    # Drop blank outcome_age
    df = df[(df.outcome_age).isin(df.outcome_age.dropna())]

    # Drop blank outcome_sex
    df = df[(df.outcome_sex).isin(df.outcome_sex.dropna())]
    
    # filter df to only cats and dogs
    df = df[(df.animal_type != 'Other') & (df.animal_type != 'Bird') & (df.animal_type != 'Livestock')]
    
    # filter df to remove pets returned to owners
    df = df[(df.outcome_type != 'Return to Owner') & (df.outcome_type != 'Rto-Adopt')]
    
    # convert all 'puppies' to '0 years'
    df['outcome_age'] = np.where(df['outcome_age'].str.contains('day|days|weeks|week|month|months'), "0 years", df.outcome_age)
    
    # convert 'year' to 'years'
    df.replace('1 year', '1 years', inplace = True )
    
    # convert outcome_age to integer
    df['outcome_age'] = df.outcome_age.str.replace('years', '').astype(int)
    
    #encode ages
    df['elderly'] = np.where(df.outcome_age > 5, 1, 0 )
    df['full_grown'] = np.where((df.outcome_age < 6) & (df.outcome_age > 1), 1, 0 )
    df['youngins'] = np.where(df.outcome_age < 2, 1, 0 )
    
    # encode sex
    df['neutered_male'] = np.where(df.outcome_sex ==  "Neutered Male", 1, 0 )
    df['intact_male'] = np.where(df.outcome_sex ==  "Intact Male", 1, 0 )
    df['neutered'] = np.where((df.outcome_sex ==  "Neutered Male") | (df.outcome_sex ==  "Spayed Female"), 1, 0 )
    
    # encode animal_type
    dummy_df = pd.get_dummies(df.animal_type, prefix="is", drop_first=True)
    
    # new columns
    df['is_pitbull'] = np.where(df['breed'].str.contains('Pit|American Staffordshire|Staffordshire'), 1, 0)
    
    df['is_black'] = np.where(df.color == "Black", 1, 0)
    
        
    # encode outcome_type
    df['adopted'] = np.where(df.outcome_type == "Adoption", 1, 0)
    
    # drop duplicates
    df = df.sort_values('date').drop_duplicates('animal_id', keep='last')
    
    # drop encoded/unncessary columns
    cols = ['animal_type', 'outcome_type', 'outcome_sex', 'outcome_age']
    df = df.drop(columns= cols)
    
    
    return df





